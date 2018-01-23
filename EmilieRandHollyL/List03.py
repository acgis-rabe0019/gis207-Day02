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
#Command Line Argument Used: ..\..\..\Data Line

import sys
import arcpy
from arcpy import env


def setArcPy():
    global arcpy
    if arcpy == None:
        import arcpy


if len(sys.argv) != 3:
    print "Usage:  List03.py <FeatureClassName>"
    sys.exit()

else:
    setArcPy()
    fcdirectory=sys.argv[1]
    fctype=sys.argv[2]

    env.workspace=fcdirectory
    if arcpy.Exists(fcdirectory):
        fclist = arcpy.ListFeatureClasses("",fctype)
        for fc in fclist:
            descFC=arcpy.Describe(fc)
            print descFC.BaseName

    else:
        print "{} does not exists".format(fcdirectory)