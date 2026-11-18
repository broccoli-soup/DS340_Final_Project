import wfdb

record = wfdb.rdrecord('/Users/shaun/Downloads/PTB_DATASET/records100/21000/21837_lr')
print(record.p_signal)

signal = record.p_signal 
print(signal.shape)

import matplotlib.pyplot as plt

plt.plot(record.p_signal[:1000, 0])


plt.show()

import numpy as np
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt

N = 1000
sample_rate = 1
fft_output = fft(signal)
frequencies = fftfreq(N, 1 / sample_rate)
half_N = N // 2
frequencies_positive = frequencies[:half_N]
amplitudes_positive = 2.0 / N * np.abs(fft_output[:half_N])

plt.plot(frequencies_positive, amplitudes_positive)
plt.title("Bare Bones FFT Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.grid()
plt.show()
