import torch

# 超参数学习
config = {
    'random_seed': 42,
    'batch_size': 100,
    'hidden_size': [5, 10, 20, 50],
    'hidden_layers': [1, 2, 3],
    'lmbda': [10 * 10 ** -4.4],
    'checkpoint': 10,
    'epochs': 200,
    'lr': [0.001, 0.005, 0.01],
    'weight_decay': 0.0,
}

# 最佳超参数
# config = {
#     'random_seed': 42,
#     'batch_size': 100,
#     'hidden_size': [5],
#     'hidden_layers': [3],
#     'lmbda': [10 * 10 ** -4.4],
#     'checkpoint': 10,
#     'epochs': 190,
#     'lr': [0.01],
#     'weight_decay': 0.0,
# }

# 寻找最佳 lmbda = 10 ** -4.4
# 注意要将损失函数改为 (1 / lmbda) * MSE + lmbda * |y| 再跑
# config = {
#     'random_seed': 42,
#     'batch_size': 100,
#     'hidden_size': [10],
#     'hidden_layers': [2],
#     'lmbda': 10 ** torch.linspace(-3, 0, 21)[:-1],
#     'checkpoint': 50,
#     'epochs': 50,
#     'lr': [0.005],
#     'weight_decay': 0.0,
# }


class gmm_dataset:

    def __init__(self, size):
        '''
        一个 GMM Dataset, 混合高斯 0.25 N(0, 1) + 0.75 N(6, 4)
        '''

        self.size = size

        # 生成训练集
        # 生成 n 个样本点
        data = torch.randn(size, 1)
        # 生成 n 个 0-1 的随机数, 用于判断取哪个高斯分布
        rand = torch.rand(size).reshape(-1, 1)
        # 生成 n 个样本点的标签
        # 通过 where 函数, 设置 data 的值
        data = torch.where(rand < 0.25, data * 1 + 0, data * 2 + 6)
        self.data = data.reshape(-1)

    def __len__(self):
        return self.size

    def __getitem__(self, idx):
        return self.data[idx]


# 设置随机种子
torch.manual_seed(config['random_seed'])
# 生成 10000 个样本点作为训练集, 1000 个样本点作为验证集, 1000 个样本点作为测试集
dataset = gmm_dataset(12000)
train_dataset, valid_dataset, test_dataset = torch.utils.data.random_split(
    dataset, [10000, 1000, 1000])
train_loader = torch.utils.data.DataLoader(
    train_dataset, batch_size=config['batch_size'], shuffle=True)
valid_loader = torch.utils.data.DataLoader(
    valid_dataset, batch_size=config['batch_size'], shuffle=True)
test_loader = torch.utils.data.DataLoader(
    test_dataset, batch_size=config['batch_size'], shuffle=True)


class autoencoder(torch.nn.Module):

    def __init__(self, hidden_size, hidden_layers):
        '''
        神经网络, 输入为一个实数 x, 经过一个编码器得到 y,
        再通过加一个随机数 epsilon in U(-0.5, 0.5) 得到 yhat,
        最后通过一个解码器得到 xhat
        '''
        super().__init__()

        self.hidden_size = hidden_size
        self.encoder = torch.nn.Sequential()
        self.encoder.add_module('input', torch.nn.Linear(1, hidden_size))
        self.encoder.add_module('relu_input', torch.nn.ReLU())
        for i in range(hidden_layers):
            self.encoder.add_module(
                f'hidden_layer_{i}', torch.nn.Linear(hidden_size, hidden_size))
            self.encoder.add_module(f'relu_{i}', torch.nn.ReLU())
        self.encoder.add_module('output', torch.nn.Linear(hidden_size, 1))

        self.decoder = torch.nn.Sequential()
        self.decoder.add_module('input', torch.nn.Linear(1, hidden_size))
        self.decoder.add_module('relu_input', torch.nn.ReLU())
        for i in range(hidden_layers):
            self.decoder.add_module(
                f'hidden_layer_{i}', torch.nn.Linear(hidden_size, hidden_size))
            self.decoder.add_module(f'relu_{i}', torch.nn.ReLU())
        self.decoder.add_module('output', torch.nn.Linear(hidden_size, 1))

    def encode_y(self, x):
        y = self.encoder(x)
        return y

    def round(self, y, is_train=True):
        if is_train:
            # 训练时是 y + epsilon
            epsilon = torch.rand_like(y) - 0.5
            yhat = y + epsilon
        else:
            # 测试时是取整 [y]
            yhat = torch.round(y)
        return yhat
    
    def encode(self, x, is_train=True):
        y = self.encode_y(x)
        yhat = self.round(y, is_train)
        return yhat

    def decode(self, yhat):
        xhat = self.decoder(yhat)
        return xhat

    def forward(self, x, is_train=True):
        yhat = self.encode(x, is_train)
        xhat = self.decode(yhat)
        return xhat


# 开始训练
def train(model, train_loader, valid_loader, lmbda, checkpoint, epochs=100, lr=0.001, weight_decay=0.0, silent=False):
    # 优化器
    optimizer = torch.optim.Adam(
        model.parameters(), lr=lr, weight_decay=weight_decay)
    # 损失函数 = MSE + lambda * y
    MSELoss = torch.nn.MSELoss()
    criterion = lambda x, y, xhat: MSELoss(x, xhat) + lmbda * torch.mean(torch.abs(y))
    # 训练
    for epoch in range(1, epochs + 1):
        # 训练集
        train_loss = 0.0
        model.train()
        for x in train_loader:
            x = x.reshape(-1, 1)
            y = model.encode_y(x)
            yhat = model.round(y, is_train=True)
            xhat = model.decode(yhat)
            loss = criterion(x, y, xhat)
            train_loss += loss.item()
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        # 验证集
        model.eval()
        with torch.no_grad():
            valid_loss = 0.0
            for x in valid_loader:
                x = x.reshape(-1, 1)
                y = model.encode_y(x)
                yhat = model.round(y, is_train=False)
                xhat = model.decode(yhat)
                valid_loss += criterion(x, y, xhat)
            train_loss /= len(train_loader)
            valid_loss /= len(valid_loader)
            if epoch % checkpoint == 0:
                yield epoch, train_loss, valid_loss
                if not silent:
                    print(
                        f'epoch: {epoch}, train_loss: {train_loss}, valid_loss: {valid_loss}')


best_valid_loss = float('inf')
best_hidden_size = config['hidden_size'][0]
best_hidden_layers = config['hidden_layers'][0]
best_epochs = 0
best_lr = config['lr'][0]

def find_best_model(train_loader, valid_loader, config):
    # 对 config 中的每个参数进行网格搜索
    best_model = None
    count = 0
    best_lmbda = 0.
    global best_valid_loss
    global best_hidden_size
    global best_hidden_layers
    global best_epochs
    global best_lr
    for hidden_size in config['hidden_size']:
        for hidden_layers in config['hidden_layers']:
            for lmbda in config['lmbda']:
                for lr in config['lr']:
                    torch.manual_seed(config['random_seed'])
                    model = autoencoder(
                        hidden_size=hidden_size, hidden_layers=hidden_layers)
                    for epochs, train_loss, valid_loss in train(model, train_loader, valid_loader, lmbda=lmbda,
                                                epochs=config['epochs'], checkpoint=config['checkpoint'], lr=lr, weight_decay=config['weight_decay'], silent=True):
                        count += 1
                        print(
                            f'{count}: hidden_size: {hidden_size}, hidden_layers: {hidden_layers}, lmbda: {lmbda}, epochs: {epochs}, lr: {lr}:\n   train_loss: {train_loss}, valid_loss: {valid_loss}')
                        # 保存最好的模型
                        if valid_loss < best_valid_loss:
                            best_model = model
                            best_valid_loss = valid_loss
                            best_hidden_size = hidden_size
                            best_hidden_layers = hidden_layers
                            best_lmbda = lmbda
                            best_epochs = epochs
                            best_lr = lr
    return best_model, best_lmbda


best_model, best_lmbda = find_best_model(train_loader, valid_loader, config)
print(f'best_hidden_size: {best_hidden_size}')
print(f'best_hidden_layers: {best_hidden_layers}')
print(f'best_lmbda: {best_lmbda}')
print(f'best_epochs: {best_epochs}')
print(f'best_lr: {best_lr}')
print(f'best_valid_loss: {best_valid_loss}')
print(best_model)

# 测试
def test(model, test_loader, lmbda):
    model.eval()
    # 损失函数 = MSE + lambda * y
    criterion = lambda x, y, xhat: torch.nn.MSELoss()(x, xhat) + lmbda * torch.mean(torch.abs(y))
    with torch.no_grad():
        loss = 0.0
        for x in test_loader:
            x = x.reshape(-1, 1)
            y = model.encode_y(x)
            yhat = model.round(y, is_train=False)
            xhat = model.decode(yhat)
            loss += criterion(x, y, xhat)
        loss /= len(test_loader)
        print(f'test loss: {loss}')

test(best_model, test_loader, best_lmbda)


def predict(model, x):
    with torch.no_grad():
        yhat = model.encode(x, is_train=False)
        xhat = model.decode(yhat)
    return x, yhat, xhat

def print_result(x, yhat, xhat):
    print(f'x = {x.item()}, yhat = {yhat.item()}, xhat = {xhat.item()}')

print_result(*predict(best_model, torch.tensor([-1.])))
print_result(*predict(best_model, torch.tensor([0.5])))
print_result(*predict(best_model, torch.tensor([1.25])))
print_result(*predict(best_model, torch.tensor([4.5])))
print_result(*predict(best_model, torch.tensor([6.])))
print_result(*predict(best_model, torch.tensor([6.5])))

print_result(*predict(best_model, torch.tensor([-100.])))
print_result(*predict(best_model, torch.tensor([-50.])))
print_result(*predict(best_model, torch.tensor([50.])))
print_result(*predict(best_model, torch.tensor([100.])))

