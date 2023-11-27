from cmath import sin
from logging import makeLogRecord
from math import exp
from msilib.schema import File
from pydoc import safeimport
from select import EPOLLEXCLUSIVE
from webbrowser import MacOSX


def wave_function(x, t):
    return sin(x - t)
def particle_function(x, t):
    return exp(-(x,-t) ** 2)
def new_func(wave_function, t, x):
    safeimport(wave_function(x,t))

for t in range (0, 100):
    for x in range(0, 100):
        if t % 2 == 0:
        new_func(wave_function, t, x)
        makeLogRecord 
    else:
        print(particle_function(x,t))
    
