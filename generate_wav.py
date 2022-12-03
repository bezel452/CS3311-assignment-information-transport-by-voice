import wave 
import numpy as np

def generate_wav(in_path, info_path, out_path):
    with wave.open(in_path, 'rb') as f:
        n_samples1 = f.getnframes()
        data1 = f.readframes(n_samples1)
        param = f.getparams()
        data1 = np.fromstring(data1, 'short')
        data1 = data1 // 256
        data1 = data1 * 255

    with wave.open(info_path, 'rb') as f:
        n_samples2 = f.getnframes()
        data2 = f.readframes(n_samples2)
        data2 = np.fromstring(data2, 'short')
        data2 = data2 // 256
    
    div = len(data1) - len(data2)
    
    data2 = np.pad(data2, (0, div))

    with wave.open(out_path, 'wb') as f:
        f.setparams(param)
        data = data1 + data2
        f.writeframesraw(data)
    

generate_wav("test.wav", "test_img3_3.wav", "test_gen1.wav")

