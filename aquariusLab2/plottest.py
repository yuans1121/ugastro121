import matplotlib
matplotlib.use('Agg')

import numpy as np
import ugradio 
import matplotlib.pyplot as plt
import lab2
from lab2 import make_complex

d1420 = 0.1*np.genfromtxt('1420_990Blocks.txt')/(2.**15)
d1420_comp = make_complex(d1420, 990)

def power(compData, div, N):
    vsamp = 62.5
    time = np.linspace(-N/2./vsamp, (N/2. - 1)/vsamp, N)
    freq = np.linspace(-vsamp/2, (vsamp/2)*(1-2./N), N)
    fft_ = np.fft.fft(compData[:,:N])
    power = abs(fft_)**2
    return freq, power

frequency, power_spec = power(d1420_comp , 1, 2**10)
sum_power = 0
for p in power_spec:
    sum_power += p
plt.plot(np.fft.fftshift(np.fft.fftfreq(2**10)), np.fft.fftshift(sum_power)/len(d1420_comp), label = 'average')
plt.show(block = True)
plt.savefig('test_power')
#plt.xlim(-.2,.2)
