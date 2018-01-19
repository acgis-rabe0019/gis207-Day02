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
        print "Usage:  Describe06.py <FeatureClassName>"

    else:
        setArcPy()
        fc=sys.argv[1]

        if arcpy.Exists(fc):
            dsFc=arcpy.Describe(fc)
            fields=dsFc.Fields
            fmt = "{:15} {:15} {:>5}"
            headings = ("Field Name", "Field Type", "Length")

            print fmt.format(*headings)
            print fmt.format(len(headings[0])*'-',len(headings[1])*'-',len(headings[2])*'-')
            for field in fields:
                print  fmt.format(field.name, field.type, field.Length)

        else:
            print "{} does not exists".format(fc)



if __name__=="__main__":
    main()