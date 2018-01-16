import os
import arcpy
from arcpy import env

scriptPath = os.path.dirname(__file__)
os.chdir(scriptPath)
env.workspace = r"..\..\..\Data\Canada\province.shp"
#fc = r"C:\Users\mie_r\Documents\acgis\gis4207_Customization_1\day02\lab\Data\Canada\province.shp"
dsFc = arcpy.Describe(env.workspace)

print "BaseName : " + dsFc.BaseName
print "CatalogPath : " + dsFc.CatalogPath
print "DataType : " + dsFc.DataType
