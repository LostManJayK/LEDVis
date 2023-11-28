from threading import Thread
from RGB_Audio import AudioManager
from RGB_Strip import StripManager

#Create a custom AudioThread class using the threading.Thread class
class AudioThread(Thread):

    def __init__(self):
        
        super().__init__()
        self.AM = AudioManager()

    def run(self):
        self.analyze()
        
    
    def analyze(self):
        self.AM.record()
        self.AM.fftInit()
        self.AM.filterFrequencies()

#Create a custom VisThread class using the threading.Thread class
class VisThread(Thread):

    def __init__(self, amplitudes):

        super().__init__()
        #self.SM = StripManager()
        self.amplitudes = amplitudes

    def run(self):

        for i in range(len(self.amplitudes)):

            if self.amplitudes[i] > 100000:
                #self.SM.writeSegment(self.SM.LED_segments[i])
                print(f"segment {i} illuminated")


class ThreadManager:

    def __init__(self):
        
        self.at = None
        self.vt = None
        self.frequency_amplitudes = [] #Will be updated by the frequency amplitudes throughout the program

    def newAudioThread(self):

        self.at = AudioThread()
        self.at.start()   
        self.at.join()
        self.frequency_amplitudes = self.at.AM.amplitudes 

        

    def newVisThread(self):

        self.vt = VisThread(self.frequency_amplitudes)
        self.vt.start()



    
if __name__ == "__main__":

    TM = ThreadManager()

    TM.newAudioThread()

    for i in range(60):

        TM.newVisThread()
        TM.newAudioThread()


