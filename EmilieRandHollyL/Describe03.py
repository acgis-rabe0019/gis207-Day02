#-------------------------------------------------------------------------------
# Name:        Describe03.py
# Purpose:
#
# Author:      holly long, emilie rabeau
#
# Created:     18-01-2018
# Copyright:   (c) holly 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# Command Line Arugument used: ..\..\..\Data\Canada\province.shp\

import os
import arcpy
import sys
from arcpy import env

scriptPath = os.path.dirname(__file__)
os.chdir(scriptPath)

fc = r"..\..\..\Data\Canada\province.shp"
dsFc = arcpy.Describe(fc)
fmt = "{:13}: {}"

if len(sys.argv) != 2:
   print "Usage:  Describe03.py <FeatureClassName>"
   sys.exit()

else:
    print fmt.format ("BaseName", dsFc.BaseName)
    print fmt.format ("CatalogPath", dsFc.CatalogPath)
    print fmt.format ("DataType", dsFc.DataType)