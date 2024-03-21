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

#######################################################################################################################
# COPY FILES FROM ONE LOCATION TO ANOTHER

rsync source destination
rsync /source/area/file.ma francois@machine115:/some/place/thing.ma

#######################################################################################################################
# MOUNTING/BINDING THINGS

# Create a link/replacement
sudo mount --bind /new/file.xml /original/file.xml
 
# List all the links currently on your machine
mount -l
 
# Revert/Undo the link
sudo umount /original/file.xml

#######################################################################################################################
# SYMLINKING FILES

ln -s /some/place/file.txt .☻

#######################################################################################################################
# FIX A SLOW TERMINAL

# You need to clear your ~/.history file, because it is too large and is holding all your previous terminal
# commands. To clear it run this:

# Close all open terminals first!
cat /dev/null > ~/.history && history -c && exit

#######################################################################################################################
# FIND A FILE

find /some/place -name "general.dat"
find / -name "general.dat" # To search from root
find /some/place -type d -name "general.dat" # -type d to search for directories/folders
find /some/place -type f -name "general.dat" # -type f to search for directories/folders

#######################################################################################################################
# READ A FILE

cat /the/file.txt

#######################################################################################################################
# RPRINT ENVIRONMENT VARIABLE VALUE

echo $THE_VARIABLE