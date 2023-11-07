# coding: utf-8
import sys
import math

from observer import Subject
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

class Generator(Subject):
    def __init__(self,bg="white",width=600,height=300):
        Subject.__init__(self=self)
        self.bg=bg
        self.width,self.height=width,height
        self.name="X"
        self.signal=[]
        self.m,self.f,self.p=1.0,2.0,0.0
        self.harmonics=1
        self.samples=100
        self.units=1
    # properties getter/setter
    def get_name(self) :
        return self.name
    def set_name(self,name) :
        self.name=name
    def get_signal(self) :
        return self.signal
    def set_signal(self,signal) :
        self.signal=signal
    def get_magnitude(self) :
        return self.m
    def set_magnitude(self,magnitude) :
        self.m = magnitude
    def get_frequence(self):
        return self.f
    def set_frequence(self, frequence):
        self.f = frequence
    def get_phase(self):
        return self.p
    def set_phase(self, phase):
        self.p = phase
    def get_harmonique(self): 
        return self.harmonics
    def set_harmonique(self, harmoniques) : 
        self.harmonics = harmoniques
    def vibration(self,t, odd=None):
        # Warning : take care of degrees_to_radians conversion on phase (self.p)
        # if you get degree from your slider, use radians() function from math module to convert
        m,f,p=self.m,self.f,self.p
        harmo=int(self.harmonics)
        sum=0
        if odd is None:
            for h in range(1,harmo+1) :
                print("printing all harmonics..")
                sum=sum + (m/h)*sin(2*pi*(f*h)*t)-p
        if odd is True:
            print("printing odd harmonics..")
            for h in range(1,harmo+1, 2) :
                sum=sum + (m/h)*sin(2*pi*(f*h)*t)-p
        if odd is False:
            print("printing even harmonics..")
            for h in range(2,harmo+1, 2) :
                sum=sum + (m/h)*sin(2*pi*(f*h)*t)-p

        return sum
    def generate(self, harm_odd = None):
        print("Generator observers", self.observers)
        print("Generator.generate()")
        del self.signal[0:]
        samples=int(self.samples)
        for t in range(samples+1) :
            self.signal.append([t/samples,self.vibration(t/samples, odd=harm_odd)])
        self.notify()
        return self.signal
    

if   __name__ == "__main__" :
    mw=Generator()
    signal = mw.generate()
    print(signal)

