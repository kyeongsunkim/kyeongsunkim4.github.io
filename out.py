# Boilerplate
import os, time, sys, math, random, json, requests, csv, subprocess
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scienceplots
import multiprocessing as mp
from scipy import stats
from plotnine import *
from plotnine.data import diamonds
from IPython.display import display
import xlsxwriter
import xmltodict
from plxscripting.easy import *
import plxscripting.easy
from collections import defaultdict
from collections import Mapping
from bs4 import BeautifulSoup
from lxml import objectify

# Initialize Output server
s_o, g_o = new_server('localhost', 10000, password='Ntf$m5vs6U^x=a+!')

# Create variables: bucket

bucket1 = g_o.RigidBodies[0][0]
bucket2 = g_o.RigidBodies[1][0]
bucket3 = g_o.RigidBodies[2][0]

# Create variables: phase_01

for x in range(1, 9):
    print('x =', x)
    locals()['phase_{0}'.format(x)] = g_o.Phases[x]
print(phase_2)
print("@@@@@@@@@@@@      222222222       @@@@@@@@@@@@@@")

# for phase 2_step1
phase1 = phase_2[0]

# Define ResultTypes
# Ref Points
resulttype_x = g_o.ResultTypes.RigidBody.XRef
resulttype_y = g_o.ResultTypes.RigidBody.YRef
resulttype_z = g_o.ResultTypes.RigidBody.ZRef
# Displacements
resulttype_Ux = g_o.ResultTypes.RigidBody.Ux
resulttype_Uy = g_o.ResultTypes.RigidBody.Uy
resulttype_Uz = g_o.ResultTypes.RigidBody.Uz
# Forces
resulttype_Fx = g_o.ResultTypes.RigidBody.Fxreaction
resulttype_Fy = g_o.ResultTypes.RigidBody.Fyreaction
resulttype_Fz = g_o.ResultTypes.RigidBody.Fzreaction
# Rotations
resulttype_Phix = g_o.ResultTypes.RigidBody.phix
resulttype_Phiy = g_o.ResultTypes.RigidBody.phiy
resulttype_Phiz = g_o.ResultTypes.RigidBody.phiz
# Moments
resulttype_Mx = g_o.ResultTypes.RigidBody.Mxreaction
resulttype_My = g_o.ResultTypes.RigidBody.Myreaction
resulttype_Mz = g_o.ResultTypes.RigidBody.Mzreaction

x_bucket1 = g_o.getresults(bucket1, phase1, resulttype_x, "node")
y_bucket1 = g_o.getresults(bucket1, phase1, resulttype_y, "node")
z_bucket1 = g_o.getresults(bucket1, phase1, resulttype_z, "node")
x_bucket2 = g_o.getresults(bucket2, phase1, resulttype_x, "node")
y_bucket2 = g_o.getresults(bucket2, phase1, resulttype_y, "node")
z_bucket2 = g_o.getresults(bucket2, phase1, resulttype_z, "node")
x_bucket3 = g_o.getresults(bucket3, phase1, resulttype_x, "node")
y_bucket3 = g_o.getresults(bucket3, phase1, resulttype_y, "node")
z_bucket3 = g_o.getresults(bucket3, phase1, resulttype_z, "node")

refpoint1 = (x_bucket1, y_bucket1, z_bucket1)
refpoint2 = (x_bucket2, y_bucket2, z_bucket2)
refpoint3 = (x_bucket3, y_bucket3, z_bucket3)

# Create Dataframe for 3 buckets

df1 = pd.DataFrame(refpoint1)
df2 = pd.DataFrame(refpoint2)
df3 = pd.DataFrame(refpoint3)

ref_bucket1 = (df1.iat[0, 0], df1.iat[1, 0], df1.iat[2, 0])
ref_bucket2 = (df2.iat[0, 0], df2.iat[1, 0], df2.iat[2, 0])
ref_bucket3 = (df3.iat[0, 0], df3.iat[1, 0], df3.iat[2, 0])

# Check location of bucket1
print("phase1 = ", phase1)
print("ref_bucket1 = ", ref_bucket1)  # (11.5, -8.13199996948242, -42.5)
print("ref_bucket2 = ", ref_bucket2)
print("ref_bucket3 = ", ref_bucket3)

# Get single result
# Displacements
Ux = g_o.getsingleresult(phase1, resulttype_Ux, ref_bucket1)
Uy = g_o.getsingleresult(phase1, resulttype_Uy, ref_bucket1)
Uz = g_o.getsingleresult(phase1, resulttype_Uz, ref_bucket1)
# Forces
Fx = g_o.getsingleresult(phase1, resulttype_Fx, ref_bucket1)
Fy = g_o.getsingleresult(phase1, resulttype_Fy, ref_bucket1)
Fz = g_o.getsingleresult(phase1, resulttype_Fz, ref_bucket1)
# Rotations
Phix = g_o.getsingleresult(phase1, resulttype_Phix, ref_bucket1)
Phiy = g_o.getsingleresult(phase1, resulttype_Phiy, ref_bucket1)
Phiz = g_o.getsingleresult(phase1, resulttype_Phiz, ref_bucket1)
# Moments
Mx = g_o.getsingleresult(phase1, resulttype_Mx, ref_bucket1)
My = g_o.getsingleresult(phase1, resulttype_My, ref_bucket1)
Mz = g_o.getsingleresult(phase1, resulttype_Mz, ref_bucket1)

# Loop through all phases
allphases = [p for p in g_o.Phases[:]]
print(allphases)


# Define get_plate function
def get_plate(phase_o):
    phase1 = phase_o

    bucket1 = g_o.RigidBodies[0][0]
    bucket2 = g_o.RigidBodies[1][0]
    bucket3 = g_o.RigidBodies[2][0]

    x_bucket1 = g_o.getresults(bucket1, phase1, resulttype_x, "node")
    y_bucket1 = g_o.getresults(bucket1, phase1, resulttype_y, "node")
    z_bucket1 = g_o.getresults(bucket1, phase1, resulttype_z, "node")
    x_bucket2 = g_o.getresults(bucket2, phase1, resulttype_x, "node")
    y_bucket2 = g_o.getresults(bucket2, phase1, resulttype_y, "node")
    z_bucket2 = g_o.getresults(bucket2, phase1, resulttype_z, "node")
    x_bucket3 = g_o.getresults(bucket3, phase1, resulttype_x, "node")
    y_bucket3 = g_o.getresults(bucket3, phase1, resulttype_y, "node")
    z_bucket3 = g_o.getresults(bucket3, phase1, resulttype_z, "node")

    refpoint1 = (x_bucket1, y_bucket1, z_bucket1)
    refpoint2 = (x_bucket2, y_bucket2, z_bucket2)
    refpoint3 = (x_bucket3, y_bucket3, z_bucket3)

    # Create Dataframe for 3 buckets

    df1 = pd.DataFrame(refpoint1)
    df2 = pd.DataFrame(refpoint2)
    df3 = pd.DataFrame(refpoint3)

    ref_bucket1 = (df1.iat[0, 0], df1.iat[1, 0], df1.iat[2, 0])
    ref_bucket2 = (df2.iat[0, 0], df2.iat[1, 0], df2.iat[2, 0])
    ref_bucket3 = (df3.iat[0, 0], df3.iat[1, 0], df3.iat[2, 0])
    #########################################
    # Displacements
    Ux1 = g_o.getsingleresult(phase1, resulttype_Ux, ref_bucket1)
    Uy1 = g_o.getsingleresult(phase1, resulttype_Uy, ref_bucket1)
    Uz1 = g_o.getsingleresult(phase1, resulttype_Uz, ref_bucket1)
    # Forces
    Fx1 = g_o.getsingleresult(phase1, resulttype_Fx, ref_bucket1)
    Fy1 = g_o.getsingleresult(phase1, resulttype_Fy, ref_bucket1)
    Fz1 = g_o.getsingleresult(phase1, resulttype_Fz, ref_bucket1)
    # Rotations
    Phix1 = g_o.getsingleresult(phase1, resulttype_Phix, ref_bucket1)
    Phiy1 = g_o.getsingleresult(phase1, resulttype_Phiy, ref_bucket1)
    Phiz1 = g_o.getsingleresult(phase1, resulttype_Phiz, ref_bucket1)
    # Moments
    Mx1 = g_o.getsingleresult(phase1, resulttype_Mx, ref_bucket1)
    My1 = g_o.getsingleresult(phase1, resulttype_My, ref_bucket1)
    Mz1 = g_o.getsingleresult(phase1, resulttype_Mz, ref_bucket1)
    ########################################
    # Displacements
    Ux2 = g_o.getsingleresult(phase1, resulttype_Ux, ref_bucket2)
    Uy2 = g_o.getsingleresult(phase1, resulttype_Uy, ref_bucket2)
    Uz2 = g_o.getsingleresult(phase1, resulttype_Uz, ref_bucket2)
    # Forces
    Fx2 = g_o.getsingleresult(phase1, resulttype_Fx, ref_bucket2)
    Fy2 = g_o.getsingleresult(phase1, resulttype_Fy, ref_bucket2)
    Fz2 = g_o.getsingleresult(phase1, resulttype_Fz, ref_bucket2)
    # Rotations
    Phix2 = g_o.getsingleresult(phase1, resulttype_Phix, ref_bucket2)
    Phiy2 = g_o.getsingleresult(phase1, resulttype_Phiy, ref_bucket2)
    Phiz2 = g_o.getsingleresult(phase1, resulttype_Phiz, ref_bucket2)
    # Moments
    Mx2 = g_o.getsingleresult(phase1, resulttype_Mx, ref_bucket2)
    My2 = g_o.getsingleresult(phase1, resulttype_My, ref_bucket2)
    Mz2 = g_o.getsingleresult(phase1, resulttype_Mz, ref_bucket2)
    ###########################################
    # Displacements
    Ux3 = g_o.getsingleresult(phase1, resulttype_Ux, ref_bucket3)
    Uy3 = g_o.getsingleresult(phase1, resulttype_Uy, ref_bucket3)
    Uz3 = g_o.getsingleresult(phase1, resulttype_Uz, ref_bucket3)
    # Forces
    Fx3 = g_o.getsingleresult(phase1, resulttype_Fx, ref_bucket3)
    Fy3 = g_o.getsingleresult(phase1, resulttype_Fy, ref_bucket3)
    Fz3 = g_o.getsingleresult(phase1, resulttype_Fz, ref_bucket3)
    # Rotations
    Phix3 = g_o.getsingleresult(phase1, resulttype_Phix, ref_bucket3)
    Phiy3 = g_o.getsingleresult(phase1, resulttype_Phiy, ref_bucket3)
    Phiz3 = g_o.getsingleresult(phase1, resulttype_Phiz, ref_bucket3)
    # Moments
    Mx3 = g_o.getsingleresult(phase1, resulttype_Mx, ref_bucket3)
    My3 = g_o.getsingleresult(phase1, resulttype_My, ref_bucket3)
    Mz3 = g_o.getsingleresult(phase1, resulttype_Mz, ref_bucket3)
    ##############################################
    col1 = 'UX1'
    col2 = 'UY1'
    col3 = 'UZ1'
    col4 = 'FX1'
    col5 = 'FY1'
    col6 = 'FZ1'
    col7 = 'RX1'
    col8 = 'RY1'
    col9 = 'RZ1'
    col10 = 'MX1'
    col11 = 'MY1'
    col12 = 'MZ1'
    col13 = 'UX2'
    col14 = 'UY2'
    col15 = 'UZ2'
    col16 = 'FX2'
    col17 = 'FY2'
    col18 = 'FZ2'
    col19 = 'RX2'
    col20 = 'RY2'
    col21 = 'RZ2'
    col22 = 'MX2'
    col23 = 'MY2'
    col24 = 'MZ2'
    col25 = 'UX3'
    col26 = 'UY3'
    col27 = 'UZ3'
    col28 = 'FX3'
    col29 = 'FY3'
    col30 = 'FZ3'
    col31 = 'RX3'
    col32 = 'RY3'
    col33 = 'RZ3'
    col34 = 'MX3'
    col35 = 'MY3'
    col36 = 'MZ3'

    results = {
        col1: Ux1,
        col2: Uy1,
        col3: Uz1,
        col4: Fx1,
        col5: Fy1,
        col6: Fz1,
        col7: Phix1,
        col8: Phiy1,
        col9: Phiz1,
        col10: Mx1,
        col11: My1,
        col12: Mz1,
        col13: Ux2,
        col14: Uy2,
        col15: Uz2,
        col16: Fx2,
        col17: Fy2,
        col18: Fz2,
        col19: Phix2,
        col20: Phiy2,
        col21: Phiz2,
        col22: Mx2,
        col23: My2,
        col24: Mz2,
        col25: Ux3,
        col26: Uy3,
        col27: Uz3,
        col28: Fx3,
        col29: Fy3,
        col30: Fz3,
        col31: Phix3,
        col32: Phiy3,
        col33: Phiz3,
        col34: Mx3,
        col35: My3,
        col36: Mz3
    }

    plateresults = pd.DataFrame(results, index=[1])
    return plateresults


# Run for loop for Phase2
df_list = []

for x in g_o.Phases[4]:
    print("In for loop, x = ", x)
    df_current = get_plate(x)
    df_list.append(df_current)
print('finished for loop!')

df_concat = pd.concat(df_list)

RESULT = df_concat

# Filename
EXCEL_PATH = r'C:\Users\Admin\Desktop\pytools\\'
EXCEL_NAME = 'plate_output_phase4.xlsx'
FILENAME = EXCEL_PATH + EXCEL_NAME
print("excel file name = ", FILENAME)

# Export
writer = pd.ExcelWriter(FILENAME, engine='xlsxwriter')
RESULT.to_excel(writer, "bucket123", index=False)
writer.save()

print("CODE FINISHED SUCCESSFULLY UNTIL HERE")
