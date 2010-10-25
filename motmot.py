"""
Making the front panel
"""
from py2scad import *
import motmot_components
import bnc_module
import enclosure as enclosure_module
motmot_components = motmot_components.get_motmot_components()
enclosure = enclosure_module.get_enclosure()

standoff_height = bnc_module.standoff_height
enclosure_length = enclosure_module.enclosure_length

# Units below are in mm
INCH2MM = 25.4
INCH2CM = 2.54

"""""""""""""""""""""""""""""
Measurements
"""""""""""""""""""""""""""""
bnc_conn_length = 31.8
thickness = 0.125*INCH2MM
panel_length = 19*INCH2MM
panel_height = 1.75*INCH2MM
screw_diameter = 0.221*INCH2MM
slot_gap = 0.25*screw_diameter

"""""""""""""""""""""""""""""
Add Front Panel
"""""""""""""""""""""""""""""

panel = Cube(size=[panel_length, thickness, panel_height])
panel = Translate(panel, v=[0, 0, 0.5*panel_height])


"""""""""""""""""""""""""""""
Add screw holes
"""""""""""""""""""""""""""""

screwhole = Cube(size=[slot_gap, screw_diameter, 2*thickness])

slot = Cylinder(h=2*thickness ,r1=0.5*screw_diameter,r2=0.5*screw_diameter)
slot_pos = Translate(slot, v=[0.5*slot_gap, 0, 0])
slot_neg = Translate(slot, v=[-0.5*slot_gap, 0, 0])
screwhole = Union([slot, slot_pos, slot_neg])

screwhole = Rotate(screwhole, a=90, v=[1,0,0])
pos_screwhole = Translate(screwhole, v=[0.5*panel_length - 0.344*INCH2MM, 0, 0.5*panel_height])
neg_screwhole = Translate(screwhole, v=[-(0.5*panel_length - 0.344*INCH2MM), 0, 0.5*panel_height])
screwhole1 = Translate(pos_screwhole, v=[0, 0, 0.625*INCH2MM])
screwhole2 = Translate(pos_screwhole, v=[0, 0, -0.625*INCH2MM])
screwhole3 = Translate(neg_screwhole, v=[0, 0, 0.625*INCH2MM])
screwhole4 = Translate(neg_screwhole, v=[0, 0, -0.625*INCH2MM])


"""""""""""""""""""""""""""""
Add enclosure
"""""""""""""""""""""""""""""

enclosure = Translate(enclosure, v=[0,0.5*enclosure_length+0.5*thickness,0.5*thickness])

"""""""""""""""""""""""""""""
Add guts
"""""""""""""""""""""""""""""

motmot_components = Translate(motmot_components, v=[0, 0.5*bnc_conn_length + 1*thickness, standoff_height+0.5*thickness])

"""""""""""""""""""""""""""""
Difference  - choose one
"""""""""""""""""""""""""""""
#panel = Difference([panel, screwhole1, screwhole2, screwhole3, screwhole4, motmot_components, enclosure]) # To get the front panel
#enclosure = Difference([enclosure, motmot_components]) # To get floor piece


"""""""""""""""""""""""""""""
Projections for panel
"""""""""""""""""""""""""""""

##if 1:
#panel = Translate(panel, v=[0, 0, -0.5*panel_height])
#panel = Rotate(panel, a=270, v=[1,0,0])
#panel = Projection(panel)
#reference = Cube(size = [1*INCH2MM,1*INCH2MM,1*INCH2MM]) 
#reference = Translate(reference, v=[0, 1.5*panel_height, 0])
#reference = Projection(reference) 

"""""""""""""""""""""""""""""
Projections for floor
"""""""""""""""""""""""""""""
#enclosure = Projection(enclosure)


#------------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":


    prog = SCAD_Prog()
    prog.fn=100
    prog.add(panel)
    prog.add(motmot_components)
    prog.add(enclosure)
    prog.add(screwhole1)
    prog.add(screwhole2)
    prog.add(screwhole3)
    prog.add(screwhole4)
#    prog.add(reference)
    prog.write('motmot.scad')     







