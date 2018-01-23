#-------------------------------------------------------------------------------
# Name:        List08
# Purpose:
#
# Author:      holly long, emilie rabeau
#
# Created:     18-01-2018
# Copyright:   (c) holly 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# Command Line Arugument used: ..\..\..\Data outFileName.txt

import os
import sys
import arcpy
from arcpy import env

def setArcPy():
    global arcpy
    if arcpy == None:
        import arcpy

if len(sys.argv) != 3:
    print "Usage: List08.py <RootFolder>"
    sys.exit()

else:
    setArcPy()

    arcpy.env.workspace = sys.argv[1]

    if arcpy.Exists(sys.argv[1]):
        outFileName=open(sys.argv[2], 'w')

        for root, dirs, files in os.walk(sys.argv[1]):
            arcpy.env.workspace = root
            workspaces = arcpy.ListWorkspaces('*','All')

            for workspace in workspaces:
                info1=os.path.abspath(workspace)
                outFileName.write(info1, "\n")

                arcpy.env.workspace = os.path.abspath(workspace)
                fc = arcpy.ListFeatureClasses()

                for feature_class in fc:
                    info2=os.path.join(workspace, feature_class)
                    outFileName.write(info2,"\n")

        outFileName.write("\n")
        outFileName.close()
    else:
        print "{} does not exists".format(root)

