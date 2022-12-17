import wave 
import numpy as np

# 混合背景音与信息音

def generate_wav(in_path, info_path, out_path):
    with wave.open(in_path, 'rb') as f:
        n_samples1 = f.getnframes()
        data1 = f.readframes(n_samples1)
        param = f.getparams()
    #   print(param[3])
        data1 = np.fromstring(data1, 'short')
        datadiv = data1 // 256
        data1 = data1 - datadiv

    with wave.open(info_path, 'rb') as f:
        n_samples2 = f.getnframes()
        data2 = f.readframes(n_samples2)
        data2 = np.fromstring(data2, 'short')
        data2 = data2 // 256
    
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
    
def generate_wav_s(in_path, info_path, out_path):
    with wave.open(in_path, 'rb') as f:
        n_samples1 = f.getnframes()
        data1 = f.readframes(n_samples1)
        param = f.getparams()
    #   print(param[3])
        data1 = np.fromstring(data1, 'short')
        datadiv = data1 // 4
        data1 = data1 - datadiv

    with wave.open(info_path, 'rb') as f:
        n_samples2 = f.getnframes()
        data2 = f.readframes(n_samples2)
        data2 = np.fromstring(data2, 'short')
        data2 = data2 // 4
    
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
    generate_wav("whale.wav", "test_img_new.wav", "test2.wav")

