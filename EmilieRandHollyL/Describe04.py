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

scriptPath = os.path.dirname(__file__)
os.chdir(scriptPath)

def main():

    if len(sys.argv) != 2:
        print "Usage:  Describe03.py <FeatureClassName>"

    else:

        print fmt.format ("BaseName", dsFc.BaseName)
        print fmt.format ("CatalogPath", dsFc.CatalogPath)
        print fmt.format ("DataType", dsFc.DataType)

    setArcPy()

def setArcPy():
    global arcpy
    if arcpy == None:
        import arcpy
    env.workspace = r"..\..\..\Data\Canada\province.shp"
    dsFc = arcpy.Describe(env.workspace)

if __name__=="__main__":
    main()