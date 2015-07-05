# dirMigrate
### Abstract
Python script to update workspace paths in all .mxds in a directory tree.  The script checks all .mxds files in a directory tree to see if any contain layers in the user-specified directory (the 'from' directory in the data migration).  If any exist, the script updates their workspace path to the new user-specified directory (the 'to' directory in the data migration).

### Version
The script is at version 1.0 and has been tested for ArcGIS 10.2.2

### Updates
Eventually, a full Tkinter (or Qt) user interface should be developed.  This is will remove any command-line dependencies while also not be required to run inside of ArcGIS/ArcCatalog (though it could be re-written as an ESRI tool).
