import wave 
import numpy as np

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
        div = max(data2)
        data2 = data2 // div * 32767
        data2 = data2 // 256
        data2 = data2 * 255

    data = data1 - data2
    data = data * 256

    with wave.open(output_path, 'wb') as f:
        f.setparams(param)
        f.writeframesraw(data)

return_wav("test_trans1.wav", "test.wav", "test_re1.wav")