# Server Directory Migration
# dirMigrate.py
# Created by Taylor C. Johnson
# Date created: 20150114
# Date updated: 20150115
# Version: 10.2.2
# Abstract: Migrate layer workspace paths in all .mxd files in a user-specified directory

import os, arcpy, Tkinter, tkFileDialog
from time import sleep

def mxdReport(startDir):
    mxdCount = 0
    mxdList = []
    for dirs, subDirs, files in os.walk(startDir):
        for fi in files:
            fullPath = os.path.join(os.path.normpath(dirs), fi)
            if os.path.isfile(fullPath):
                basename, extension = os.path.splitext(fullPath)
                if extension == ".mxd":
                    mxdCount += 1
                    mxdList.append(fullPath)
    print("\nTotal .mxds to update: {0}".format(mxdCount))
    return mxdList

def updateMXD(mxdPath, oldSource, newSource):
    mxd = arcpy.mapping.MapDocument(mxdPath)
    mxd.findAndReplaceWorkspacePaths(oldSource, newSource)
    #mxd.saveACopy(mxdPath[0:-4] + "_fixed.mxd")
    mxd.save()
    print("Updated and Saved: {0}".format(mxdPath))
    del mxd



try:
    print("This script updates the workspace paths for migrated layers in all ArcGIS project files (.mxd) within a parent directory.")
    sleep(5)
    
    root = Tkinter.Tk()
    root.withdraw()
    startDir = tkFileDialog.askdirectory(title='Parent .mxd Search Directory:', initialdir='P:\\')
    oldPath = os.path.normpath(tkFileDialog.askdirectory(title='Original Workspace Directory:', initialdir='Q:\\'))
    newPath = os.path.normpath(tkFileDialog.askdirectory(title='New Workspace Directory:', initialdir='P:\\'))
    print("The script will search the following directory: {0}".format(startDir))
    print("The script will replace {0} with {1}".format(oldPath, newPath))
    
    for mxdPath in mxdReport(startDir):
        updateMXD(mxdPath, oldPath, newPath)

finally:
    print("End of Script")
