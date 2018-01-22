#-------------------------------------------------------------------------------
# Name:        List07
# Purpose:
#
# Author:      holly long, emilie rabeau
#
# Created:     18-01-2018
# Copyright:   (c) holly 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# Command Line Arugument used: ..\..\..\Data

import os
import arcpy

rootFolder = r"..\..\..\Data"
fileList = []


if os.path.exists(rootFolder):
    print "Usage:  List07.py <RootFolder>"

    arcpy.env.workspace=sys.argv[1]

    if arcpy.Exists(sys.argv[1]):
        fwork = arcpy.ListWorkspaces()
        for f in fwork:
            print f

    for root, dirs, files in os.walk(rootFolder):
        for i in files:
            if i.find(".shp") >= 0:
                print os.path.join(rootFolder, i)

else:
    print "{} does not exists".format(rootFolder)