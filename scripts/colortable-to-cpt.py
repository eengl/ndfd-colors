#!/usr/bin/env python

import re
import sys

colortableFile = sys.argv[1]

dVal = []
rVal = []
gVal = []
bVal = []

with open("colortable/"+colortableFile+".colortable",'r') as f: lines = f.read().splitlines()

for i,line in enumerate(lines):
    if i > 8:
        ctdata = re.sub(' +',' ',line.replace("\t"," ")).split(" ")
        dVal.append(float(ctdata[0]))
        rVal.append(int(ctdata[1]))
        gVal.append(int(ctdata[2]))
        bVal.append(int(ctdata[3]))

ncolors = len(dVal)

dVal = [x * 25.4 for x in dVal]

# Print .cpt file to screen
print "# NDFD-"+colortableFile.replace(".colortable","")+".cpt"
print "# COLOR_MODEL = RGB"
for i in range(len(dVal)-1):
    print "%f %3d %3d %3d %f %3d %3d %3d" % (dVal[i],rVal[i],gVal[i],bVal[i],dVal[i+1],rVal[i+1],gVal[i+1],bVal[i+1])
