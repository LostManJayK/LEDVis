from rpi_ws281x import Adafruit_NeoPixel, Color
import time

class LEDSegment:

    colours = {
    "red": (255, 0, 0),    # Red
    "orange": (255, 165, 0),  # Orange
    "yellow": (255, 255, 0),  # Yellow
    "green": (0, 255, 0),    # Green
    "blue": (0, 0, 255),    # Blue
    "purple": (148, 0, 211)   # Violet
    }

    def __init__(self, colour="red", pixel_range=(0, 144), pos=0):
        self.colour = colour
        self.is_on = False
        self.pixel_range = pixel_range

    def illuminate(self, strip, turn_off=False):
        
        if not turn_off:
            for i in range(*self.pixel_range):
                strip.setPixelColor(i, Color(*LEDSegment.colours[self.colour]))
                strip.show()
        else:
            for i in range(*self.pixel_range):
                strip.setPixelColor(i, Color(0, 0, 0))
                strip.show()





class StripManager:

    def __init__(self):

        LED_COUNT = 144  # Number of LED pixels.
        LED_PIN = 18  # GPIO pin connected to the pixels (18 uses PWM).
        LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
        LED_DMA = 10  # DMA channel to use for generating signal (try 10)
        LED_BRIGHTNESS = 180  # Set to 0 for darkest and 255 for brightest
        LED_INVERT = False
        
        self.LED_segments = [] #To be filled with custom objects made for LED segments
        i = 0
        segment_count = LED_COUNT//6
        for c in LEDSegment.colours:
            self.LED_segments.append(LEDSegment(c, (i, i+segment_count-1), i//segment_count))
            i += segment_count

        self.strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
        self.strip.begin()
    
    #Illuminate the desired segment with its colour
    def writeSegment(self, segment):
        
        segment.illuminate(self.strip)
        
    def turnOffSegment(self, segment):
        
        segment.illuminate(self.strip, True)



if __name__ == "__main__":
    
    sm = StripManager()
    sm.writeSegment(sm.LED_segments[0])
    time.sleep(1)
    sm.turnOffSegment(sm.LED_segments[0])
	

    
