import os
import arcpy
from arcpy import env

scriptPath = os.path.dirname(__file__)
os.chdir(scriptPath)
env.workspace = r"..\..\..\..\acgis\gis4207_Customization_1\day02\lab\Data\Canada"
fc = r"C:\Users\mie_r\Documents\acgis\gis4207_Customization_1\day02\lab\Data\Canada\province.shp"
dsFc = arcpy.Describe(fc)

print "BaseName : " + dsFc.BaseName
print "CatalogPath : " + dsFc.CatalogPath
print "DataType : " + dsFc.DataType
