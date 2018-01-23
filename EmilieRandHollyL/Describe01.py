#-------------------------------------------------------------------------------
# Name:        Describe01
# Purpose:
#
# Author:      holly long, emilie rabeau
#
# Created:     18-01-2018
# Copyright:   (c) holly 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
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
