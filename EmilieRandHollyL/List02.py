#-------------------------------------------------------------------------------
# Name:        List02.py
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

def main():

    if len(sys.argv) != 2:
        print "Usage:  List02.py <FeatureClassName>"

    else:
        setArcPy()
        fc=sys.argv[1]

        if arcpy.Exists(fc):
            fclist = arcpy.ListFeatureClasses(fc)
            for fc in fclist:
                print fc

        else:
            print "{} does not exists".format(fc)

if __name__=="__main__":
    main()

