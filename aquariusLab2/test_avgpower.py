import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import ugradio
from lab2 import make_complex, avg_power

data = 0.1*np.genfromtxt('1420_990Blocks.txt')/(2.**15)
comp = make_complex(data, 990)

avg_power(comp, 1, 2**13)
plt.savefig('poweravg')
