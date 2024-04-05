import numpy as np
import matplotlib.pyplot as plt

e = 1.60e-19
c = 3 * 10 ** 8
K_b = 1.38e-23
h = 6.63e-34
m_e = 9.11e-31
# Given
ni = 50e-6
ne = ni
# Choosing random value
Z = 3
G = 1
def alpha(nu, T, ne, ni, Z):
    return (4 * e ** 6 / (3 * m_e * h * c)) * G * ((2 * np.pi) / (3 * K_b * m_e)) ** 0.5 * (1 / (T ** 0.5)) * (Z ** 2 * ne * ni / nu ** 3) * (1-np.exp(-h * nu / (K_b * T)))
nu = np.linspace(10e8, 10e15, 1000)
plt.plot(nu, alpha(nu, 1000, ne, ni, Z) * 10e5, label = 'L = 10^5 m_e, T = 1000K')
plt.plot(nu, alpha(nu, 1000, ne, ni, Z) * 10e13, label = 'L = 10^13 m_e, T = 1000K')
plt.plot(nu, alpha(nu, 100000, ne, ni, Z) * 10e5, label = 'L = 10^5 m_e, T = 100000K')
plt.plot(nu, alpha(nu, 100000, ne, ni, Z) * 10e13, label = 'L = 10^13 m_e, T = 100000K')
plt.xlabel('Frequency in Hz')
plt.ylabel('Optical Depth')
plt.title('Optical Depth - Frequency Plot')
plt.xscale('log')
plt.yscale('log')
#plt.grid(True)
plt.legend()
plt.show()