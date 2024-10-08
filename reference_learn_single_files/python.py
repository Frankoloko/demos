# A good way to test something if you are unsure if prints work in the environment
# raise ImportError()

############################################################################################################
# TIME CODE EXECUTION

import time
start_time = time.time()
 
# Your code here
# for _ in range(100):
# ...
 
end_time = time.time()
elapsed_time = end_time - start_time
print(f"The code took {elapsed_time} seconds to execute.")

############################################################################################################
# REVERSE A LIST

# Fastest way I know of
[1, 2, 3][::-1]

############################################################################################################
# BASIC PYTHON VENV

# To create a virtualenv run this. It will create all the required files: python -m venv /path/to/new/virtual/environment
# Then you need to "turn on" (activate) the virtual env: 

# Platform
# Shell
# Command to activate virtual environment
# POSIX
# bash/zsh
# $ source <venv>/bin/activate (use this at DNEG)
# fish
# $ source <venv>/bin/activate.fish
# csh/tcsh
# $ source <venv>/bin/activate.csh
# PowerShell
# $ <venv>/bin/Activate.ps1
# Windows
# cmd.exe
# C:\> <venv>\Scripts\activate.bat
# PowerShell
# PS C:\> <venv>\Scripts\Activate.ps1

# Now your venv is activated, so any pip installs or other python commands will build into the path you supplied
# Lastly, when you are done, you can turn it off again with: "deactivate"

############################################################################################################
# BASIC LOGGING SETUP

import logging
LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
LOGGER.info("something")

############################################################################################################
# PRETTY PRINT STUFF

# Create a sample dictionary
data = {
    'name': 'John Doe',
    'age': 30,
    'city': 'Exampletown',
    'skills': ['Python', 'JavaScript', 'SQL']
}

# Use pprint to pretty print the dictionary
import pprint
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(data)

############################################################################################################
# AUTOMATICALLY ADD A KEY TO A DICT IF IT WASNT THERE

dict = {}
 
# This
if key in dict:
    dict.append(thing)
else:
    dict[key] = [thing]
 
# Can easily be replace by
dict.setdefault(key, []).append(thing)
 
OR

# This
if key in dict:
    dict.append(thing)
else:
    dict[key] = {"thing": "value"}
x.setdefault("parent", {})["thing"] = "value"