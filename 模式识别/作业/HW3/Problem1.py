import numpy as np

def cov_eig(X):
    # 1. Subtract the mean
    X_centered = X - X.mean(axis = 0)
 
    # 2. Get the covariance matrix: 1/m * X^TX
    cov_matrix = (1 / X_centered.shape[0]) * (X_centered.T @ X_centered)
 
    # 3. Calculate the eigenvalues and eigenvectors
    eigenvalues, eigenmatrix = np.linalg.eig(cov_matrix)

    # 4. Sort the eigenvalues and eigenvectors
    idx = eigenvalues.argsort()[::-1]
    eigenvalues = eigenvalues[idx]
    eigenmatrix = eigenmatrix[:, idx]

    # 5. Make sure the eigenvectors are pointing in the same direction
    for i in range(eigenmatrix.shape[1]):
        if eigenmatrix[0, i] < 0:
            eigenmatrix[:, i] = -eigenmatrix[:, i]

    return eigenvalues, eigenmatrix

X = np.array([[1, 2, 3], [4, 0, 2], [1, 2, 9], [3, 5, 2]])
X_eigenvalues, X_eigenmatrix = cov_eig(X)

# y_i = x_i - w_1^T (x_i - x_bar) w_1
Y = np.array([X[i] - X_eigenmatrix[:, 0] @ (X[i] - X.mean(axis=0)) * X_eigenmatrix[:, 0] for i in range(X.shape[0])])
Y_eigenvalues, Y_eigenmatrix = cov_eig(Y)

print('second eigenvalue of X:', X_eigenvalues[1])
print('second eigenvector of X:', X_eigenmatrix[:, 1])
print('first eigenvalue of Y:', Y_eigenvalues[0])
print('first eigenvector of Y:', Y_eigenmatrix[:, 0])