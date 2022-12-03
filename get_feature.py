import wave
import numpy as np
import matplotlib.pyplot as plt

def read_wav(path):
    file = wave.open(path, "rb")
    params = file.getparams()
    framesra, frameswav = params[2], params[3]
    datawav = file.readframes(frameswav)
    file.close()
    datause = np.fromstring(datawav, dtype=np.short)
    print(datause)
    # print(datause)
    time = np.arange(0, frameswav) * (1.0 / framesra)
    return datause, time, framesra

data, time, sr = read_wav('test1.wav')

# print(data)
data_fft = np.fft.fft(data)
# data_fft = np.fft.fftshift(data_fft)

freq = np.linspace(0, sr, len(data_fft))

plt.title("test")
plt.subplot(211)
plt.plot(freq, data_fft)

plt.subplot(212)
data_ifft = np.fft.ifft(data_fft)
# print(data_ifft)
plt.plot(time, data)

plt.show()
