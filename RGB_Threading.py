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
        self.SM = StripManager()
        self.amplitudes = amplitudes

    def run(self):

        for i in range(len(self.amplitudes)):
            if self.amplitudes[i] > 15000 + (i==0)*80000 - (i==5)*11000:
                self.SM.writeSegment(self.SM.LED_segments[i])
                self.SM.LED_segments[i].is_on = True 
                print(f"segment {i} illuminated")
            else:
                if self.SM.LED_segments[i].is_on ==True:
                    self.SM.turnOffSegment(self.SM.LED_segments[i])
                    self.SM.LED_segments[i].is_on == False


class ThreadManager:

    def __init__(self):
        
        self.at = None
        self.vt = None
        self.frequency_amplitudes = [] #Will be updated by the frequency amplitudes throughout the program
        self.colour_info = [] #Received from GUI
        self.is_over = False #For ending the program

    def newAudioThread(self):

        self.at = AudioThread()
        self.at.start()   
        self.at.join()
        self.frequency_amplitudes = self.at.AM.amplitudes

        

    def newVisThread(self):

        self.vt = VisThread(self.frequency_amplitudes)
        self.vt.start()
        self.vt.join()

    def runLED(self):
        
        TM = ThreadManager()

        TM.newAudioThread()

        while not self.is_over:

            TM.newVisThread()
            TM.newAudioThread()

    def updateColour(self):

        LEDSegment.colours[self.colour_info[0]] = tuple(self.colour_info[1:3])


    
if __name__ == "__main__":

    TM = ThreadManager()

    TM.newAudioThread()

    for i in range(100):

        TM.newVisThread()
        TM.newAudioThread()


