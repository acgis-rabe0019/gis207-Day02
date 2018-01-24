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
#Command Line Argument Used: ..\..\..\Data\SanFrancisco Line

import sys
import arcpy
from arcpy import env


def setArcPy():
    global arcpy
    if arcpy == None:
        import arcpy


if len(sys.argv) != 3:
    print "Usage:  List03.py <FeatureClassName> <FeatureType>\n"
    print "where FeatureType is one of "
    print "     'Annotation', 'Arc', 'Dimension',"
    print "     'Edge', 'Junction', 'Label', 'Line', 'Multipatch', 'Node', 'Point', "
    print "     'Polygon', 'Polyline', 'Region', 'Route', 'Tic', 'All'"
    sys.exit()

else:
    setArcPy()
    fcdirectory=sys.argv[1]
    fctype=sys.argv[2]
    fctypes = ['Annotation', 'Arc', 'Dimension', 'Edge', 'Junction', 'Label',
               'Line', 'Multipatch', 'Node', 'Point', 'Polygon', 'Polyline', 'Region', 'Route', 'Tic', 'All']
    if fc in fctypes:
        print "Feature Class is not found"


    env.workspace=fcdirectory
    if arcpy.Exists(fcdirectory):
        fclist = arcpy.ListFeatureClasses("",fctype)
        for fc in fclist:
            descFC=arcpy.Describe(fc)
            print descFC.BaseName

    else:
        print "{} does not exists".format(fcdirectory)