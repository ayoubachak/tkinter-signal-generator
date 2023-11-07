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
        self.var_mag.set(self.model.get_magnitude())
        self.var_freq = tk.IntVar()
        self.var_freq.set(self.model.get_frequence())
        self.var_phase = tk.IntVar()
        self.var_phase.set(self.model.get_phase())
        self.var_harm = tk.IntVar()
        self.var_harm.set(self.model.get_harmonique())
        self.scaleA=tk.Scale(self.frame,variable=self.var_mag,
                             label="Amplitude",
                             orient="horizontal",length=250,
                             from_=0,to=5,tickinterval=1)
        self.scaleF=tk.Scale(self.frame,variable=self.var_freq,
                             label="Frequence",
                             orient="horizontal",length=250,
                             from_=0,to=20,tickinterval=1)
        self.scaleP=tk.Scale(self.frame,variable=self.var_phase,
                             label="Phase",
                             orient="horizontal",length=250,
                             from_=0,to=5,tickinterval=1)
        self.scaleH=tk.Scale(self.frame,variable=self.var_harm,
                             label="Harmoniques",
                             orient="horizontal",length=250,
                             from_=0,to=20,tickinterval=10)
        self.radio_var = tk.IntVar()
        self.radio_var.set(3)  # default value
        self.radio_frame = tk.Frame(self.frame)
        self.radio1 = tk.Radiobutton(self.radio_frame, text="Odd", variable=self.radio_var, value=1)
        self.radio2 = tk.Radiobutton(self.radio_frame, text="Even", variable=self.radio_var, value=2)
        self.radio3 = tk.Radiobutton(self.radio_frame, text="All", variable=self.radio_var, value=3)

    def get_radio_state_odd(self):
        print("Radion var ", self.radio_var.get())
        if self.radio_var.get() == 1 : print("Radio is Odd");return True
        if self.radio_var.get() == 2 : print("Radio is Even");return False
        if self.radio_var.get() == 3 : print("Radio is All");return None
        

    def layout(self) :
        print("Generator.layout()")
        # self.screen.pack(fill="x")
        # self.screen.pack(fill="both",padx=10,pady=20)
        self.frame.pack()
        self.scaleA.pack()
        self.scaleF.pack()
        self.scaleP.pack()
        self.scaleH.pack()

        # radio
        self.radio_frame.pack()  # Pack the frame that holds the radio buttons
        self.radio1.pack(side=tk.LEFT)
        self.radio2.pack(side=tk.LEFT)
        self.radio3.pack(side=tk.LEFT)



    def configure(self):
        self.model.attach(self.view)
        self.view.create_grid(8)
        self.view.layout()
        self.layout()
        self.model.generate()
    
    def on_radio_action(self):
        print("Selected Option:", self.radio_var.get())
        if  self.model.get_harmonique() != self.var_harm.get() :
            self.model.set_harmonique(self.var_harm.get())
            self.model.generate(harm_odd=self.get_radio_state_odd())

    def actions_binding(self) :
        print("Generator.actions_binding()")
        self.view.screen.bind("<Configure>",self.resize)
        self.scaleA.bind("<B1-Motion>",self.on_magnitude_action)
        self.scaleF.bind("<B1-Motion>",self.on_frequence_action)
        self.scaleP.bind("<B1-Motion>",self.on_phase_action)
        self.scaleH.bind("<B1-Motion>",self.on_harmonique_action)
        self.radio_var.trace("w", lambda *args: self.on_radio_action())


    # callbacks (on_<name>_action(...) )
    def on_magnitude_action(self, event):
        print("Generator.on_magnitude_action()")
        if  self.model.get_magnitude() != self.var_mag.get() :
            self.model.set_magnitude(self.var_mag.get())
            self.model.generate()
    # callbacks (on_<name>_action(...) )
    def on_frequence_action(self, event):
        print("Generator.on_frequence_action()")
        if  self.model.get_frequence() != self.var_freq.get() :
            self.model.set_frequence(self.var_freq.get())
            self.model.generate()
    # callbacks (on_<name>_action(...) )
    def on_phase_action(self, event):
        print("Generator.on_phase_action()")
        if  self.model.get_phase() != self.var_phase.get() :
            self.model.set_phase(self.var_phase.get())
            self.model.generate()
    # callbacks (on_<name>_action(...) )
    def on_harmonique_action(self, event):
        print("Generator.on_harmonique_action()")
        if  self.model.get_harmonique() != self.var_harm.get() :
            self.model.set_harmonique(self.var_harm.get())
            self.model.generate(harm_odd=self.get_radio_state_odd())
    
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