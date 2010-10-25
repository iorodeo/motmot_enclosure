"""
Test using bnc connnector module from another program
"""
from py2scad import *
import bnc_connector
import bnc_module
import camera_trigger
x_side = bnc_module.x_side
y_side = bnc_module.y_side
#module_y = bnc_module.y_side
camera_y = camera_trigger.y_side
bnc_module = bnc_module.get_bnc_module()
camera_trigger = camera_trigger.get_camera_trigger()
thread_height = bnc_connector.thread_height
conn_height = bnc_connector.conn_height

# Units below are in cm
INCH2MM = 25.4
INCH2CM = 2.54


"""""""""""""""""""""""""""""
Add BNC modules + camera trigger
"""""""""""""""""""""""""""""
def get_motmot_components():

    module_0 = Translate(camera_trigger, v=[-(0.5*17*INCH2MM - (0.5*57.2) -0.55*INCH2MM), 0.5*camera_y - 0.5*y_side , 0])
    #module_0 = Translate(camera_trigger, v=[0, 0, 0])
    module_1 = Translate(bnc_module, v=[0.5*17*INCH2MM - 0.5*x_side - 0.55*INCH2MM,0,0])
    module_2 = Translate(module_1, v=[-(1*x_side + 0.55*INCH2MM),0,0])
    module_3 = Translate(module_2, v=[-(1*x_side + 0.55*INCH2MM),0,0])

    part = Union([module_0,module_1,module_2, module_3]);
    return part
    #return [module_0, module_1, module_2, module_3]

#------------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":

    part = get_motmot_components()
    prog = SCAD_Prog()
    prog.fn=50
    prog.add(part)
    prog.write('motmot_components.scad')     







