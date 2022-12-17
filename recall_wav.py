import wave 
import numpy as np

## 获取原信息音频

def return_wav(input_path, back_path, output_path):
    with wave.open(input_path, 'rb') as f:
        n_samples1 = f.getnframes()
        data1 = f.readframes(n_samples1)
        param = f.getparams()
        data1 = np.fromstring(data1, 'short')

    with wave.open(back_path, 'rb') as f:
        n_samples2 = f.getnframes()
        data2 = f.readframes(n_samples2)
        data2 = np.fromstring(data2, 'short')
    #    data2 = data2 // div * 32767
        datadiv = data2 // 256
        data2 = data2 - datadiv
        
    data = data1 - data2
    data = data * 256

    with wave.open(output_path, 'wb') as f:
        f.setparams(param)
        f.writeframesraw(data)

def return_wav_s(input_path, back_path, output_path):
    with wave.open(input_path, 'rb') as f:
        n_samples1 = f.getnframes()
        data1 = f.readframes(n_samples1)
        param = f.getparams()
        data1 = np.fromstring(data1, 'short')

    with wave.open(back_path, 'rb') as f:
        n_samples2 = f.getnframes()
        data2 = f.readframes(n_samples2)
        data2 = np.fromstring(data2, 'short')
        div = max(data2)
    #    data2 = data2 // div * 32767
        datadiv = data2 // 8
        data2 = data2 - datadiv * 2
    data = data1 - data2
    data = data * 4

    with wave.open(output_path, 'wb') as f:
        f.setparams(param)
        f.writeframesraw(data)

if __name__ == '__main__':
    return_wav_s("mi.wav", "whale.wav", "re.wav")