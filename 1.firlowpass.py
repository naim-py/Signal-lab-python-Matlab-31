import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

fs = 8000  # sampling frequency rate
N = 50  # order of filer
fc = 1200  # cutoff frequency
# wc = 2 * fc / fs  # normalized cutoff frequency to the nyquist frequency
b = sig.firwin(N + 1, fc, fs=fs, window='hamming', pass_zero='lowpass')
w, h_freq = sig.freqz(b, fs=fs)   #compute the frequency response of the filter
z, p, k = sig.tf2zpk(b, 1)      # convert the transfer function of the filter to its zeros, poles, and gain.

plt.subplot(3, 1, 1)
plt.plot(w, np.abs(h_freq))  # magnitude
plt.xlabel('frequency(Hz)')
plt.ylabel('Magnitude')

plt.subplot(3, 1, 2)
plt.plot(w, np.unwrap(np.angle(h_freq)))  # phase
plt.xlabel('frequency(Hz)')
plt.ylabel('Phase(angel)')

plt.subplot(3, 1, 3)
plt.scatter(np.real(z), np.imag(z), marker='o', edgecolors='b')
plt.scatter(np.real(p), np.imag(p), marker='x', color='b')
plt.show()

''''
The hamming wondow generates less ripple in the side lobes thatn the hanning window .
there is comparatively reduction in side lobe hence spectral leakage in Hamming window is
better than hanning window
It is a circuit which allows the frequencies above cut off frequency to pass through it
It consists of Capacitor followed by a resistor.
Operating Frequency	Higher than the cut off frequency.
used In audio amplifiers, low noise amplifiers etc.

'''