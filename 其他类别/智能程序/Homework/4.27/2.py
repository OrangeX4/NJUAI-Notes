# %%
import numpy as np

m = np.random.rand(10, 10)

# %%
m[:, :5] = m[:, :5] * (-1)

print(m)