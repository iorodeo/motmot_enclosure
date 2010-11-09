"""
Makes the camera trigger board
"""
from py2scad import *
import bnc_connector

# Units below are in mm
INCH2MM = 25.4
INCH2CM = 2.54


base_x = bnc_connector.base_x
base_y = bnc_connector.base_y
base_z = bnc_connector.base_z
edge_gap = 5.5
conn_gap = 11
bnc_conn = bnc_connector.get_bnc_connector()

"""""""""""""""""""""""""""""""""
PCB measured parameters
"""""""""""""""""""""""""""""""""

x_side = 57.2
y_side = 76.25
thickness = 1.70
x_atmel = 18
y_atmel = 51
thickness_atmel =1.5
x_USB = 8.6*1.05
y_USB = 8.1
z_USB = 4.8*1.05
standoff_height = 0.375*INCH2MM
standoff_radius = 3.23
standoff_screw_height = 15
standoff_screw_radius = 1.39



def get_camera_trigger():

    PCB = Cube(size=[x_side,y_side,thickness])
    PCB = Color(PCB,rgba=[0,0.5,0,1.00])
    atmel = Cube(size=[x_atmel,y_atmel,thickness_atmel])
    atmel = Color(atmel,rgba=[0,0.4,0,1.00])
    atmel = Translate(atmel, v=[-(0.5*x_side - 0.5*x_atmel -7), -(0.5*y_side - 0.5*y_atmel), 0.5*thickness + 0.5*thickness_atmel])
#    USB = Cube(size=[x_USB, y_USB, z_USB])  # Makes actual cube 
    USB = Cube(size=[x_USB, 5*y_USB, z_USB+2*thickness_atmel]) # Makes oversized cube for Differencing
    USB = Translate(USB, v= [-(0.5*x_side - 0.5*x_atmel -7), -(0.5*y_side - 0.5*y_USB), 0.5*thickness + 0.5*z_USB])
    bnc_connector = Translate(bnc_conn, v=[0.5*x_side - 0.5*base_x - 8.33, -0.5*y_side+0.5*base_y+0.5*thickness, 0.5*base_z + 0.5*thickness])
    standoff = Cylinder(h=standoff_height ,r1=standoff_radius,r2=standoff_radius)
    standoff1 = Translate(standoff, v=[25,0.5*y_side - standoff_radius, - (0.5*standoff_height + 0.5*thickness)])
    standoff2 = Translate(standoff, v=[-25,0.5*y_side - standoff_radius, - (0.5*standoff_height + 0.5*thickness)])
    standoff3 = Translate(standoff, v=[25,-(0.5*y_side - standoff_radius),- (0.5*standoff_height + 0.5*thickness)])
    standoff4 = Translate(standoff, v=[-25,-(0.5*y_side - standoff_radius),- (0.5*standoff_height + 0.5*thickness)])

    standoff_screw = Cylinder(h=2*standoff_height + 2.5*thickness,r1=standoff_screw_radius,r2=standoff_screw_radius) 
    standoff_screw1 = Translate(standoff_screw, v=[25,0.5*y_side - standoff_radius, - 0.5*standoff_height])
    standoff_screw2 = Translate(standoff_screw, v=[-25,0.5*y_side - standoff_radius, - 0.5*standoff_height])
    standoff_screw3 = Translate(standoff_screw, v=[25,-(0.5*y_side - standoff_radius),- 0.5*standoff_height])
    standoff_screw4 = Translate(standoff_screw, v=[-25,-(0.5*y_side - standoff_radius),- 0.5*standoff_height])

    part = Union([PCB,atmel, USB, bnc_connector, standoff1,standoff2, standoff3, standoff4, standoff_screw1, standoff_screw2, standoff_screw3, standoff_screw4]);
    return part

#------------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":

    part = get_camera_trigger()
    prog = SCAD_Prog()
    prog.fn=50
    prog.add(part)
    prog.write('camera_trigger.scad')     






