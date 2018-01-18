import os
import arcpy
from arcpy import env

scriptPath = os.path.dirname(__file__)
os.chdir(scriptPath)
env.workspace = r"..\..\..\Data\Canada\province.shp"
dsFc = arcpy.Describe(env.workspace)

print "BaseName : " + dsFc.BaseName
print "CatalogPath : " + dsFc.CatalogPath
print "DataType : " + dsFc.DataType
