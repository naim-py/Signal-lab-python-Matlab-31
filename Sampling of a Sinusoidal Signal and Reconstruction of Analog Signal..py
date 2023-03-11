import numpy as np
import matplotlib.pyplot as plt

# Define the continuous-time sinusoidal signal
f = 10   # frequency (Hz)
T = 1/f  # period (s)
t = np.linspace(0, 3*T, 1000, endpoint=False)
x_cts = np.sin(2*np.pi*f*t)

# Sample the signal at a certain rate
Fs = 50  # sampling frequency (Hz)
Ts = 1/Fs  # sampling interval (s)
n = np.arange(0, len(t))
x_samp = np.sin(2*np.pi*f*n*Ts)

# Reconstruct the analog signal using linear interpolation
t_interp = np.linspace(0, 3*T, 150)
x_interp = np.interp(t_interp, n*Ts, x_samp)

# Plot the results
plt.figure(figsize=(8,6))

# Continuous-time signal
plt.subplot(3,1,1)
plt.plot(t, x_cts)
plt.title('Continuous-Time Sinusoidal Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

# Sampled signal
plt.subplot(3,1,2)
plt.stem(n*Ts, x_samp, use_line_collection=True)
plt.title('Sampled Sinusoidal Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

# Reconstructed signal
plt.subplot(3,1,3)
plt.plot(t_interp, x_interp)
plt.title('Reconstructed Sinusoidal Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()