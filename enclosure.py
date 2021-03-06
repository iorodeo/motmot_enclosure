from py2scad import *

# Units below are in mm
INCH2MM = 25.4
INCH2CM = 2.54
output_type = 'assembly'
#output_type = 'dxf'

"""""""""""""""""""""""""""""
Measurements
"""""""""""""""""""""""""""""
enclosure_width = 17*INCH2MM
enclosure_length = 5*INCH2MM
enclosure_height = 1.75*INCH2MM
thickness = 0.125*INCH2MM
tab_length = 1*INCH2MM
standoff_height = 1.5*INCH2MM
standoff_radius = 0.125*INCH2MM
standoff_screw_radius = 1.39
standoff_screw_height = 2*standoff_height

"""""""""""""""""""""""""""""
Individual pieces
"""""""""""""""""""""""""""""

panel_tab = Cube(size=[thickness, thickness, 0.5*tab_length]) 
oversize_panel_tab = Cube(size=[1.05*thickness, 1.5*thickness, 0.5*tab_length])  
panel_tab_top = Cube(size=[tab_length, thickness, 1.05*thickness])
floor = Cube(size=[enclosure_width,enclosure_length, thickness])
side = Cube(size=[thickness, enclosure_length-thickness, enclosure_height-2*thickness])
back = Cube(size=[enclosure_width, thickness, enclosure_height-2*thickness])
tab_cube = Cube(size=[thickness, tab_length, thickness])                        
back_tab_cube = Cube(size=[tab_length, thickness, thickness])
lid = Cube(size=[enclosure_width,enclosure_length, thickness])

standoff_screw = Cylinder(h=2*standoff_height,r1=standoff_screw_radius,r2=standoff_screw_radius) 
standoff = Cylinder(h=standoff_height,r1=standoff_radius,r2=standoff_radius) 

"""""""""""""""""""""""""""""
Translations and tabs
"""""""""""""""""""""""""""""
pos_side = Translate(side, v=[0.5*enclosure_width - 0.5*thickness, 0, 0.5*enclosure_height-0.5*thickness])
tab_cube_1 = Translate(tab_cube, v=[0.5*enclosure_width - 0.5*thickness,0.5*(0.5*enclosure_length),0])
tab_cube_2 = Translate(tab_cube, v=[0.5*enclosure_width - 0.5*thickness, -0.5*(0.5*enclosure_length),0])
panel_tab_1 = Translate(panel_tab, v=[0.5*enclosure_width - 0.5*thickness, 0.5*enclosure_length,0.5*enclosure_height])
panel_tab_2 = Translate(panel_tab, v=[0.5*enclosure_width - 0.5*thickness, -0.5*enclosure_length,0.5*enclosure_height])
pos_side = Union([pos_side, tab_cube_1, tab_cube_2, panel_tab_1, panel_tab_2])
pos_side = Translate(pos_side, v=[0, -0.5*thickness, 0])

neg_side = Translate(side, v=[-(0.5*enclosure_width - 0.5*thickness), 0, 0.5*enclosure_height-0.5*thickness])
tab_cube_3 = Translate(tab_cube, v=[-(0.5*enclosure_width - 0.5*thickness),0.5*(0.5*enclosure_length),0])
tab_cube_4 = Translate(tab_cube, v=[-(0.5*enclosure_width - 0.5*thickness), -0.5*(0.5*enclosure_length),0])
panel_tab_3 = Translate(panel_tab, v=[-(0.5*enclosure_width - 0.5*thickness), 0.5*(enclosure_length),0.5*enclosure_height])
panel_tab_4 = Translate(panel_tab, v=[-(0.5*enclosure_width - 0.5*thickness), -0.5*(enclosure_length),0.5*enclosure_height])
neg_side = Union([neg_side, tab_cube_3, tab_cube_4, panel_tab_3, panel_tab_4])
neg_side = Translate(neg_side, v=[0, -0.5*thickness, 0])

oversize_pos_side = Translate(side, v=[0.5*enclosure_width - 0.5*thickness, 0, 0.5*enclosure_height-0.5*thickness])
tab_cube_1 = Translate(tab_cube, v=[0.5*enclosure_width - 0.5*thickness,0.5*(0.5*enclosure_length),0])
tab_cube_2 = Translate(tab_cube, v=[0.5*enclosure_width - 0.5*thickness, -0.5*(0.5*enclosure_length),0])
oversize_panel_tab_1 = Translate(oversize_panel_tab, v=[0.5*enclosure_width - 0.5*thickness, 0.5*enclosure_length ,0.5*enclosure_height])
oversize_panel_tab_2 = Translate(oversize_panel_tab, v=[0.5*enclosure_width - 0.5*thickness, -0.5*enclosure_length,0.5*enclosure_height])
oversize_pos_side = Union([oversize_pos_side, tab_cube_1, tab_cube_2, oversize_panel_tab_1, oversize_panel_tab_2])
oversize_pos_side = Translate(oversize_pos_side, v=[0, -0.5*thickness, 0])

oversize_neg_side = Translate(side, v=[-(0.5*enclosure_width - 0.5*thickness), 0, 0.5*enclosure_height-0.5*thickness])
tab_cube_3 = Translate(tab_cube, v=[-(0.5*enclosure_width - 0.5*thickness),0.5*(0.5*enclosure_length),0])
tab_cube_4 = Translate(tab_cube, v=[-(0.5*enclosure_width - 0.5*thickness), -0.5*(0.5*enclosure_length),0])
oversize_panel_tab_3 = Translate(oversize_panel_tab, v=[-(0.5*enclosure_width - 0.5*thickness), 0.5*(enclosure_length),0.5*enclosure_height])
oversize_panel_tab_4 = Translate(oversize_panel_tab, v=[-(0.5*enclosure_width - 0.5*thickness), -0.5*(enclosure_length),0.5*enclosure_height])
oversize_neg_side = Union([oversize_neg_side, tab_cube_3, tab_cube_4, oversize_panel_tab_3, oversize_panel_tab_4])
oversize_neg_side = Translate(oversize_neg_side, v=[0, -0.5*thickness, 0])

back = Translate(back, v=[0, 0.5*enclosure_length, 0.5*enclosure_height-0.5*thickness])
tab_cube_5 = Translate(back_tab_cube, v=[0,0.5*enclosure_length,0])
tab_cube_6 = Translate(tab_cube_5, v=[-0.5*(0.5*enclosure_width), 0, 0])
tab_cube_7 = Translate(tab_cube_5, v=[0.5*(0.5*enclosure_width), 0, 0])
tab_cube_8 = Translate(tab_cube_5, v=[0,0,enclosure_height-thickness])
tab_cube_9 = Translate(tab_cube_6, v=[0,0,enclosure_height-thickness])
tab_cube_10 = Translate(tab_cube_7, v=[0,0,enclosure_height-thickness])
back = Union([back, tab_cube_5, tab_cube_6, tab_cube_7, tab_cube_8, tab_cube_9, tab_cube_10])
back = Translate(back, v=[0, -0.5*thickness, 0])
#back.mod = '%' # Comment out for differencing


lid = Translate(lid, v=[0,0,enclosure_height-thickness])
panel_tab_5 = Translate(panel_tab_top, v=[0, -(0.5*enclosure_length+0.5*thickness), enclosure_height-thickness])
panel_tab_6 = Translate(panel_tab_5, v=[-0.25*enclosure_width, 0,0])
panel_tab_7 = Translate(panel_tab_5, v=[0.25*enclosure_width, 0,0])
lid = Union([lid, panel_tab_5, panel_tab_6, panel_tab_7])
#lid.mod = '%' # Comment out for differencing


panel_tab_8 = Translate(panel_tab_top, v=[0, -(0.5*enclosure_length+0.5*thickness), 0])
panel_tab_9 = Translate(panel_tab_8, v=[-0.25*enclosure_width, 0,0])
panel_tab_10 = Translate(panel_tab_8, v=[0.25*enclosure_width, 0,0])
floor = Union([floor,  panel_tab_8, panel_tab_9, panel_tab_10])


standoffa = Translate(standoff, v=[0, 0.5*enclosure_length-standoff_radius - 1*thickness, 0.5*standoff_height])
standoffb = Translate(standoff, v=[0, -(0.5*enclosure_length-standoff_radius - 1*thickness), 0.5*standoff_height])
standoff1 = Translate(standoffa, v=[0.5*enclosure_width-standoff_radius-1*thickness,0,0.5*thickness])
standoff2 = Translate(standoffb, v=[0.5*enclosure_width-standoff_radius-1*thickness, 0,0.5*thickness])
standoff3 = Translate(standoffa, v=[-(0.5*enclosure_width-standoff_radius-1*thickness),0,0.5*thickness])
standoff4 = Translate(standoffb, v=[-(0.5*enclosure_width-standoff_radius-1*thickness),0,0.5*thickness])
standoff_group = Union([standoff1, standoff2, standoff3, standoff4])


standoff_screwa = Translate(standoff_screw, v=[0, 0.5*enclosure_length-standoff_radius - 1*thickness, 0.5*standoff_height])
standoff_screwb = Translate(standoff_screw, v=[0, -(0.5*enclosure_length-standoff_radius - 1*thickness), 0.5*standoff_height])
standoff_screw1 = Translate(standoff_screwa, v=[0.5*enclosure_width-standoff_radius-1*thickness,0,0])
standoff_screw2 = Translate(standoff_screwb, v=[0.5*enclosure_width-standoff_radius-1*thickness, 0,0])
standoff_screw3 = Translate(standoff_screwa, v=[-(0.5*enclosure_width-standoff_radius-1*thickness),0,0])
standoff_screw4 = Translate(standoff_screwb, v=[-(0.5*enclosure_width-standoff_radius-1*thickness),0,0])


"""""""""""""""""""""""""""""
Differencing 
"""""""""""""""""""""""""""""

back_wall = Difference([back, pos_side, neg_side])
floor = Difference([floor, back, pos_side, neg_side, standoff_screw1, standoff_screw2, standoff_screw3, standoff_screw4])
#lid.mod = '%'
lid = Difference([lid, pos_side, neg_side, back, standoff_screw1, standoff_screw2, standoff_screw3, standoff_screw4])


"""""""""""""""""""""""""""""
For importing into motmot 
"""""""""""""""""""""""""""""
def get_oversizetabs_enclosure():
    part = Union([oversize_pos_side, oversize_neg_side, floor, lid, back_wall]); 
    return part

def get_enclosure_floor():
    part = Union([floor]) 
    return part

def get_enclosure():
    part = Union([floor, back, pos_side, neg_side, lid, standoff1, standoff2, standoff3, standoff4]); 
    return part


"""""""""""""""""""""""""""""""""""""""""""""
Projections - making the sides, back and lid
"""""""""""""""""""""""""""""""""""""""""""""

if output_type == 'dxf':


    back = Translate(back, v=[0, -0.5*enclosure_length, 2*enclosure_height])
    back = Rotate(back, a=90, v = [1,0,0])
    back = Translate(back, v=[0,0,0.5*thickness])

    neg_side = Translate(neg_side, v=[(0.5*enclosure_width - 0.5*thickness),0, -(0.5*enclosure_height-0.5*thickness)])
    neg_side = Rotate(neg_side, a=90, v= [0,1, 0])
    neg_side = Rotate(neg_side, a= 90, v= [0,0,1])
    neg_side = Translate(neg_side, v=[0.75*enclosure_length, 0.75*enclosure_length, 0])

    pos_side = Translate(pos_side, v=[-(0.5*enclosure_width - 0.5*thickness), 0, -(0.5*enclosure_height-0.5*thickness)])
    pos_side = Rotate(pos_side, a=90, v= [0,1, 0])
    pos_side = Rotate(pos_side, a=90, v= [0,0, 1])
    pos_side = Translate(pos_side, v=[-0.75*enclosure_length, 0.75*enclosure_length, 0])

    lid = Translate(lid, v=[0,0,-(enclosure_height-thickness)])

    back = Projection(back)
    neg_side = Projection(neg_side) 
    pos_side = Projection(pos_side)
    lid = Projection(lid)



#------------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":

#    part = get_enclosure()
    prog = SCAD_Prog()
    prog.fn=50
#    prog.add(pos_side)
#    prog.add(neg_side)
    prog.add(oversize_pos_side)
    prog.add(oversize_neg_side)
    prog.add(back)
    prog.add(lid)
    prog.add(floor)
#    prog.add(standoff_group)
#    prog.add(standoff_screw_group)    
    prog.write('enclosure.scad')     

