#import "@local/mytemplate:0.1.0": *
#import "@local/treemap:0.1.0": treemap

#set heading(numbering: Numbering.with(first-level: "一、", "1.1"))

// apply the template
#show: report.with(
  media: "screen",
  theme: "dark",
  show-outline: false,
)

= 深度学习科研代码管理和实验管理面临的问题

深度学习模型结构变化程度大、参数多，如何高效地进行代码和实验管理？

+ *环境管理*：如何保证代码运行环境可复现；
+ *模块管理*：如何划分模型的核心和任务，以及一些辅助的目录；
+ *分支管理*：如何划分 git 分支；
+ *大文件管理*：如何管理数据集、模型文件等大型二进制文件；
+ *参数管理*：如何管理训练参数；
+ *结果管理*：如何管理日志、输出数据和实验结果；
+ *进度管理*：如何可视化训练进度、训练用时；
+ *随机数管理*：如何处理实验的 random seed；
+ *错误处理*：如何处理 Python 中的错误，避免实验中断；
+ *调试模式*：如何实现小数据集的调试模式，避免执行用时过长；
+ *图表管理*：如何管理论文中可能用到的文档图表；
+ *文档管理*：如何编写和管理文档，包括笔记、论文和 slides。


= 环境管理

使用 `requirements.txt` 和 #link("https://docs.conda.io/projects/miniconda/en/latest/", "miniconda") 来管理项目的环境。

conda 新建环境：

```sh
conda create -n envName python=3.9
```

conda 查看所有环境：

```sh
conda env list
```

conda 删除环境：

```sh
conda env remove -n envName
```

生成 `requirements.txt` 文件：

```sh
pip freeze > requirements.txt
```

安装 `requirements.txt` 依赖：

```sh
pip install -r requirements.txt
```

使用 conda 安装 `requirements.txt` 依赖：

```sh
conda install --yes --file requirements.txt
```


使用 conda 安装 `requirements.txt` 依赖（失败时用 pip 重试）：

```sh
while read requirement; do conda install --yes $requirement || pip install $requirement; done < requirements.txt
```


= 模块管理

良好的目录划分和模块划分是可维护性的关键。一般可以分为这几大块：

#treemap[
  - 数据
    - 原始数据
    - 预处理数据
    - 模型文件
    - 日志数据
    - 实验数据
    - 实验结果
    - 文档
  - 稳定代码
    - I/O 模块
    - 预处理模块
    - 可视化模块
    - 数据加载模块
    - 模型主体
    - 损失函数
    - 后处理模块
    - 训练函数模块
  - 易变代码
    - 实验参数配置
    - 训练/测试脚本
]


= 分支管理

我们应该使用 git 分支管理管理好我们的主分支和实验分支，并且分支的命名要有一定的规则，必要的话可以通过脚本来自动化。

这里的分支管理规则参考了常见的 #link("https://www.ruanyifeng.com/blog/2012/07/git.html", "Git Flow") 开发流程（推荐 10 到 20 人共同开发），并根据深度学习科研的代码管理特性进行了一定的改良。

这里是理论上的较复杂项目的最佳实践，可以根据自己的情况进行一定程度的化简，例如去除 `dev` 分支，只留下 `main` 分支并解除相应限制。

== main 主分支

长期分支，应该始终保持为一个最新的可用版本，即版本发布状态。

`main` 主分支需要有最严格的权限管理，不能直接提交 commit 到 `main` 分支，只能合并其他分支，因此最好开启分支保护。只有在 `dev` 分支上的代码达到一个稳定状态之后，才能合并到 `main` 分支。

简单的 `hotfix-xxx` 分支（数行代码的修改）可以在确认无误后合并到 `main` 分支（也需要同步到 `dev` 分支）。除了 `dev` 和 `hotfix-xxx` 分支以外的分支都不能合并到 `main` 分支。

合并命令：

```sh
git checkout main
git merge --squash dev
```

这里使用 squash merge 可以将 `dev` 分支新增的 commits 压缩为一个 commit 并加入 `main` 中。这样做能够让 `main` 分支的 commit 记录保持简洁。

但是这样 main 的 commit 记录提交者就变成了执行 merge 操作的那个人，所以最好是由特性分支的开发者执行 merge。为了解决记录提交者问题，也可以考虑常规的非快进模式 merge `git --no-ff merge dev` 或 #link("https://www.jianshu.com/p/ff1877c5864e", "rebase merge")。

在 merge 之后还需要 `dev` 重新 merge 一下 `main` 分支的最新提交，这样才能让 `dev` 保持最新的 commit 记录，方便下次 merge。

```sh
git checkout dev
git merge main
```

== dev 开发分支

长期分支，用于保持最新的开发进度，主要开发工作都应该在这个分支进行。

由于深度学习科研中的代码常常仅由单人（或几个人）进行开发，所以应当允许在 dev 分支直接进行开发和提交 commit。

`dev` 分支可以合并任何其他分支，例如 `feature-xxx` 和 `hotfix-xxx` 分支。

== feature-xxx 特性分支

临时分支，用于开发某一个特性模块，例如预处理模块、可视化模块等。

特性分支一般是在多人开发的情形下使用，能够方便地进行并行化开发，也可以用于区分不同模块的开发，让开发过程更具区分性。

一般一个特性分支专注于一个功能，而且应该只是临时的，不应该长期存在。完成后应该先合并至 `dev` 分支，确认稳定后再经由 `dev` 分支合并到 `main` 分支。

== hotfix-xxx 修复分支

临时分支，仅用于 bug 的紧急修复。

`hotfix-xxx` 分支是为了应对 `dev` 分支还不稳定，不能合并到 `main` 分支，但是又需要紧急修复的情况而使用的，否则可以直接在 `dev` 分支上修复。

分支内不应该包含过多的删除或新增代码，即不应该是实现功能，而应该是修复功能。

`hotfix-xxx` 分支可以直接合并到 `dev` 和 `main` 分支。

== exper-xxx 实验分支

临时分支，用于修改实验参数，然后跑一次实验，并记录结果。

只能从 `main` 中分支出来（模型变更后需要先更新模型版本，并打一个 git tag），并且应该由一个自动化脚本创建，根据模型版本-时间戳-模型参数的维度命名，便于辨识。

只应该用于修改超参数后执行一次实验，并记录结果，不应该更改具体的代码。如果认为需要修改具体代码，请考虑是否应该新增一个超参数用于控制，或者是否应该在其他如 `dev` 和 `hotfix-xxx` 分支中进行修复。

记录的内容可以包括：

- 复制一份当前的 Yaml 参数文件，可以根据分支名判断应该使用这份文件作为参数输入；
- 也可以加入一份自定义训练脚本；
- 记录代码执行的 log 日志；
- 记录实验的原始图表数据文件（便于后续生成图表）；
- 实验的具体输出结果；
- 在汇总的表格文件中新增一条结果（或者由脚本自动化执行）。

由于没有代码层面的变更，执行完成后可以直接合并到 `dev` 和 `main` 分支中。

== debug-xxx 调试分支

临时分支，用于在 debug 模式下跑一次实验，用于验证是否能正常地跑通训练流程。

可以从 `main` 或 `dev` 中分支出来，并且应该由一个自动化脚本创建。

该分支的变更都不应该保存到其他分支里，包括数据变更和代码变更。如果有代码的修复，可以使用 `git stash` 暂存代码并切换到 `dev` 或 `hotfix-xxx` 分支修复。

== commit 提交规范

常规规范：

- `feat`：新功能（feature）
- `fix`：修复 bug
- `docs`：文档（documentation）
- `style`：代码风格（不影响代码运行的变动）
- `refactor`：重构（即不是新增功能，也不是修改 bug 的代码变动）
- `test`：增加测试
- `chore`：构建过程或辅助工具的变动

深度学习科研代码新增规范：

- `exper`: 合并一个 `exper-xxx` 分支的实验执行结果。

在 merge 到 `main` 主分支时，merge 的 commit 信息也应该遵循这个规范。

= 大文件管理

我们使用数据版本控制（DVC）进行大文件的管理，其允许在 Git 提交中数据和模型的版本，同时将它们存储在本地或云存储中。

我们既可以#link("https://juejin.cn/post/7057767026072223751", "在命令行中使用")，也可以在 VS Code 中安装 DVC 插件来使用。

== 跟踪数据文件

```sh
dvc add data/data.xml
```

这个命令会将文件信息存储到名为 `data/data.xml.dvc` 的特殊文件中，并且会将原始数据放在 `.gitignore` 文件中。

然后将数据移动到目录的缓存 `.dvc/cache` 中，并将其链接回工作区。

所以我们可以放心地将这些元信息文件放入 git 仓库中托管，如果数据文件发生了更改，则我们应该重新执行 `dvc add` 命令来追踪更改，这会更新 `data/data.xml.dvc` 文件，进而让我们能在 git 中记录当前的数据版本。


== 远程存储库同步

可以使用 `dvc push` 上传 DVC 跟踪的数据或模型文件，后续也可以通过 `dvc pull` 进行恢复。

我们需要设置一个原创存储库的地址，例如 Amazon S3、SSH、Google Drive 等。


== 在版本之间进行切换

当使用 `git checkout xxx` 切换了分支之后，我们可以执行

```sh
dvc checkout
```

来切换数据文件的版本，也即 DVC 会根据所有的 `.dvc` 文件来切换到正确的数据文件版本。

可以看出 DVC 的实现原理还是相对简单的，整体小巧而精致，但是可以很有效地和 git 共同工作，维护我们的数据文件，并且保证 git repo 的体积不会过于庞大。


= 参数管理

命令行 input argparse 并不是必须的，这里更加推荐使用 Yaml 文件来管理参数，参数包括项目设置、模型参数等。

参数文件里至少要包含：

- `VERSION`: 用于记录当前的模型版本，例如 `0.1.0`。
- `DEBUG`: 是否开启 debug 模式，即使用小型数据集。

