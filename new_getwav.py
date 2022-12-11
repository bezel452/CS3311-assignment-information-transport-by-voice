import pyaudio
import math
import struct
import wave
import sys

Threshold = 40

SHORT_NORMALIZE = (1.0 / 32768.0)

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 15000
swidth = 2
MAX_Second = 22

TimeoutSignal = ((RATE / CHUNK * MAX_Second) + 2)
silence = True
filename = 'test_getnew.wav'
Time = 0
all = []

def GetStream(chunk):
    return stream.read(chunk)

def rms(frame):
    count = len(frame) / swidth
    format = "%dh"%(count)
    shorts = struct.unpack(format, frame)

    sum_squares = 0.0
    for sample in shorts:
        n = sample * SHORT_NORMALIZE
        sum_squares += n * n
    rms = math.pow(sum_squares / count, 0.5)
    return rms * 1000

def WriteSpeech(WriteData):
#    stream.stop_stream()
#    stream.close()
#    p.terminate()
    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(WriteData)
    wf.close()

def KeepRecord(TimeoutSignal, LastBlock):
    all.append(LastBlock)
    TimeoutSignal = int(TimeoutSignal)
    for i in range(0, TimeoutSignal):
        try:
            data = GetStream(CHUNK)
        except:
            continue
        all.append(data)
    print("END RECORD AFTER TIMEOUT")
    data = b''.join(all)
    print("WRITE TO FILE")
    WriteSpeech(data)
    print("CONTINUE WAITING")

def listen(silence, Time):
    print("WAITING FOR SPEECH")
    while silence:
        
        try:
            input = GetStream(CHUNK)
        except:
            continue
           
     #   input = GetStream(CHUNK)
        rms_value = rms(input)
    #     print(rms_value)
        if rms_value > Threshold:
            silence = False
            LastBlock = input
            print("RECORDING....")
            KeepRecord(TimeoutSignal, LastBlock)
            Time = 0
            silence = True
        else:
            Time = Time + 1
        if Time > TimeoutSignal:
            print("TIMEOUT")
            stream.stop_stream()
            stream.close()
            p.terminate()
            sys.exit()

p = pyaudio.PyAudio()
stream = p.open(format = FORMAT, 
        channels= CHANNELS,
        rate = RATE,
        input = True,
        output = True,
        frames_per_buffer = CHUNK)

listen(silence, Time)