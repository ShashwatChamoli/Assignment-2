import numpy as np
from scipy.special import gamma
import matplotlib.pyplot as plt

e = 1.602e-19
C = 1
c = 3 * 10 ** 8
m_e = 9.109e-31
def Power(B, p, omega):
    return (np.sqrt(3) * e ** 3 * C * B) / (2 * np.pi * m_e * c ** 2 * (p + 1)) * gamma(p / 4 + 19 / 12) * gamma(p / 4 - 1 / 12) * (np.power(((m_e * c * omega) / (3 * e * B)), ((1 - p) / 2)))
omega_1 = np.linspace(10e7, 1e10, 1000)
omega_2 = np.linspace(1010, 1e12, 1000)

plt.title(f'Power Emitted vs. Angular Frequency in part (i)')
plt.xlabel('Frequency in Hz')
plt.ylabel('Total Power in W')
P_tot_a = Power(1e-9, 2.5, omega_1)
plt.plot(omega_1, P_tot_a, label=f"Q5 (i)")
P_tot_a = Power(1e-9, 4, omega_2)
plt.plot(omega_2, P_tot_a, label=f"Q5 (i)")
plt.legend()
plt.grid(True)
plt.show()

plt.title(f'Power Emitted vs. Angular Frequency in part (ii)')
plt.xlabel('Frequency in Hz')
plt.ylabel('Total Power in W')
P_tot_a = Power(1e-9, 2.5, omega_1)
plt.plot(omega_1, P_tot_a, label=f"Q5 (ii)")
P_tot_a = Power(1e-9, 4, omega_2)
plt.plot(omega_2, P_tot_a, label=f"Q5 (ii)")
plt.legend()
plt.grid(True)
plt.show()

plt.title(f'Power Emitted vs. Angular Frequency in part (iii)')
plt.xlabel('Frequency in Hz')
plt.ylabel('Total Power in W')
P_tot_a = Power(1e2, 2.5, omega_1)
plt.plot(omega_1, P_tot_a, label=f"Q5 (iii)")
P_tot_a = Power(1e2, 4, omega_2)
plt.plot(omega_2, P_tot_a, label=f"Q5 (iii)")
plt.grid(True)
plt.show()