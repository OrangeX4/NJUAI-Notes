from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
import numpy as np

X, y = load_boston(return_X_y=True)
trainx, testx, trainy, testy = train_test_split(
    X, y, test_size=0.33, random_state=42)


def linReg(X_train: np.ndarray, y_train: np.ndarray) -> np.ndarray:
    # linear regression
    pass


def linRegMSE(X_train: np.ndarray, y_train: np.ndarray, X_test: np.ndarray, y_test: np.ndarray) -> float:
    pass


def reportLinRegMSE(): return linRegMSE(trainx, trainy, testx, testy)

# ridge regression


def ridgeReg(X_train: np.ndarray, y_train: np.ndarray, lmbd: float) -> np.ndarray:
    pass


def ridgeRegMSE(X_train: np.ndarray, y_train: np.ndarray, X_test: np.ndarray, y_test: np.ndarray, lmbd: float) -> float:
    pass


def reportRidgeRegMSE(lmbd): return ridgeRegMSE(
    trainx, trainy, testx, testy, lmbd)
