import os
import arcpy
import sys
from arcpy import env

scriptPath = os.path.dirname(__file__)
os.chdir(scriptPath)
env.workspace = r"..\..\..\Data\Canada\province.shp"

if len(sys.argv) > 0:
    print (sys.argv[2])
else:
    print "Usage:  Describe03.py <FeatureClassName>"



