import time
from tkinter import *
from tkinter.messagebox import *

class strip_gui:
    def __init__(self):
        self.main_window = Tk()
        self.main_window.geometry("540x380+100+100")
        self.main_window.title("CMPT2200")
        
        self.var1 = DoubleVar()
        self.scale1 = Scale(self.main_window, variable=self.var1, from_=0, to=255)
        self.scale1.place(x=50,y=120)
        
        self.var2 = DoubleVar()
        self.scale2 = Scale(self.main_window, variable=self.var2, from_=0, to=255)
        self.scale2.place(x=130,y=120)
        
        self.var3 = DoubleVar()
        self.scale3 = Scale(self.main_window, variable=self.var3, from_=0, to=255)
        self.scale3.place(x=210,y=120)
        
        self.label1 = Label(self.main_window)
        self.label1.place(x=50,y=220)

        self.label2 = Label(self.main_window, text="Microphone-based LED Controller", font=("Microsoft Sans Serif", 16))
        self.label2.place(x=50,y=30)

        self.colours = ("Colour 1", "Colour 2", "Colour 3", "Colour 4", "Colour 5", "Colour 6", "Colour 7", "Colour 8")
        self.preset_list = Variable(value=self.colours)

        self.listbox1 = Listbox(self.main_window, listvariable=self.preset_list, height=8)
        self.listbox1.place(x=300,y=120)
        
        self.label3 = Label(self.main_window, text="Use the microphone to activate the LEDs. Use these sliders to change the present colours.", font=("Microsoft Sans Serif", 8))
        self.label3.place(x=50,y=80)

        self.button = Button(self.main_window, text="Set Value", command=self.get_value)
        self.button.place(x=100,y=280)
        mainloop()
    def get_value(self):
        #selection = "Value: R" + str(self.var1.get()) + "  G" + str(self.var2.get()) + "  B" + str(self.var3.get())
        #self.label1.config(text=selection)
        selected_colours = [self.var1.get(), self.var2.get(), self.var3.get()]
        selected_preset = self.listbox1.curselection()
        return [selected_preset, selected_colours[0], selected_colours[1], selected_colours[2]]
        

start = strip_gui()