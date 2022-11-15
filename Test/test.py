import scipy

# get min of f(K, z) = (K + 3) / (2 * sqrt(K * z + 2)), K > 0 and z > 2
f = lambda x: (x[0] + 3) / (2 * scipy.sqrt(x[0] * x[1] + 2))
res = scipy.optimize.minimize(f, [1, 3], bounds=[(0, 50), (2, 50)])
print(res)