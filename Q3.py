import numpy as np
import matplotlib.pyplot as plt

e = 1.60e-19
c = 3 * 10 ** 8
K_b = 1.38e-23
h = 6.63e-34
m_e = 9.11e-31
# given
ne = 1e5
ni = 1e5
# Choosing random value
Z = 3
g = 2
def P(T, nu, ne, ni, Z, g):
    return 32 * np.pi * e ** 6 * g / (3 * (2 * m_e) * c ** 3) * np.sqrt(2 * np.pi / (3 * K_b * (2 * m_e))) * np.exp(-h * nu / (K_b * T)) * 1 / np.sqrt(T) * Z ** 2 * ne * ni
nu = np.linspace(10 ** 8, 10 ** 19, 1000)
nu = np.array(nu)
plt.plot(nu / 1e6, P(1000, nu, ne, ni, Z, g), 'o-')
plt.xlabel('Frequency in MHz')
plt.ylabel('Power in W / m_e^3 / Hz')
plt.title('Bremsstrahhlung Power Spectrum for 1000 K')
plt.grid(True)
plt.show()

plt.plot(nu / 1e6, P(100000, nu, ne, ni, Z, g), 'o-')
plt.xlabel('Frequency in MHz')
plt.ylabel('Power in W / m_e^3 / Hz')
plt.title('Bremsstrahhlung Power Spectrum for 100000 K')
plt.grid(True)
plt.show()