import numpy as np
from scipy.special import gamma
import matplotlib.pyplot as plt

e = 1.602e-19
C = 1
c = 3 * 10 ** 8
m_e = 9.109e-31

def optical_depth(B, p, omega_Array, l):
    nu_Array = omega_Array / (2 * np.pi)
    return (np.sqrt(3) * e ** 3) / (8 * np.pi * m_e) * pow((3 * e) / (2 * np.pi * m_e ** 3 * c ** 5), (p / 2)) * C * pow((B), ((p + 2) / 2)) * gamma((3 * p + 2) / 12) * gamma((3 * p + 22) / 12) * np.power(nu_Array, (-(p + 4) / 2)) * l
p_values = [2.5, 4]
L_values = [10 ** 2, 10 ** 10]
omega_Array1 = np.linspace(10e6, 10e9, 10000)
omega_Array2 = np.linspace(10e9, 1e12, 10000)
total_omega_Array = omega_Array1 + omega_Array2

for l in L_values:
    for part in ['i', 'ii', 'iii']:
        if part == 'i':
            B = 1e-9
        if part == 'ii':
            B = 1e-9
        elif part == 'iii':
            B = 1e2
        tau1 = optical_depth(B, 2.5, omega_Array1, l)
        tau2 = optical_depth(B, 4, omega_Array2, l)
        total_tau = tau1 + tau2
        plt.plot(total_omega_Array, total_tau, label=f"Q5 Part {part}")
        plt.xlabel('Frequency in Hz')
        plt.ylabel('Total Power in W')
        plt.title(f'Total Power Emitted vs. Angular Frequency [l = {l} Km - Part {part})]')
        plt.legend()
        plt.grid(True)
        plt.yscale('log')
        plt.xscale('log')
        plt.show()