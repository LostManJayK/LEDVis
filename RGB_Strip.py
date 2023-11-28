from rpi_ws281x import Adafruit_NeoPixel, Color

class LEDSegment:

    colours = {
    "red": (255, 0, 0),    # Red
    "orange": (255, 165, 0),  # Orange
    "yellow": (255, 255, 0),  # Yellow
    "green": (0, 255, 0),    # Green
    "blue": (0, 0, 255),    # Blue
    "purple": (148, 0, 211)   # Violet
    }

    def __init__(self, colour="red", pixel_range=(0, 300), pos=0):
        self.colour = colour
        self.is_on = False

    def illuminate(self, strip):

        for i in range(*self.pixel_range):
            strip.setPixelColor(i, Color(*LEDSegment.colours[self.colour]))





class StripManager:

    def __init__(self):

        LED_COUNT = 150  # Number of LED pixels.
        LED_PIN = 18  # GPIO pin connected to the pixels (18 uses PWM).
        LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
        LED_DMA = 10  # DMA channel to use for generating signal (try 10)
        LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
        LED_INVERT = False
        
        self.LED_segments = [] #To be filled with custom objects made for LED segments
        i = 0
        for c in LEDSegment.colours:
            self.LED_segments.append(LEDSegment(c, (i, i+49), i//50))
            i += 50

        self.strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
        self.strip.begin()
    
    #Illuminate the desired segment with its colour
    def writeSegment(self, segment):
        
        segment.illuminate(self.strip)

    