#-------------------------------------------------------------------------------
# Name:        List05
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

rootFolder = r"..\..\..\Data"
fileList = []
for root, dirs, files in os.walk(rootFolder):
    for f in files:
        if f.find(".shp") >= 0:
            print os.path.join(root, f)

print "All done."