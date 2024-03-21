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

############################################################################################################
# pathlib Path

from pathlib import Path

# Create a Path object representing a file
file_path = Path("/path/to/your/file.txt")

# Create a Path object representing a directory
directory_path = Path("/path/to/your/directory")

# Checking if a Path exists:
if file_path.exists():
    print("File exists!")
else:
    print("File does not exist!")

# Checking if a Path is a file or directory:
if file_path.is_file():
    print("It's a file!")
elif file_path.is_dir():
    print("It's a directory!")

# Iterating over files in a directory (see note below!)
for file_path in directory_path.iterdir():
    print(file_path)
# Note with this you need to change it into a list if you wanted to do list stuff
file_paths = list(directory_path.iterdir())
print(len(file_paths)) # len would break otherwise

# Getting the parent directory of a file:
parent_directory = file_path.parent
print("Parent directory:", parent_directory)

# Joining paths (I don't suggest using this method! It's hella weird to read)
sub_directory = directory_path.joinpath("subdir")
print("Subdirectory path:", sub_directory)

# Getting the file name:
file_name = file_path.name # With the extension/file type
file_name = file_path.stem # Without the extension/file type
file_extension = file_path.suffix # File extension alone

# Checking if a file matches a pattern:
pattern = "*.txt"
if file_path.match(pattern):
    print("File matches pattern!")

# Reading contents of a file:
file_content = file_path.read_text()
print("File content:", file_content)

# Writing contents to a file:
file_path.write_text("Hello, world!")

# Appending contents to a file:
file_path.write_text("More content", mode="a")

# Go one folder up (this give you the full path of the parent)
parent_path = file_path.parent