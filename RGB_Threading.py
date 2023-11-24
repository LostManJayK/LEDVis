from threading import Thread
from RGB_Audio import Audiomanager

#Create a custom AudioThread class using the threading.Thread class
class AudioThread(Thread):

    def __init__(self, id):
        
        super().__init__()
        self.id = id
        self.AM = AudioManager()

    def run(self):
        self.analyze()
        
    
    def analyze(self):
        self.AM.record()
        self.AM.fftInit()
        self.AM.filterFrequencies()

#Create a custom VisThread class using the threading.Thread class
class VisThread(Thread):

    def __init__(self):

        super().__init__()

class ThreadManager:

    def __init__(self):
        
        self.num_audio_threads = 0 #Increment on thread creation to use as a thread ID
        self.num_vis_threads = 0
        self.audio_threads = {} #Used to store thread objets. Contents are AudioThread objects and their keys are their thread ID
        self.visualization_threads = {}

    def newAudioThread(self):
        
        self.num_audio_threads += 1
        
        self.audio_threads[self.num_threads] = AudioThread(self.num_threads)

    def newVisThread(self):

        self.num_vis_threads += 1

        self.visualization_threads[self.num_vis_threads] = None #Add visualization thread

    
