from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
import numpy as np

X, y = load_boston(return_X_y = True)
trainx, testx, trainy, testy = train_test_split(X, y, test_size = 0.33, random_state = 42)

# linear regression
def linReg(X_train:np.ndarray, y_train:np.ndarray) -> np.ndarray:
    pass

def linRegMSE(X_train:np.ndarray, y_train:np.ndarray, X_test:np.ndarray, y_test:np.ndarray) -> float:
    pass
reportLinRegMSE= lambda : linRegMSE(trainx,trainy,testx,testy)

# ridge regression
def ridgeReg(X_train:np.ndarray, y_train:np.ndarray, lmbd:float) -> np.ndarray:
    pass
    
def ridgeRegMSE(X_train:np.ndarray, y_train:np.ndarray, X_test:np.ndarray, y_test:np.ndarray, lmbd:float) -> float:
    pass
reportRidgeRegMSE= lambda lmbd : ridgeRegMSE(trainx,trainy,testx,testy,lmbd)