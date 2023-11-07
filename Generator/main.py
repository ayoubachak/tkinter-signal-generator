# coding: utf-8
import sys
import math
from controller import Controller

from screen import Screen
from generator import Generator
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


if   __name__ == "__main__" :
    root=tk.Tk()
    model=Generator()
    screen = Screen(root)
    controller = Controller(model=model, view=screen)
    controller.configure()
    root.mainloop()




