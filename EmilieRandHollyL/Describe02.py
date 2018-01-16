import os
import arcpy
from arcpy import env

scriptPath = os.path.dirname(__file__)
os.chdir(scriptPath)

fc = r"..\..\..\Data\Canada\province.shp"
dsFc = arcpy.Describe(fc)
fmt = "{:13}: {}"

print fmt.format ("BaseName", dsFc.BaseName)
print fmt.format ("CatalogPath", dsFc.CatalogPath)
print fmt.format ("DataType", dsFc.DataType)