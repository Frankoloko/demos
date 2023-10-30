####################################################################################################################
# .PHONY

.PHONY means "always run this command"

In make files, if you had something like this:

create_file:
    # create file code

do_all: create_file

If you run do_all here the first time, then a file will get created.

If you run it a second time, the file will not be created again (because the file already exists). It will skip over the create_file code. But, if you add create_file to .PHONY like so:

.PHONY: create_file
create_file:
    # create file code

do_all: create_file

Now create_file will get executed all the time.

Note that you can put the .PHONY line anywhere in the file, but a convention at DNEG is to put it just above the defined rule. 

You can also list multiples like:

.PHONY: create_file something another