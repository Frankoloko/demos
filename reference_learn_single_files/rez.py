# List the current loaded packages
rez env

# Create an environment
rez env python-3.7 some_package-1.0.0

# Graph the current environment
# Note that here you would need "graphviz" in your environment already
rez context --graph