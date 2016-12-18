import numpy as np
import matplotlib.pyplot as plt

x = range(1000)
y = np.random.normal(0, 1, 1000)

plt.plot(x, y, 'o')
