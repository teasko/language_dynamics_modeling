import numpy as np
import sys

class Abs:
    def __int__(self, NH, NL, NB):
        self.NH = NH
        self.NL = NL
        self.NB = NB
          
        
class Rel:
    def __int__(self, xH, xL, xB):
        if ((xH+xL+xB) < (1+0.000000001)) and ((xH+xL+xB)> (1 - 0.000000001)): 
            self.xH = xH
            self.xL = xL
            self.xB = xB
        else:
            raise ValueError('xH+xL+xH not equal to 1')

            
            
    def __int__(self):
        self.xH = []
        self.xL = []
        self.xB = []
class Years:
    def __int__(self, years):
        self.years = years
        
class Data:
    def __init__(self):
        self.Abs = Abs()
        self.Rel = Rel()
        self.Years = Years()
        
    def print_data(self):
        print(f"xH =")
        print(self.Rel.xH)
        print(f"xL =")
        print(self.Rel.xL)
        print(f"xB =")
        print(self.Rel.xB)
        print("years")
        print(self.Years)