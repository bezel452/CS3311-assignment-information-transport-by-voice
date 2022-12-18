import wave
import pyaudio

## 播放音频

def do_work(file_path):
    CHUNK = 1024

    f = wave.open(file_path, 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                    channels = f.getnchannels(),
                    rate= f.getframerate(),
                    output=True)
    data = f.readframes(CHUNK)
    while len(data) > 0:
        stream.write(data)
        data = f.readframes(CHUNK)
    stream.stop_stream()
    stream.close()
    f.close()
    p.terminate()

if __name__ == '__main__':
    do_work('test.wav')

