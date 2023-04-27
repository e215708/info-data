import numpy as np
true_function = np.array([[4,7], [8,10], [13,11], [17,14]])
x = true_function[:,0]
y = true_function[:,0]
estimated = np.sin(np.pi * x * 0.8) * 10