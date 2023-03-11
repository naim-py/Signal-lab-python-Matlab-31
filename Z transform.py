import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Define the coefficients of the discrete-time function
b = [1, 0.5]
a = [1, -0.7, 0.1]

# Compute the Z-transform of the function
z, h = signal.freqz(b, a)

# Plot the magnitude and phase of the Z-transform
fig, (ax1, ax2) = plt.subplots(2, 1)
fig.suptitle('Z-Transform of Discrete-Time Function')
ax1.plot(z, np.abs(h))
ax1.set_ylabel('Magnitude')
ax2.plot(z, np.angle(h))
ax2.set_ylabel('Phase')
ax2.set_xlabel('z')
plt.show()

# Compute the inverse Z-transform of the function
n, x = signal.impz(b, a)

# Plot the impulse response of the function
plt.stem(n, x)
plt.title('Impulse Response of Discrete-Time Function')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.show()

# Plot the pole-zero diagram of the function
zeros, poles, _ = signal.tf2zpk(b, a)
plt.scatter(np.real(zeros), np.imag(zeros), marker='o', color='blue', label='Zeros')
plt.scatter(np.real(poles), np.imag(poles), marker='x', color='red', label='Poles')
plt.legend()
plt.title('Pole-Zero Diagram of Discrete-Time Function')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.show()