from Tkinter import *

def frame(root, side):
    w = Frame(root)
    w.pack(side=side, expand=YES, fill=BOTH)
    return w


class Calculator(Frame):
    def __init__(self):
        frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Simple Calculation')
        self.master.iconname("Calcl")

        display = StringVar()
        Entry(self, relief=SUNKEN,
              textvariable=display) .pack(side=Top,  expand=YES,
                                          fill=BOTH)

        for key in  (" 123 " , "456", "789", "-0."):
             keyF = frame (self, Top)
             for char in key:
                 button(keyF, LEFT,char,
                  lambda w=display, s=' %s  '%char: w.set(w.get ()+s))
                 
            
       

            

            
                 Calculator().mainloo()
