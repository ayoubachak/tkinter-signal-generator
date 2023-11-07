# coding: utf-8
import sys
import math

from observer import Observer
major=sys.version_info.major
minor=sys.version_info.minor
if major==2 and minor==7 :
    import Tkinter as tk
    import tkFileDialog as filedialog
elif major==3 :
    import tkinter as tk
    from tkinter import filedialog
else :
    if __name__ == "__main__" :
        print("Your python version is : ",major,minor)
        print("... I guess it will work !")
    import tkinter as tk
    from tkinter import filedialog 

from math import pi,sin,radians

class Screen(Observer) :
    def __init__(self,parent : tk.Tk ,bg="white",width=600,height=300):
        self.parent=parent
        self.bg=bg
        self.width,self.height=width,height
        self.units=1
        self.tiles = 2
        self.signal = []
        self.gui()

    def gui(self) :
        print("Generator.gui()")
        self.screen=tk.Canvas(self.parent, bg=self.bg,width=self.width,height=self.height)

    def update(self, subject):
        signal = subject.get_signal()
        self.plot_signal(signal)

    def plot_signal(self,signal,  name="X",color="red"):
        print("Generator.plot_signal()")
        if signal and len(signal)>1:
            w,h=self.width,self.height
            if self.screen.find_withtag(name) :
                self.screen.delete(name)         
            plots=[(x*w,(h/self.units)*y+h/2) for (x,y) in signal]
            self.screen.create_line(plots,fill=color,smooth=1,width=3,tags=name)
        return
    
    def create_grid(self,tiles=2):
        print("Generator.create_grid()")
        if self.screen.find_withtag("grid") :
            self.screen.delete("grid")         
        self.units=tiles
        tile_x=self.width/tiles
        for t in range(1,tiles+1):
            x =t*tile_x
            self.screen.create_line(x,0,x,self.height,tags="grid")
            self.screen.create_line(x,self.height/2-10, x,self.height/2+10,width=3,tags="grid")
        tile_y=self.height/tiles
        for t in range(1,tiles+1):
            y =t*tile_y
            self.screen.create_line(0,y,self.width,y,tags="grid")
            self.screen.create_line(self.width/2-10,y,self.width/2+10,y, width=3,tags="grid")


    def layout(self) :
        print("Generator.layout()")
        # self.screen.pack()
        # self.screen.pack(fill="x")
        # self.screen.pack(fill="both",padx=10,pady=20)
        self.screen.pack(expand=True,fill="both",padx=10,pady=20)

if   __name__ == "__main__" :
    root=tk.Tk()
    screen = Screen(root)
    screen.create_grid(8)
    screen.layout()
    root.mainloop()

