#-------------------------------------------------------------------------------
# Name:        List03
# Purpose:
#
# Author:      holly long, emilie rabeau
#
# Created:     18-01-2018
# Copyright:   (c) holly 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy
from arcpy import env

env.workspace=r"..\..\..\Data\Canada"

fclist=arcpy.ListFeatureClasses(feature_type="Line")

for fc in fclist:
    print fc