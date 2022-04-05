from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

X, y = load_boston(return_X_y=True)
trainx, testx, trainy, testy = train_test_split(
    X, y, test_size=0.33, random_state=42)


def linReg(X_train: np.ndarray, y_train: np.ndarray) -> np.ndarray:
    # linear regression
    ones = np.ones(X_train.shape[0]).reshape(-1, 1)
    X_splash = np.hstack((X_train, ones))
    T: np.ndarray = np.linalg.inv(X_splash.transpose() @ X_splash)
    return T @ X_splash.transpose() @ y_train


def linRegMSE(X_train: np.ndarray, y_train: np.ndarray, X_test: np.ndarray, y_test: np.ndarray) -> float:
    weights = linReg(X_train, y_train).reshape(-1, 1)
    ones = np.ones(X_test.shape[0]).reshape(-1, 1)
    X_splash = np.hstack((X_test, ones))
    E: np.ndarray = y_test.reshape(-1, 1) - X_splash @ weights
    # return E.transpose() @ E / X_test.shape[0]
    return np.mean(E ** 2)


def reportLinRegMSE():
    return linRegMSE(trainx, trainy, testx, testy)


def ridgeReg(X_train: np.ndarray, y_train: np.ndarray, lmbd: float) -> np.ndarray:
    # ridge regression
    ones = np.ones(X_train.shape[0])
    eye = np.eye(X_train.shape[1])
    T: np.ndarray = np.linalg.inv(
        X_train.transpose() @ X_train + 2 * lmbd * eye)
    S: np.ndarray = ones @ X_train @ T @ X_train.transpose() - ones
    b = (S @ y_train) / (S @ ones)
    w = T @ X_train.transpose() @ (y_train - b * ones)
    return np.hstack((w, b))


def ridgeRegMSE(X_train: np.ndarray, y_train: np.ndarray, X_test: np.ndarray, y_test: np.ndarray, lmbd: float) -> float:
    weights = ridgeReg(X_train, y_train, lmbd).reshape(-1, 1)
    ones = np.ones(X_test.shape[0]).reshape(-1, 1)
    X_splash = np.hstack((X_test, ones))
    E: np.ndarray = y_test.reshape(-1, 1) - X_splash @ weights
    # return E.transpose() @ E / X_test.shape[0]
    return np.mean(E ** 2)


def reportRidgeRegMSE(lmbd):
    return ridgeRegMSE(trainx, trainy, testx, testy, lmbd)

print(linReg(trainx, trainy))
print(ridgeReg(trainx, trainy, 0))
print(reportLinRegMSE())
print(reportRidgeRegMSE(0))
lmbds = np.arange(-2, 2.1, 0.4)
mses = [reportRidgeRegMSE(lmbd) for lmbd in lmbds]
print(lmbds)
print(mses)
plt.plot(lmbds, mses)
plt.xlabel('lambda')
plt.ylabel('MSE')
plt.show()