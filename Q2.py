import numpy as np
import matplotlib.pyplot as plt

omega0 = 5e15 # Random omega0 value 
def OpticalDepth(omega_Array, tau_value):
    n = 50e-6 # Given
    return n * 6.652e-29 * (np.power(omega_Array, 4) / (np.power(np.power(omega_Array, 2)-np.power(omega0, 2), 2)+ np.power(np.power(omega0, 3) * tau_value, 2)))
omega_Array = np.linspace(omega0 / 10000, 100 * omega0, 100000)
optical_Depth = OpticalDepth(omega_Array, 1 / (100 * omega0))
plt.plot(omega_Array, optical_Depth, color = 'green')
plt.xlabel('Omega')
plt.ylabel('Optical Depth')
plt.title('Optical Depth vs Omega')
plt.grid(True)
plt.show()