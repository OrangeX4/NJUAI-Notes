import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA 

# 1. Loading dataset into Pandas DataFrame and get numpy data
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
df = pd.read_csv(url, names=['sepal length','sepal width','petal length','petal width','target'])
data = df.iloc[:, :4].to_numpy()
# data = np.array([[-1., -1., -1.], [-2., -1., 5.], [-3., -2., 3.], [1., 1., 2.], [2., 1., 4.], [3., 2., 3.]])

def pca(data, n_component):
    data = data.T

    # 2. Subtract the mean
    data -= data.mean(axis = 1).reshape(-1, 1)
 
    # 3. Get the covariance matrix: 1/m * XX^T
    cov_matrix = 1 / len(data[0]) * data @ data.T
 
    # 4. Calculate the eigenvalue and eigenvector
    eigenvalues, eigenmatrix = np.linalg.eig(cov_matrix)

    # 5. Get data after dimensionality reduction and Sort eigenmatrix by eigenvalues
    new_data = eigenmatrix.T @ data

    # 6. Sort data
    return new_data[sorted(range(len(eigenvalues)),  key=lambda v: -eigenvalues[v])][:n_component]

new_data = pca(data, 2)

print(new_data.T)

pca=PCA(n_components=2)
new_data = pca.fit_transform(data)

print(new_data)
