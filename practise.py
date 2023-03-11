import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

fs =8000
N =50
fc =1200
b = sig.firwin(N+1,fc, fs=fs,window='hamming',pass_zero='highpass')
w,h_freq=sig.freqz(b,fs=fs)
z,p,k = sig.tf2zpk(b,1)

plt.subplot(3,1,1)
plt.show()