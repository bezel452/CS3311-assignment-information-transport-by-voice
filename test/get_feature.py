import wave
import numpy as np
import matplotlib.pyplot as plt

## 获取相关频谱、时谱图像，与仅用作调试

def read_wav(path):
    file = wave.open(path, "rb")
    params = file.getparams()
    print(params)
    framesra, frameswav = params[2], params[3]
    datawav = file.readframes(frameswav)
    file.close()
    datause = np.fromstring(datawav, dtype=np.short)
    print(datause)
    # print(datause)
    time = np.arange(0, frameswav) * (1.0 / framesra)
    return datause, time, framesra

data, time, sr = read_wav('test_noise.wav')


# print(data)
data_fft = np.fft.fft(data)
data_fft = np.fft.fftshift(data_fft)

# data_fft = np.fft.fftshift(data_fft)

# for cur in range(0, int(data_fft / 2)):

data_ffta = abs(data_fft)

freq = np.linspace(-1 * sr / 2, sr / 2, len(data_ffta))
# print(freq)
plt.title("test")
plt.subplot(211)
plt.plot(freq, data_ffta)
'''
data_ifft = np.fft.ifft(data_fft)
plt.title("test")
plt.subplot(211)
plt.plot(time, data_ifft)
'''
# plt.subplot(212)

# print(data_ifft)
# plt.plot(time, data)

plt.show()
