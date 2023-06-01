from pxr import Sdf

###############################################################################
# READ A CURRENT USD FILE

PATH = "/hosts/mtlws844/user_data/DNEG/dev/model-assembly-bundler/export.usda"

# Read the stage/layer?
layer = Sdf.Layer.FindOrOpen(PATH)

# Get a certain prim/primspec
primspec = layer.GetPrimAtPath("/cube")

###############################################################################
# CREATE A NEW USD FILE

# Create an empty layer
layer = Sdf.Layer.CreateAnonymous()

# Add/ccCreate a prim
primspec = Sdf.CreatePrimInLayer(layer, Sdf.Path("/Asset"))

# Export the file
path_to_file = '/hosts/mtlws844/user_data/DNEG/dev/model-assembly-bundler/export.usda'
layer.Export(path_to_file)

###############################################################################

x = Sdf.Path('/first/second/third').GetPrefixes()
print(x)
# [Sdf.Path('/first'), Sdf.Path('/first/second'), Sdf.Path('/first/second/third')]