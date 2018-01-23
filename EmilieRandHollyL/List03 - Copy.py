#-------------------------------------------------------------------------------
# Name:        List03
# Purpose:
#
# Author:      holly long, emilie rabeau
#
# Created:     18-01-2018
# Copyright:   (c) holly 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Command Line Argument Used: ..\..\..\Data\SanFrancisco

#We need to redo list 3, maybe more as to not hard code anything
#and set two parameters for comman line
import sys
arcpy = None

def setArcPy():
    global arcpy
    if arcpy == None:
        import arcpy


if len(sys.argv) != 2:
    print "Usage:  List03.py <FeatureClassName>"
    sys.exit()

else:
    setArcPy()

    arcpy.env.workspace=sys.argv[1]
    fcdir =
    fclist =
    if arcpy.Exists(sys.argv[1]):
        fclist = arcpy.ListFeatureClasses(feature_type="Line")
        for f in fclist:
            print f

    else:
        print "{} does not exists".format(sys.argv[1])