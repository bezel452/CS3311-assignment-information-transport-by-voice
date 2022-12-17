import wave

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from matplotlib.mlab import window_none
import librosa
import scipy.io

## 配套使用，将图片变为音频

def img2wav(img_path, wav_path, fft_size = 1024):
    img = Image.open(img_path).convert('L')

    img = img.resize((img.width * fft_size // 2 // img.height, fft_size // 2), Image.BICUBIC)
    img = np.array(img, 'float')
    img = img * (100 / 255) - 100
    img = np.exp(img * (np.log(10) / 20))
    img = img[::-1].T
    max_sum = max(col.sum() for col in img)
    if max_sum > 1:
        img /= max_sum

    with wave.open(wav_path, 'wb') as f:
        f.setparams((1, 2, 15000, len(img) * fft_size, 'NONE', ''))
        for col in img:
            data = np.fft.ifft(col * fft_size, fft_size).real * 32767
            for index in np.where(data < -32768):
                data[index] = -32768
            for index in np.where(data > 32767):
                data[index] = 32768

            data = data.astype('short')
            f.writeframesraw(data)
'''
def change_freq(wav_path, output_path, size):
    input, sr = librosa.load(wav_path)
    data = librosa.effects.pitch_shift(input, sr, n_steps=size)
    data = data * 32767
    for index in np.where(data < -32768):
        data[index] = -32768
    for index in np.where(data > 32767):
        data[index] = 32768
    data = data.astype('short')
    scipy.io.wavfile.write(output_path, sr, data)
'''
def draw_figure(wav_path, output_path, fft_size=1024):
    with wave.open(wav_path, 'rb') as f:
        n_samples = f.getnframes()
        data = f.readframes(n_samples)
        n_channels = f.getnchannels()
        sample_rate = f.getframerate()

    data = np.fromstring(data, 'short')
    data.shape = (n_samples, n_channels)
    data = data.T[0]

    plt.specgram(data / 32767, fft_size, sample_rate, window=window_none, noverlap=0, scale='dB')
    plt.axis('off')
    plt.savefig(output_path, dpi = 300)
    img = Image.open(output_path).convert('L')
    img.save(output_path)
    plt.show()

if __name__ == '__main__':
    # img2wav("test_img.png", "test_img_new.wav")
    # change_freq("test_img3.wav", "test_img3_1.wav", -5)
    draw_figure("test_redu.wav", "11.png")
