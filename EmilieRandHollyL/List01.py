import arcpy
from arcpy import env

env.workspace=r"..\..\..\Data\SanFrancisco"

fclist=arcpy.ListFeatureClasses()

for fc in fclist:
    print fc

