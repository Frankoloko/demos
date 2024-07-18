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

# Or go up many parents
parent_path = file_path.parent.parent.parent
parent_path = file_path.parents[2]