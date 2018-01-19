#-------------------------------------------------------------------------------
# Name:        Describe04
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
        print "Usage:  Describe03.py <FeatureClassName>"

    else:
        setArcPy()
        fc=sys.argv[1]
        dsEx=arcpy.Exists(fc)
        dsFc=arcpy.Describe(fc)
        fmt = "{:13}: {}"
        print fmt.format ("BaseName", dsFc.BaseName)
        print fmt.format ("CatalogPath", dsFc.CatalogPath)
        print fmt.format ("DataType", dsFc.DataType)

if __name__=="__main__":
    main()