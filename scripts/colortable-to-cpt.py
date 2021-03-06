#!/usr/bin/env python

# ---------------------------------------------------------------------------------------- 
# Import modules
# ---------------------------------------------------------------------------------------- 
import re
import sys

# ---------------------------------------------------------------------------------------- 
# Test for command arguments
# ---------------------------------------------------------------------------------------- 
if len(sys.argv) != 3:
    print "usage: ",sys.argv[0]," <COLORTABLE_FILE> <CPT_FILE>"
    exit(1)

# ---------------------------------------------------------------------------------------- 
# Get command arguments
# ---------------------------------------------------------------------------------------- 
colortableFile = sys.argv[1]
cptFile = sys.argv[2]

# ---------------------------------------------------------------------------------------- 
# Initialize lists
# ---------------------------------------------------------------------------------------- 
dVal = []
rVal = []
gVal = []
bVal = []

# ---------------------------------------------------------------------------------------- 
# Read .colortable file
# ---------------------------------------------------------------------------------------- 
with open(colortableFile) as f: lines = f.read().splitlines()

# ---------------------------------------------------------------------------------------- 
# Parse colortable data
# ---------------------------------------------------------------------------------------- 
for i,line in enumerate(lines):
    if i > 8:
        ctdata = re.sub(' +',' ',line.replace("\t"," ")).split(" ")
        dVal.append(float(ctdata[0]))
        rVal.append(int(ctdata[1]))
        gVal.append(int(ctdata[2]))
        bVal.append(int(ctdata[3]))

# ---------------------------------------------------------------------------------------- 
# Print .cpt file to screen
# ---------------------------------------------------------------------------------------- 
fout = open(cptFile,"w")
fout.write("# NDFD-"+colortableFile.replace(".colortable","")+".cpt\n")
fout.write("# COLOR_MODEL = RGB\n")
for i in range(len(dVal)-1):
    fout.write("%f %3d %3d %3d %f %3d %3d %3d\n" % (dVal[i],rVal[i],gVal[i],bVal[i],dVal[i+1],rVal[i+1],gVal[i+1],bVal[i+1]))

# ---------------------------------------------------------------------------------------- 
# Close output file
# ---------------------------------------------------------------------------------------- 
fout.close()
