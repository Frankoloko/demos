# See my file "understanding_usd.md"

###############################################################################

# Key Concepts and Terms in USD
# USD (Universal Scene Description): An open-source file format and system that allows artists to interchange assets between different software while preserving complex scene hierarchies and attributes.
# Layering: USD supports the layering of multiple files. Layers can be combined to form a single, coherent scene, allowing different departments to work on separate aspects of the same shot.
# Composition: The process of combining multiple layers into a single scene. Composition arcs are relationships that control how layers are combined.
# Prims (Primitives): The basic building blocks in USD. Prims can represent geometric objects, lights, cameras, etc. Each prim has attributes and relationships that define its properties and connections to other prims.
# Attributes: Properties assigned to prims, such as position, rotation, color, etc. Attributes can be animated and vary over time.
# Schema: A USD schema defines a set of attributes and behaviors for a specific type of prim. For example, a UsdGeomMesh schema defines a prim type for polygonal meshes.
# Stage: The primary object for manipulating and querying USD data. A stage holds a collection of layers and provides an API to access the scene graph.
# Variants: USD allows for different variations of an asset within a single file, enabling artists to switch between different versions of a model or animation.
# References: A way to reference external USD files within another USD file. This helps in managing large scenes by modularizing them.
# Instancing: USD supports instancing to optimize memory and performance. Instances are copies of a prim that share the same underlying data but can have unique transformations.
# Overrides: Changes applied to referenced or inherited data. Overrides allow customization without altering the original data.
# Value Clips: A mechanism to efficiently handle time-sampled data for animation, allowing smooth interpolation between keyframes.
# Hydra: The rendering engine within USD, designed for high-performance drawing of USD data. It supports various renderers and can handle large, complex scenes interactively.
# Omniverse: NVIDIA’s platform for collaborative 3D production, which leverages USD for real-time simulation and rendering.
# Serialization: The process of converting USD data structures into a format that can be written to a file and later reconstructed.
# Understanding USD in Animation Pipeline
# Asset Creation: Artists create assets (models, textures, rigs) and save them as USD files. USD's non-destructive editing capabilities allow for easy updates and iterations.
# Scene Assembly: Assets are assembled into a scene using composition, layering, and referencing. Different departments (modeling, rigging, layout, animation, lighting) work simultaneously on the same shot.
# Animation: Animators work on USD stages, animating characters and objects. They can use value clips and overrides to manage different animation states and versions.
# Lighting and Shading: Lighters use USD to import assets and set up lights and materials. They can take advantage of Hydra for interactive previews.
# Rendering: Final scenes are rendered using renderers that support USD, such as Pixar’s RenderMan or NVIDIA’s Omniverse.

# Key Tools and Libraries
# USDView: A tool for viewing and debugging USD files.
# USD Libraries: A set of C++ and Python libraries for working with USD files, enabling custom tools and pipeline integration.
# USDZ: A file format for sharing USD assets in a single, portable archive, often used for AR applications.
# Example Workflow
# Modeling: Create a model in Maya or Blender and export as USD.
# Rigging: Rig the model in a rigging software, exporting the rigged model as another USD layer.
# Animation: Animate the rigged model in an animation software, saving animation data as additional USD layers.
# Scene Assembly: Use USD to assemble the scene, combining models, rigs, and animations.
# Lighting and Rendering: Set up lighting and materials, and render the final scene using a USD-compatible renderer.
# Learning Resources
# Pixar's USD Documentation: Comprehensive documentation and tutorials.
# NVIDIA Omniverse: Tutorials and examples on using USD in a collaborative environment.
# OpenUSD: The official repository and community for USD development and resources.
# By understanding these concepts and how they fit into the animation pipeline, you'll be well-prepared for your interview as a pipeline developer for animation using USD.

###############################################################################

# Honestly the best way to work with usd is to just use the what_is_this script
# and find the functions you might need
import sys
sys.path.append('/hosts/user_data/dev/what_is_this')
from what_is_this import what_is_this
what_is_this("my_var", my_var)

###############################################################################
from pxr import Sdf

###############################################################################
# READ A CURRENT USD FILE

PATH = "/hosts/user_data/dev/export.usda"

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

# Save / Export the file
path_to_file = '/hosts/dev/export.usda'
layer.Export(path_to_file)

###############################################################################
# SOME PATH SPLITTING THING

x = Sdf.Path('/first/second/third').GetPrefixes()
print(x)
# [Sdf.Path('/first'), Sdf.Path('/first/second'), Sdf.Path('/first/second/third')]

###############################################################################
# CHECKING PROPERTY/ATTRIBUTE VALUES (IN HOUDINI)

import hou
node = hou.node('/stage/x')
layer_active = node.activeLayer()
prim = layer_active.GetPrimAtPath("/HoudiniLayerInfo")

print(prim.properties)
print(prim.properties['the_key'])
print(prim.properties['the_key'].default)

###############################################################################
# SDF VS USD
# Note that this is for Houdini (the first lines)

# USD
stage = node.editableStage() # Note that here we get the stage
prim = stage.GetPrimAtPath("/HoudiniLayerInfo")
attribute = prim.CreateAttribute(
    "key_name",
    Sdf.ValueTypeNames.String
)
attribute.Set("some_value")

# Sdf
layer = node.editableLayer() # Note that here we get the layer
Sdf.JustCreatePrimAttributeInLayer(
    layer=layer,
    attrPath="/HoudiniLayerInfo.key_name",
    typeName=Sdf.ValueTypeNames.String,
    variability=Sdf.VariabilityUniform,
    isCustom=True
)
attr = layer.GetPrimAtPath("/HoudiniLayerInfo").GetAttributeAtPath("key_name")
attr.default = "some_value"

# But why would you use the one over the other?

# Good question. In general, SDF is the "lower level (strong)" language while
# USD is built on top of SDF. So USD has extra error checking and easier functions

# In general, Usd is higher-level API. As a result, it has better type-checking /
# error handling and it is generally more convenient to write. Since it operates
# on the composed stage, it is generally better at handling traversals because it
# can ignore unused scene description such as unselected variants. However, because
# it operates across many layers at once, it can be harder to know what you are actually
# authoring. For instance if I try to author an attribute using the Usd APIs, I won’t
# necessarily know whether it is defining or overriding a prim to hold the attribute.
# Also, when querying whether an attribute exists, Usd won’t give you any indication
# as to what layer it is in.

# With Sdf, it is more like editing a text document. You have the highest level of
# control over what the scene description actually looks like since you are engaging
# with a specific layer rather than an entire stage. Since it doesn’t need to look at
# multiple layers, it is often significantly faster for authoring scene description.
# However, because it is lower-level you lose access to many of the provided APIs
# making it somewhat riskier. For example, when authoring a primvar you need to use
# the primvars namespace. With Sdf, you would be much more likely to accidentally use
# primvar instead since you don’t have access to the PrimvarsAPI.

# ANOTHER EXAMPLE OF SDF VS USD

usd_stage = Usd.Stage.Open('/u/fkru/Desktop/new_stagexxx.usd')
print(usd_stage) # Usd.Stage.Open(rootLayer=Sdf.Find('/u/fkru/D...
usd_prim = usd_stage.DefinePrim('/UnTypedPrim')
print(usd_prim) # Usd.Prim(</UnTypedPrim>)

sdf_layer = node.editableLayer()
print(sdf_layer) # Sdf.Find('anon:0x7f7cb1ab0c00:LOP:/stage/pythonscript3')
sdf_prim = Sdf.CreatePrimInLayer(sdf_layer, Sdf.Path("/test"))
print(sdf_prim) # Sdf.Find('anon:0x7f7cb1ab0c00:LOP:/stage/pythonscript3', '/test')

###############################################################################
# CREATING A PRIM

new_prim_path = Sdf.Path("{}/{}".format(root_prim_path, root_prim))
primspec = Sdf.CreatePrimInLayer(layer, new_prim_path)
# You need to set a lot of default types otherwise the prim is just
# a useless "over" or something
primspec.specifier = pxr.Sdf.SpecifierDef
primspec.typeName = "Xform"
primspec.kind = pxr.Kind.Tokens.component

###############################################################################
# ADD A PAYLOAD TO A PRIMSPEC

new_prim_path = Sdf.Path("{}/{}".format(root_prim_path, root_prim))
primspec = Sdf.CreatePrimInLayer(layer, new_prim_path)
primspec.payloadList.Add(Sdf.Payload(element.uri))

###############################################################################
# REMOVING/DELETING A PRIM

# USD method
stage = Usd.Stage.Open(layer)
stage.RemovePrim(primspec.path)

###############################################################################
# HOUDINI USD PYTHON LOP

# From my understanding, you can only EDIT usd related things from with a Python LOP in Houdini
import hou
from pxr import Sdf
node = hou.pwd()

# There are two ways to get the stage/layer to work with
stage = node.editableStage()
layer = node.editableLayer()
# NOTE: YOU CANNOT USE BOTH IN THE SAME SCRIPT. The second one will always be None.
# https://www.sidefx.com/docs/houdini/hom/hou/LopNode.html
# editableStage: Returns a pxr.Usd.Stage object with permission to edit that represents the USD stage input to a Python LOP.
# editableLayer: Returns a pxr.Sdf.Layer object with permission to edit that represents the active layer in a Python LOP.

# These I haven't see used much. A note, you cannot query the node you are currently on or nodes below. You can only query nodes above or on other network branches.
# https://www.sidefx.com/docs/houdini/hom/hou/LopNode.html
layer = node.activeLayer()
print(layer) # Sdf.Find('anon:0x7fcae4be8d00:LOP')
# activeLayer :Returns a pxr.Sdf.Layer object representing the USD layer that has been modified by this node.
stage = node.stage()
print(stage) # Usd.Stage.Open(rootLayer=Sdf.Find('anon...
# stage: Returns a pxr.Usd.Stage object representing the USD stage output from this node.

# Note the result of these two ways of getting the layer
stage = node.editableStage()
layer = stage.GetRootLayer()
print(layer) # Sdf.Find('anon:0x7ff164fba400:LOP:rootlayer')
layer = node.editableLayer()
print(layer) # Sdf.Find('anon:0x7ff16645a800:LOP:/stage/pythonscript1')
# But they are actually the same thing
# print(Sdf.Find('anon:0x7ff164fba400:LOP:rootlayer') == Sdf.Find('anon:0x7ff16645a800:LOP:/stage/pythonscript1'))
# NOTE: I think they are both None haha, that's why they are equal

# In Houdini, not sure about others, the stage and layer are both SDFs

###############################################################################
# PRIM
# https://openusd.org/release/api/class_usd_prim.html

# Get a prim from the stage
prim = stage.GetPrimAtPath("/MyPrim")

# Get the default prim of the stage
prim = stage.GetDefaultPrim()

# Set the defaultPrim (Houdini snippet)
node = hou.pwd()
stage = node.editableStage()
layer = stage.GetEditTarget().GetLayer()
layer.defaultPrim = "Asset"

print(prim.GetName()) # prints "Prim"
print(prim.GetPrimPath()) # prints "/Prim"

# Create a new prim (without setting the Type)
prim = stage.DefinePrim('/UnTypedPrim')
print(prim) # Usd.Prim(</UnTypedPrim>)

# Create a new prim and set the Type. Two methods:
stage.DefinePrim('/XformPrim', 'Xform')
xform = UsdGeom.Xform(prim)
# OR
xform = UsdGeom.Xform.Define(stage, '/XformPrim')

# Remove a prim
stage.RemovePrim('/MyPrim')

# After removing a prim, your previous variables holding the prim will still point to something
# So use this to check if the pointer is still valid
prim.IsValid()

# Get the children prims of a prim
prim.GetChildren()

###############################################################################
# VARIANTS

# Get variants from sdf primspec
for item in dict(primspec.variantSets):
    print(item)

prim = stage.DefinePrim('/XformPrim')
for variant in ["one", "two", "three"]:
    varset = prim.GetVariantSets().AddVariantSet(variant)

# More advanced example of setting variants and stuff
prim = stage.DefinePrim("/Asset", "Xform")

for variant in ["one", "two", "three"]:
    varset = prim.GetVariantSets().AddVariantSet(variant)

    for colour in colour_info: # Ignoring this
        varset.AddVariant("red")
        varset.SetVariantSelection("red")
        with varset.GetVariantEditContext():
            target_prim = stage.DefinePrim(
                "/Asset/x{}".format(colour["active_stemtips"]), "Xform"
            )
            primvars_api = UsdGeom.PrimvarsAPI(target_prim)
            color_primvar = primvars_api.CreatePrimvar(
                "cpal:{}".format(variant),
                Sdf.ValueTypeNames.Float3,
                UsdGeom.Tokens.constant,
            )
            color_primvar.Set((0.3064955472946167, 1.0, 1.0))

varset.ClearVariantSelection()

#######

prim.GetVariantSets().GetAllVariantSelections()

# Get variant sets
# And set their values
prim.GetVariantSet("texture_default").SetVariantSelection("0")
prim.GetVariantSet("preview_look").SetVariantSelection("default")
prim.GetVariantSet("geo").SetVariantSelection("0")
prim.GetVariantSet("look").SetVariantSelection("0")
prim.GetVariantSet("lod").SetVariantSelection("300")

#### Get variant sets, variant names and attribute/properties/values

layer = Sdf.Layer.FindOrOpen(usd_file)
prim = layer.GetPrimAtPath("/Asset")
variant_sets = []
variant_names_and_values = {}

# Get the variant sets, variant names, and variant values
for variant_set in prim.variantSets:
    variant_sets.append(variant_set.name)
    for variant in variant_set.variantList:
        for attr in variant.primSpec.attributes:
            if attr.name == "primvar:thing:value":
                if variant.name not in variant_names_and_values:
                    variant_names_and_values[variant.name] = attr.default

####

# Getting attribute values with path with variants
layer.GetAttributeAtPath(Sdf.Path("/Asset{primaryColor=0}.primvars:cpal:primaryColor")).default

###############################################################################
# CUSTOM LAYER DATA

# Setting
layer.customLayerData = {"anything": "like this"}

# Reading
layer.customLayerData

###############################################################################
# CUSTOM LAYER DATA

import hou
node = hou.node('/stage/mynode')
layer = node.activeLayer()
prim = layer.GetPrimAtPath("/Asset/geo")
variantList = prim.variantSets["my_variant_set"].variantList
prim_variant_0 = layer.GetPrimAtPath("{}test".format(variantList[0].path))
print(prim_variant_0.relationships["material:binding:preview"].targetPathList.GetAddedOrExplicitItems()[0])

###############################################################################
# MOVE/REPARENT PRIM

edit = Sdf.BatchNamespaceEdit()
edit.Add(current_prim_path, new_prim_path)
layer = Sdf.Layer.FindOrOpen(usd_file)
layer.Apply(edit)
# More info here
# https://github.com/ColinKennedy/USD-Cookbook/blob/master/features/batch_namespace_edit/python/batch_namespace_edit.py