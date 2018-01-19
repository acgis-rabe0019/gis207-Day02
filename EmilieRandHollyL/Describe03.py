import os
import arcpy
import sys
from arcpy import env

scriptPath = os.path.dirname(__file__)
os.chdir(scriptPath)

fc = r"..\..\..\Data\Canada\province.shp"
dsFc = arcpy.Describe(fc)
fmt = "{:13}: {}"

if len(sys.argv) != 2:
   print "Usage:  Describe03.py <FeatureClassName>"
   sys.exit()

else:
    print fmt.format ("BaseName", dsFc.BaseName)
    print fmt.format ("CatalogPath", dsFc.CatalogPath)
    print fmt.format ("DataType", dsFc.DataType)