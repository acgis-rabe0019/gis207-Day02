import sys
arcpy = None

scriptPath = os.path.dirname(__file__)
os.chdir(scriptPath)


def main():

    if arcpy.Exists():
        print fmt.format ("BaseName", dsFc.BaseName)
        print fmt.format ("CatalogPath", dsFc.CatalogPath)
        print fmt.format ("DataType", dsFc.DataType)
    else:
        print fc + "does not exists"

        setArcPy()

def setArcPy():
    global arcpy
    if arcpy == None:
        import arcpy

        env.workspace = r"..\..\..\Data\Canada\province.shp"
        dsEx = arcpy.Exists(env.workspace)
        dsFc = arcpy.Describe(env.workspace)

if __name__=="__main__":
    main()