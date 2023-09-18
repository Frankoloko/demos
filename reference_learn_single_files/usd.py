# https://openusd.org/release/api/index.html
# https://developer.nvidia.com/usd/tutorials

# General Classes:
# Usd.Stage: Represents a USD stage, which is a container for organizing and authoring a scene. It provides functions for creating, loading, and saving USD files.
# Usd.Stage.Load: Loads a USD file into a stage.
# Usd.Stage.GetRootLayer: Returns the root layer of a stage, which represents the composition of all layers in the scene.
# Usd.Stage.DefinePrim: Defines a new prim (object) in the scene. Prims can represent various entities such as geometry, lights, or cameras.
# Usd.Prim.GetPrimAtPath: Retrieves a prim from the stage using its path.
# Usd.Prim.CreateAttribute: Creates a new attribute on a prim.
# Usd.Attribute.Set: Sets the value of an attribute.
# Usd.Attribute.Get: Retrieves the value of an attribute.
# Usd.Stage.GetPrimAtPath: Retrieves a prim from the stage using its path.
# Usd.Stage.GetRootLayer: Returns the root layer of a stage.
# Usd.Stage.GetSessionLayer: Returns the session layer of a stage. The session layer is used for temporary changes that do not persist when the stage is saved.
# Usd.Stage.Reload: Reloads the stage from disk, discarding any unsaved changes.
# Usd.Stage.Save: Saves the stage to disk.

from pxr import Usd, UsdGeom, Sdf, UsdUtils

# -------------------------------------------------------------------------------------------------------
# STAGE
# https://openusd.org/release/api/class_usd_stage.html

# Create a new stage
# Note that you can only run this if the file doesn't exist
# If you don't give a full path, it will add this file to your computer's temp location
# So the below would become something like /temp/francois/new_stage.usd
# You can set the file type like usd, usda, usdc etc
stage = Usd.Stage.CreateNew('new_stage.usd')

# If the file exists, you have to open it
stage = Usd.Stage.Open('a_usda_file.usda')

print(stage) # Everything below is part of this single print
# Usd.Stage.Open(rootLayer=Sdf.Find('/u/fkru/new_stage.usd'),
# sessionLayer=Sdf.Find('anon:0x3851f420:new_stage-session.usda'),
# pathResolverContext=<dneg_usd_assetresolver._dneg_usd_assetresolver_py.DnegArResolverContext object at 0x7f2b806f3b18>)

# Save over original file
stage = Usd.Stage.Open('a_usda_file.usda')
# do something to the stage
stage.Save() # I think this will change the original file also if you used Open

# Export to new file
stage = Usd.Stage.Open('a_usda_file.usda')
# do something to the stage
stage.Export('a_usdc_file.usdc')

# Reload the original file (I think, haven't tested it, remove this if you have tested it)
stage.Reload()

# Get the root layer
# Not yet super sure what that is exactly
layer = stage.GetRootLayer()



# -------------------------------------------------------------------------------------------------------
# ATTRIBUTE
# https://openusd.org/release/api/class_sdf_property_spec.html ???

attribute = prim.GetAttribute('purpose')

print(attribute)
# Usd.Prim(</XformPrim>).GetAttribute('purpose')

# Get and Set the attribute values
attribute.Get()
attribute.Set("Something")

# Create a new attribute
prim.CreateAttribute("Attribute_Name", type)

# Get all attributes on the prim
attributes = prim.GetAttributes()

# Iterate over the attributes and print their names
for attribute in attributes:
    print(attribute.GetName())

# -------------------------------------------------------------------------------------------------------
# Layer

layer = stage.GetRootLayer()

# This brings back a usda type string
string = layer.ExportToString()


# -------------------------------------------------------------------------------------------------------
# SDF.LAYER

# Create an empty layer
layer = Sdf.Layer.CreateAnonymous()

# Open a usd Layer/Stage (not sure which one)
layer = Sdf.Layer.FindOrOpen("some/path.usda")

# Get a Prim
prim = layer.GetPrimAtPath("/cube")

# Add/Create a prim
prim = Sdf.CreatePrimInLayer(layer, Sdf.Path("/Asset"))

# Export the layer to a new file
layer.Export("some/new/path.usd")

# -------------------------------------------------------------------------------------------------------
# Explaining layers and edit targets

# Example of taking two layers and then opening a stage from them
# I'm not sure if this is only the root & session, or if it is just layer1 and layer2 (meaning you can just add more if you want)
root = Sdf.Layer.CreateAnonymous()
session = Sdf.Layer.CreateAnonymous()
stage = Usd.Stage.Open(root, session) # The first one here will be the EditContext by default

stage.GetEditTarget().GetLayer() == root # True
stage.GetEditTarget().GetLayer() == session # False

# Change the edit target
stage.SetEditTarget(session)

# Add a new layer to root
# What I find interesting here is that it adds it to root. I would expect to add it to stage or something.
root.subLayerPaths.append("/some/place/cube.usda")
external_layer = Sdf.Layer.Find("/some/place/cube.usda")
stage.SetEditTarget(external_layer)
stage.GetEditTarget().GetLayer() == root # False
stage.GetEditTarget().GetLayer() == session # False

# -------------------------------------------------------------------------------------------------------
# Sdf Prefixes

prefixes = Sdf.Path('/first/second/third').GetPrefixes()
print(prefixes)
# [Sdf.Path('/first'), Sdf.Path('/first/second'), Sdf.Path('/first/second/third')]

# -------------------------------------------------------------------------------------------------------
# Cache stuff

cache = UsdUtils.StageCache.Get()
stage_id = cache.Insert(stage)

print(stage_id) # <pxr.Usd.Id at 0x7f7c980c4520>
print(stage_id.ToString()) # '9223001'

stage_id = Usd.StageCache.Id.FromString('9223001')
result = cache.Find(stage_id)
print(result) # Prints all of the below
# Usd.Stage.Open(
# rootLayer=Sdf.Find('anon:0x1765290'),
# sessionLayer=Sdf.Find('anon:0x173baa0'),
# pathResolverContext=<dneg_usd_assetresolver._dneg_usd_assetresolver_py.DnegArResolverContext object at 0x7f7c980d5140>)

with Usd.StageCacheContext(cache):
    stage = Usd.Stage.Open("/jobs/FOOD/ASSET/pipetest/prop/cube/ivy/sprst/SPRST_pipetest_prop_cube_v287/cube.usda")

print(stage)
# Usd.Stage.Open(
# rootLayer=Sdf.Find('/jobs/FOOD/ASSET/pipetest/prop/cube/ivy/sprst/SPRST_pipetest_prop_cube_v287/cube.usda'),
# sessionLayer=Sdf.Find('anon:0x2b44760:cube-session.usda'),
# pathResolverContext=<dneg_usd_assetresolver._dneg_usd_assetresolver_py.DnegArResolverContext object at 0x7f7c980d5140>)

cache.Contains(stage) # True