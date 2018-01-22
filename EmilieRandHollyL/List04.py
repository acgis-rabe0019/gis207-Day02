#-------------------------------------------------------------------------------
# Name:        List04
# Purpose:
#
# Author:      holly long, emilie rabeau
#
# Created:     18-01-2018
# Copyright:   (c) holly 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys
arcpy = None

def setArcPy():
    global arcpy
    if arcpy == None:
        import arcpy


if len(sys.argv) != 2:
    print "Usage:  List04.py <FeatureClassName>"
    sys.exit()

else:
    setArcPy()

    arcpy.env.workspace=sys.argv[1]

    if arcpy.Exists(sys.argv[1]):
        fwork = arcpy.ListWorkspaces()
        for f in fwork:
            print f

    else:
        print "{} does not exists".format(sys.argv[1])
