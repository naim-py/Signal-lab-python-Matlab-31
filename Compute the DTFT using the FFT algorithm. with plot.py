import numpy as np
import matplotlib.pyplot as plt

def compute_dtft(x):
    N = len(x)
    X = np.fft.fft(x)
    w = np.linspace(0, 2*np.pi, N, endpoint=False)
    X_dtft = X * np.exp(-1j*w*(N-1)/2) / np.sqrt(N)
    return w, X_dtft

# Example signal
x = np.array([1, 2, 3, 4, 3, 2, 1])

# Compute DTFT and plot
w, X_dtft = compute_dtft(x)
plt.plot(w, np.abs(X_dtft))
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('|X(w)|')
plt.title('DTFT Magnitude')
plt.show()


''''
In this program, the compute_dtft function takes a time-domain 
signal x as input and returns the DTFT X_dtft. The function first 
computes the FFT of x using np.fft.fft, and then multiplies it by 
the appropriate complex exponential and normalization factor to 
obtain the DTFT. The frequency range w is also computed using np.linspace.

Finally, the program applies the compute_dtft function to an 
example signal x, and plots the magnitude of the DTFT using plt.plot. 
The resulting plot shows the magnitude spectrum of the DTFT, which is 
a continuous function of frequency.
'''
