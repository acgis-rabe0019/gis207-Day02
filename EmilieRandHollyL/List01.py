import arcpy
from arcpy import env

env.workspace=r"..\..\..\Data\Canada"

fclist=arcpy.ListFeatureClasses(feature_type="Line")

for fc in fclist:
    print fc

