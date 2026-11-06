import wfdb

record = wfdb.rdrecord('/Users/shaun/Downloads/ptb-xl-a-large-publicly-available-electrocardiography-dataset-1.0.3/records100/21000/21837_lr')
print(record.p_signal)

signal = record.p_signal 
print(signal.shape)
import matplotlib.pyplot as plt

plt.plot(record.p_signal[:500, 0])
plt.show()