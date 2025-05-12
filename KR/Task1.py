import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt


A = [[2, 1], [-1, 2]]
b = [12, 8]
x= (0, None)
y= (0, None)
lambdas = np.linspace(-10, 10, 200)
z_val = []
x1_val = []
x2_val = []


for lam in lambdas:
    c = [-(5 + lam), -(2 - lam)]
    # розв'язання
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x, y])

    if res.success:
        z = -res.fun
        z_val.append(z)
        x1_val.append(res.x[0])
        x2_val.append(res.x[1])
    else:
        z_val.append(np.nan)
        x1_val.append(np.nan)
        x2_val.append(np.nan)


plt.figure(figsize=(10, 6))
plt.plot(lambdas, z_val, label='Z(λ)')
plt.xlabel('λ')
plt.ylabel('Max Z')
plt.grid(True)
plt.legend()
plt.show()
