from generator import Generator
from screen import Screen
import sys
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

class Controller :
    def __init__(self, model : Generator, view : Screen) -> None:
        self.model = model
        self.view = view
        self.gui()
        self.actions_binding()
    
    def gui(self) :
        print("Generator.gui()")
        self.frame=tk.LabelFrame(self.view.parent,text="X")
        self.var_mag=tk.IntVar()
        self.var_mag.set(1)
        self.scaleA=tk.Scale(self.frame,variable=self.var_mag,
                             label="Amplitude",
                             orient="horizontal",length=250,
                             from_=0,to=5,tickinterval=1)

    def layout(self) :
        print("Generator.layout()")
        # self.screen.pack(fill="x")
        # self.screen.pack(fill="both",padx=10,pady=20)
        self.frame.pack()
        self.scaleA.pack()



    def configure(self):
        self.model.attach(self.view)
        self.view.create_grid(8)
        self.view.layout()
        self.layout()
        self.model.generate()

    def actions_binding(self) :
        print("Generator.actions_binding()")
        self.view.screen.bind("<Configure>",self.resize)
        self.scaleA.bind("<B1-Motion>",self.on_magnitude_action)

    # callbacks (on_<name>_action(...) )
    def on_magnitude_action(self, event):
        print("Generator.on_magnitude_action()")
        if  self.model.m != self.var_mag.get() :
            self.model.m=self.var_mag.get()
            self.model.generate()
    
    def resize(self,event):
        print("Generator.resize()")
        self.view.width,self.view.height=event.width,event.height
        print("width,height",self.view.width,self.view.height)
        # TO DO  :
        # Delete existing grid and signal plot
        self.view.screen.delete("grid")
        self.view.screen.delete(self.model.get_name())
        # Create a grid with new dimensions
        self.view.tiles = self.view.width // 100  # 100-pixel grid size
        self.view.create_grid(self.view.tiles)
        # Plot signal with new dimensions
        self.model.generate()