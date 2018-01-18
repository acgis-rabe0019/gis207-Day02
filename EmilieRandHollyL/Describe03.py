
import arcpy
import sys
from arcpy import env


if len(sys.argv) != 2:
   print "Usage:  Describe03.py <FeatureClassName>"
   sys.exit()

else:

    print fmt.format ("BaseName", dsFc.BaseName)
    print fmt.format ("CatalogPath", dsFc.CatalogPath)
    print fmt.format ("DataType", dsFc.DataType)