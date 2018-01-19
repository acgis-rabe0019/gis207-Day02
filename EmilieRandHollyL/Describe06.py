#-------------------------------------------------------------------------------
# Name:        Describe06
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

        if arcpy.Exists(fc):
            dsFc=arcpy.Describe(fc)
            fmt = "{:13}: {}"
            print fmt.format ("BaseName", dsFc.BaseName)
            print fmt.format ("CatalogPath", dsFc.CatalogPath)
            print fmt.format ("DataType", dsFc.DataType)

        else:
            print "{} does not exists".format(fc)

    fmt = "{:15} {:15} {:->4}"
    headings = ("Field Name", "Field Type", "Length")

    print fmt.format(*headings)
    print fmt.format(len(headings[0])*'-',len(headings[1])*'-',len(headings[2])*'-')
    print fmt.format( )

if __name__=="__main__":
    main()