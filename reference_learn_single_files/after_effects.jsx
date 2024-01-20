// ###########################################################################################################
// IMPORT A FILE
app.project.importFile(new ImportOptions(new File(yourFilePath)));

// ###########################################################################################################
// ###########################################################################################################
// ###########################################################################################################
// EXPRESSIONS CODE. These are the expressions you can write in the UI under layers

// Get a footage file
footage("file.json")

// Read the json
footage("file.json").sourceData["username"]

// Get the start time of the comp
thisComp.displayStartTime

// Get the current time
time

// Convert any time to frames
timeToFrames(time)