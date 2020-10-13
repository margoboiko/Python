import numpy as np

n = int(input('n= ',))
x = np.random.randint(0, 15, size = (n, n))

y = [[x[i].dot(x[:,j]) for j in range(n)] for i in range(n)]
print('X = ', x)
print('Y = ', y)