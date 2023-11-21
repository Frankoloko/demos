#######################################################################################################################
# LIST FILE INFO, PERMISSIONS, SIZE etc

# The -l flag just gives you more info
ls -l (the_file/folder) 
ls -l /some/folder

# For better file size use:
ls -lh /some/folder

#######################################################################################################################
# FIND AND KILL PROCESSES

`ps -eafx` to get all the running apps and their pid
`kill -HUP <pid>` to kill them