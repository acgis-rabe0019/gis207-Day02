
import arcpy
import sys
from arcpy import env

##scriptPath = os.path.dirname(__file__)
##os.chdir(scriptPath)
##env.workspace = r"..\..\..\Data\Canada\province.shp"

fc = sys.argv[1]
dsFc = arcpy.Describe(fc)

if len(sys.argv) != 2:
   print "Usage:  Describe03.py <FeatureClassName>"

else:

    print fmt.format ("BaseName", dsFc.BaseName)
    print fmt.format ("CatalogPath", dsFc.CatalogPath)
    print fmt.format ("DataType", dsFc.DataType)