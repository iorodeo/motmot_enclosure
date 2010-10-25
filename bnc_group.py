"""
Test using bnc connnector module from another program
"""
from py2scad import *
import bnc_connector
base_x = bnc_connector.base_x
base_z = bnc_connector.base_z
edge_gap = 5.5
conn_gap = 11

bnc_conn = bnc_connector.get_bnc_connector()

# Units below are in mm
INCH2MM = 25.4
INCH2CM = 2.54


x_side = 4*INCH2MM
y_side = 31.8
thickness = 1.75
standoff_height = 12.67
standoff_radius = 3.23
standoff_screw_radius = 2.8
bnc_gap = 1*INCH2MM


def get_bnc_group():

    sig_0 = Translate(bnc_conn, v=[-1.5*bnc_gap,- (0.5*y_side) + 0.5*base_x, 0.5*base_z + 0.5*thickness])
    sig_1 = Translate(sig_0, v=[bnc_gap, 0, 0])
    sig_2 = Translate(sig_1, v=[bnc_gap, 0, 0])
    sig_3 = Translate(sig_2, v=[bnc_gap, 0, 0])

    part = Union([sig_0, sig_1, sig_2, sig_3]);
    return part

#------------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":

    part = get_bnc_group()
    prog = SCAD_Prog()
    prog.fn=50
    prog.add(part)
    prog.write('bnc_group.scad')     






