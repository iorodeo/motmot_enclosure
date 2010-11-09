"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Makes the enclosure front panel and floor parts for the Motmot device 
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

from py2scad import *
import motmot_components
import bnc_module
import enclosure as enclosure_module
import camera_trigger

motmot_components = motmot_components.get_motmot_components()
enclosure = enclosure_module.get_oversizetabs_enclosure()
enclosure_floor = enclosure_module.get_enclosure_floor()
standoff_height = bnc_module.standoff_height
enclosure_length = enclosure_module.enclosure_length
pcb_thickness = camera_trigger.thickness
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


""""""""""""""""""""""""""""""""""""""""""""""
Add screw holes for fastening to rackmount
"""""""""""""""""""""""""""""""""""""""""""""
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
Difference screw holes from front panel
"""""""""""""""""""""""""""""
panel = Difference([panel, screwhole1, screwhole2, screwhole3, screwhole4]) 

"""""""""""""""""""""""""""""
Add guts
"""""""""""""""""""""""""""""
motmot_components = Translate(motmot_components, v=[0, 0.5*bnc_conn_length + 1*thickness, 0.5*pcb_thickness+ thickness + standoff_height])

"""""""""""""""""""""""""""""
Choice 1: View assembly
"""""""""""""""""""""""""""""
enclosure_assembly = Translate(enclosure, v=[0,0.5*enclosure_length+0.5*thickness,0.5*thickness])
prog_assembly = SCAD_Prog()
prog_assembly.fn=100
prog_assembly.add(panel)
prog_assembly.add(motmot_components)
prog_assembly.add(enclosure_assembly)
prog_assembly.write('motmot_assembly.scad');

"""""""""""""""""""""""""""""
Choice 2: Make front panel
"""""""""""""""""""""""""""""
enclosure = Translate(enclosure, v=[0,0.5*enclosure_length+0.5*thickness,0.5*thickness])
panel = Difference([panel, motmot_components, enclosure]) 
panel = Translate(panel, v=[0, 0, -0.5*panel_height])
panel = Rotate(panel, a=270, v=[1,0,0])
panel = Projection(panel)
reference = Cube(size = [1*INCH2MM,1*INCH2MM,1*INCH2MM]) 
reference = Translate(reference, v=[0, 1.5*panel_height, 0])
reference = Projection(reference) 
prog_panel = SCAD_Prog()
prog_panel.fn=100
prog_panel.add(panel)
prog_panel.add(reference)
prog_panel.write('motmot_panel.scad')     

"""""""""""""""""""""""""""""
Choice 3: Make floor piece
"""""""""""""""""""""""""""""
enclosure_floor = Translate(enclosure_floor, v=[0,0.5*enclosure_length+0.5*thickness,0.5*thickness])
enclosure_floor = Difference([enclosure_floor, motmot_components]) 
enclosure_floor = Projection(enclosure_floor)
prog_floor = SCAD_Prog()
prog_floor.fn=100
prog_floor.add(enclosure_floor)
prog_floor.write('motmot_floor.scad')     









