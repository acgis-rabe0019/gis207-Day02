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
# Command Line Arugument used: ..\..\..\Data

import os
import sys
arcpy=None

def setArcPy():
    global arcpy
    if arcpy == None:
        import arcpy

if len(sys.argv) != 2:
    print "Usage: List08.py <RootFolder>"
    sys.exit()

else:
    setArcPy()

    arcpy.env.workspace = sys.argv[1]

    if arcpy.Exists(sys.argv[1]):
        for root, dirs, files in os.walk(sys.argv[1]):
            arcpy.env.workspace = root
            workspaces = arcpy.ListWorkspaces('*','All')

            for workspace in workspaces:
                print os.path.abspath(workspace)

                arcpy.env.workspace = os.path.abspath(workspace)
                fc = arcpy.ListFeatureClasses()

                for feature_class in fc:
                    print os.path.join(workspace, feature_class)
                print '\n'

                fileOut = open(r"C:\Users\mie_r\Documents\acgis\gis4207_Customization_1\Data\outputfilename.txt", 'w')
                fileOut.write(ww)
                file.close

    else:
        print "{} does not exists".format(root)