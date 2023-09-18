This will set the "TEST" env variable, but only for the current terminal session.
```
export TEST=something
```

#############################################################
# CHANGE PERMISSIONS

# -R to get all children
# 777 gives all permissions to everyone
SUDO chmod -R 777 /some/file/path

#############################################################
# CHECK CURRENT PERMISSIONS

stat -c %a /some/file/path

#############################################################
# SSH INTO ANOTHER LOCATION

ssh something

