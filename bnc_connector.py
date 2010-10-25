"""
Makes PCB Mount BNC connector. 

"""
import sys
import scipy
from py2scad import *

# Units below are in mm
INCH2MM = 25.4
INCH2CM = 2.54

"""
Measured part sizes - oversized to fit

"""
base_x = 14
base_y = 13.71
base_z = 15.2

thread_height = 9.2
thread_radius = 6.7 # oversized radius by 0.5mm to make hole 1mm larger

conn_height = 12.05
conn_radius = 4.82

notch_height = 2.3
notch_width = 8   # oversized width by 1mm 
notch_length = 9.6

def get_bnc_connector():

    base = Cube(size=[base_x,base_y,base_z])
    base = Color(base,rgba=[0.5,0.5,0.8,1])
    thread = Cylinder(h=thread_height,r1=thread_radius,r2=thread_radius)
    thread =  Rotate(thread, a = 90, v=[1,0,0])
    thread = Translate(thread, v=[0,-(0.5*base_y + 0.5*thread_height),0])
    end = Cylinder(h=conn_height,r1=conn_radius,r2=conn_radius)
    end =  Rotate(end, a = 90, v=[1,0,0])
    end = Translate(end, v=[0,-(0.5*base_y + 1*thread_height + 0.5*conn_height),0])

    Notch = Cube(size=[notch_width, notch_length, notch_height]) 
    Notch = Translate(Notch, v=[0,-(0.5*base_y + 0.5*thread_height),0.5*base_z - 0.5*2.3])
    thread = Difference([thread,Notch])

    part = Union([base,thread,end]);
    return part


# -----------------------------------------------------------------------------
if __name__ == "__main__":

    part = get_bnc_connector()
    prog = SCAD_Prog()
    prog.fn=50
    prog.add(part)
    prog.write('bnc_connector.scad')     

