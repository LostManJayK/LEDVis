#from scipy.io import wavfile
#from matplotlib import pyplot as mpl
import numpy as np
import pyaudio
import wave

class AudioManager:

    def __init__(self, id=0):

        self.id = id

        #FFT variables
        self.frequencies = None
        self.frequency_ranges = [(50, 220), (221, 550), (551, 1000), (1001, 2000), (2001, 5000), (5001, 25000)] #Define frequency bands
        self.fft_data = None #FFT results
        self.amplitudes = [None for frange in self.frequency_ranges] #Signal strength at each frequency

        #Recording variables
        self.RATE = 44100 #Samples per second
        self.CHANNELS = 1 #Record in mono
        self.FORMAT = pyaudio.paInt16 #Audio format
        self.CHUNK = 1024 #frames per sample
        self.recorder = pyaudio.PyAudio() #PyAudio instance for recording
        self.audio_data = []

    def fftInit(self):
        #rate, data = wavfile.read(f"./audio/snippet{id}.wav")
        #left_audio = data[:, 0]
        #left_audio = data[:]
        self.fft_data = np.abs(np.fft.fft(self.audio_data))
        self.frequencies = np.fft.fftfreq(len(self.audio_data), 1/self.RATE)


    def filterFrequencies(self):
        
        for i in range(0, len(self.frequency_ranges)):
            start, end = self.frequency_ranges[i]
            indices = np.where((self.frequencies >= start) & (self.frequencies <= end))
            self.amplitudes[i] = np.mean(self.fft_data[indices])


    def getAmplitudes(self):
        return self.amplitudes
'''
    def plotFrequencies(self):

        N = len(self.frequencies)

        mpl.figure()
        mpl.plot(self.frequencies[0:N//2], self.fft_data[0:N//2])
        mpl.show()
'''
    def record(self):

        stream = self.recorder.open(format=self.FORMAT,
                        channels=self.CHANNELS,
                        rate=self.RATE,
                        input=True,
                        frames_per_buffer=self.CHUNK)
        print("Recording...")

        seconds = 0.2 #Set recording length

        for i in range(0, int(self.RATE / self.CHUNK * seconds)):
            data = stream.read(self.CHUNK)
            self.audio_data.extend(np.frombuffer(data, dtype=np.int16))
        
        print("End recording...")


    

if __name__ == "__main__":
    a = AudioManager()

    print(a.getAmplitudes())
    a.record()
    a.fftInit()
    a.filterFrequencies()
    a.plotFrequencies()


