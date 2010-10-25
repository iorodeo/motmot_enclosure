"""
Test using bnc connnector module from another program
"""
from py2scad import *
import bnc_connector
import bnc_group
base_x = bnc_connector.base_x
base_z = bnc_connector.base_z
edge_gap = 5.5
conn_gap = 11
bnc_conn = bnc_connector.get_bnc_connector()
bnc_group = bnc_group.get_bnc_group()

# Units below are in mm
INCH2MM = 25.4
INCH2CM = 2.54

"""""""""""""""""""""""""""""""""
PCB measured parameters
"""""""""""""""""""""""""""""""""

x_side = 4*INCH2MM
y_side = 31.8
thickness = 1.75
standoff_height = 12.67
standoff_radius = 3.23
standoff_screw_radius = 1.39



def get_bnc_module():

    PCB = Cube(size=[x_side,y_side,thickness])
    PCB = Color(PCB,rgba=[0,0.5,0,1.00])
#    standoff = Cylinder(h=standoff_height ,r1=standoff_radius,r2=standoff_radius)
    standoff = Cylinder(h=standoff_height + 2.5*thickness,r1=standoff_screw_radius,r2=standoff_screw_radius) # Use this version for differencing from floor for holes
    standoff1 = Translate(standoff, v=[25,0.5*y_side - standoff_radius, - 0.5*standoff_height])
    standoff2 = Translate(standoff, v=[-25,0.5*y_side - standoff_radius, - 0.5*standoff_height])
    standoff3 = Translate(standoff, v=[25,-(0.5*y_side - standoff_radius),- 0.5*standoff_height])
    standoff4 = Translate(standoff, v=[-25,-(0.5*y_side - standoff_radius),- 0.5*standoff_height])
    bnc = Translate(bnc_group, v=[0, 0, 0])
    part = Union([PCB,standoff1,standoff2, standoff3, standoff4, bnc]);
    return part

#------------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":

    part = get_bnc_module()
    prog = SCAD_Prog()
    prog.fn=50
    prog.add(part)
    prog.write('bnc_module.scad')     






