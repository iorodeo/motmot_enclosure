"""
Test using bnc connnector module from another program
"""
from py2scad import *
import pcb_bnc_connector
base_x = pcb_bnc_connector.base_x
base_z = pcb_bnc_connector.base_z
edge_gap = 5.5
conn_gap = 11
bnc_conn = pcb_bnc_connector.get_bnc_connector()

"""""""""""""""""""""""""""""""""
PCB parameters
"""""""""""""""""""""""""""""""""

x_side = 101.6
y_side = 31.8
thickness = 1.75
standoff_height = 12.67
standoff_radius = 3.23

PCB = Cube(size=[x_side,y_side,thickness])
PCB = Color(PCB,rgba=[0,0.5,0,1.00])
standoff = Cylinder(h=standoff_height ,r1=standoff_radius,r2=standoff_radius)
standoff1 = Translate(standoff, v=[25,0.5*y_side - standoff_radius, - 0.5*standoff_height])
standoff2 = Translate(standoff, v=[-25,0.5*y_side - standoff_radius, - 0.5*standoff_height])
standoff3 = Translate(standoff, v=[25,-(0.5*y_side - standoff_radius),- 0.5*standoff_height])
standoff4 = Translate(standoff, v=[-25,-(0.5*y_side - standoff_radius),- 0.5*standoff_height])


"""""""""""""""""""""""""""""""""
Add BNC connectors
"""""""""""""""""""""""""""""""""

sig_0 = Translate(bnc_conn, v=[0.5*x_side - 0.5*base_x - edge_gap, - (0.5*y_side) + 0.5*base_x, 0.5*base_z + 0.5*thickness])
sig_1 = Translate(sig_0, v =[- base_x - conn_gap, 0, 0])
sig_2 = Translate(bnc_conn, v=[-(0.5*x_side - 0.5*base_x - edge_gap), - (0.5*y_side) + 0.5*base_x, 0.5*base_z + 0.5*thickness])
sig_3 = Translate(sig_2, v=[base_x + conn_gap, 0, 0])

prog = SCAD_Prog()
prog.fn = 50
prog.add(PCB)
prog.add(standoff1)
prog.add(standoff2)
prog.add(standoff3)
prog.add(standoff4)
prog.add(sig_0)
prog.add(sig_1)
prog.add(sig_2)
prog.add(sig_3)
prog.write('bnc_test.scad')





