#-------------------------------------------------------------------------------
# Name:        List01
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

env.workspace=r"..\..\..\Data\SanFrancisco"

fclist=arcpy.ListFeatureClasses()

for fc in fclist:
    print fc

