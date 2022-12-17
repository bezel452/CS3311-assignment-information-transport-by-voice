import wave 
import numpy as np

## 混入噪音，用作测试

def generate_wav(in_path, noise_path, out_path):
    with wave.open(in_path, 'rb') as f:
        n_samples1 = f.getnframes()
        data1 = f.readframes(n_samples1)
        param = f.getparams()
    #   print(param[3])
        data1 = np.fromstring(data1, 'short')
        datadiv = data1 // 2
        data1 = data1 - datadiv

    with wave.open(noise_path, 'rb') as f:
        n_samples2 = f.getnframes()
        data2 = f.readframes(n_samples2)
        data2 = np.fromstring(data2, 'short')
        data2 = data2 // 2
    
    div = len(data1) - len(data2)
    div = abs(div)
    if len(data1) > len(data2):
        data2 = np.pad(data2, (0, div))
    else:
        data1 = np.pad(data1, (0, div))
    
    with wave.open(out_path, 'wb') as f:
        f.setparams(param)
        data = data1 + data2
    #    print(max(data))
        f.writeframesraw(data)
    
if __name__ == '__main__':
    generate_wav("test2.wav", "noise.wav", "test_mul1.wav")

