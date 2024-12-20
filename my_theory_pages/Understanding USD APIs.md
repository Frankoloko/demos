# Understanding USD APIs

The goal of this document is to explain USD in terms of Python code. It is meant to be read from top to bottom, but it is also designed to work by using Ctrl+F to search for terms you might need help with.

## Importing/Imports

All of the examples will be using these imports. You can install these packages with `pip install usd-core`

```python
from pxr import Usd, UsdGeom, Sdf
```

## Usdview

You will use `usdview` a lot. It is an application, like Maya/Houdini, that allows you to view USD files. Currently you still need to compile your own version of the exe. But you can also download pre-compiled versions like from here: https://developer.nvidia.com/usd

You know you have it set up correctly if you can run `usdview` in your terminal and it errors out with information about the program. It will error out because you actually need to supply a file to open like `usdview /some/file.usd`

## Good resources

* A chatbot designed to help with USD things. Be warned it still makes mistakes and lies about functions and classes: https://build.nvidia.com/nvidia/usdcode-llama3-70b-instruct?snippet_tab=Python
* A lot of useful snippets: https://github.com/ColinKennedy/USD-Cookbook
* The official documentation page: https://openusd.org/docs/api/usd_page_front.html
* At the end of the day, the source code is worth a lot: https://github.com/PixarAnimationStudios/OpenUSD

# Useful class links

You don't need to go through this now but it would be useful later on

* `Usd.Stage`: https://openusd.org/docs/api/class_usd_stage.html
* `Sdf.Layer`: https://openusd.org/docs/api/class_sdf_layer.html
* `Usd.Prim`: https://openusd.org/docs/api/class_usd_prim.html
* `Sdf.Path`: https://openusd.org/docs/api/class_sdf_path.html

## First example of creating a stage

```python
# Create a new USD file
stage = Usd.Stage.CreateNew('HelloWorld.usda')

# Create a xForm prim
xformPrim = UsdGeom.Xform.Define(stage, '/hello')

# Create an Sphere prim
spherePrim = UsdGeom.Sphere.Define(stage, '/hello/world')

# Save your changes
stage.Save()
```

Test this by opening the file you have just created in usdview with `usdview /your/file.usda`. This is what the stage will look like.

```
#usda 1.0

def Xform "hello"
{
    def Sphere "world"
    {
    }
}
```

Note that for all following `usda` snippets I paste here, I will remove the `#usda 1.0` part, but it is technically always present in the file.


## Exporting/Saving your work

In general, when testing, it is useful to save the changes you have made to a file that you can view in text editor or in `usdview`. There are many ways to do this, here are a few examples.

```python
# Create the stage in memory and then export it
stage = Usd.Stage.CreateInMemory()
...
stage.Export("HelloWorld.usda")

# Create the stage in a file and save the changes
stage = Usd.Stage.CreateNew('HelloWorld.usda')
...
stage.Save()

# Save the layer
stage = Usd.Stage.CreateNew('HelloWorld.usda')
...
layer = stage.GetRootLayer()
layer.Save()

# Open the layer with Sdf
layer = Sdf.Layer.FindOrOpen(path)
...
layer.Save()
```

## Anonymous files

You are able to create Anonymous layers & files. These are files that only exist in memory, and cannot get saved to disk.

```python
layer = Sdf.Layer.CreateAnonymous(path)
primspec = Sdf.CreatePrimInLayer(layer, Sdf.Path("/Asset"))
layer.Save()  # This would Error out saying you cannot save an anonymous layer
```

## Different ways to define prims

Notice how these two ways of creating prims are NOT the same.

```python
test_1 = UsdGeom.Xform.Define(stage, '/test_1')
print(test_1)
# UsdGeom.Xform(Usd.Prim(</test_1>))
# https://openusd.org/docs/api/usd_geom_page_front.html

test_2 = stage.DefinePrim("/test_2", 'Xform')
print(test_2)
# Usd.Prim(</test_2>)
# https://openusd.org/docs/api/class_usd_prim.html

# But when you get the prim of the UsdGeom, they are the same
print(test_1.GetPrim())
# Usd.Prim(</test_1>)
```

That said, the resulting stage looks the same in both cases.

```
def Xform "test_2"
{
}
```

## Create attributes

Attributes always need to go on a prim.

```python
# Create the attribute
attr = xform_prim.CreateAttribute("myAttr", Sdf.ValueTypeNames.Float)

# Another way to create an attribute
property_name = "myAttr"
property_type = Sdf.ValueTypeNames.Float
attr = xform_prim.CreateAttribute(property_name, property_type)

# Set a value on the attribute
attr.Set(1.0)
```

Notice how the attributes are placed in the `{}` of the prim.

```
def Xform "test_2"
{
    custom float myAttr = 1
}
```

You can also get/find an already existing attribute with

```python
found_attr = prim.GetAttribute(attr_name)
# Note that even if the attribute was not found, it will NOT error out
# So you need to check "if found_attr" to make sure something was found
```

## Create relationships

```python
# Define a new prim with a relationship
prim = stage.DefinePrim('/MyPrim', 'Xform')
relationship = prim.CreateRelationship('myRelationship')

# Create a target prim for the relationship
spherePrim = UsdGeom.Sphere.Define(stage, '/TargetPrim')

# Set the target of the relationship to the target prim
relationship.AddTarget(spherePrim.GetPath())
```

```
def Xform "MyPrim"
{
    custom rel myRelationship
    prepend rel myRelationship = </TargetPrim>
}

def Xform "TargetPrim"
{
}
```

Note that this does not technically do anything visible in the scene. You will NOT see two spheres is my point. All you are doing here is connecting the variable `myRelationship` to point to another prim. But other than that nothing is really happening. That said, this is obviously useful when, for example, you need to point to materials or shaders that might interact with the prim in some ways.

## Attributes vs Properties

Properties are a collective term that refers to either Attributes or Relationships. Attributes have an exact value where as Relationships merely point to another value.

## Set metadata

Note that a metadata key needs to be pre-registered before using it. You cannot just add any type of metadata. You can add new metadatas to your usd setup by creating `.json` files that list then. Then you load that `.json` file into your USD with an ENV variable. See more here: https://github.com/ColinKennedy/USD-Cookbook/tree/master/plugins/plugin_metadata

```python
prim = stage.DefinePrim("/MyPrim", "Xform")
prim.SetMetadata("comment", "I am a comment")  # This will work
prim.SetMetadata("something", "I am a something")  # This will error out
```

```
def Xform "MyPrim" (
    "I am a comment"
)
{
}
```

Note that metadata goes into the `()` section of a prim.

## Create variants sets and variants

```python
spherePrim = UsdGeom.Sphere.Define(stage, '/Sphere')

# Create a variant set on the prim if it doesn't exist
variantSet = spherePrim.GetPrim().GetVariantSets().AddVariantSet('modelingVariant')

# Create, set and edit the small variant set
variantSet.AddVariant('small')
variantSet.SetVariantSelection('small')
with variantSet.GetVariantEditContext():
    # Authoring changes that will only affect the 'small' variant of the sphere
    smallSphere = UsdGeom.Sphere(spherePrim.GetPrim())
    smallSphere.GetRadiusAttr().Set(1.0)

# Create, set and edit the large variant set
variantSet.AddVariant('large')
variantSet.SetVariantSelection('large')
with variantSet.GetVariantEditContext():
    # Authoring changes that will only affect the 'large' variant of the sphere
    largeSphere = UsdGeom.Sphere(spherePrim.GetPrim())
    largeSphere.GetRadiusAttr().Set(2.0)
```

```
def Sphere "Sphere" (
    variants = {
        string modelingVariant = "large"
    }
    prepend variantSets = "modelingVariant"
)
{
    variantSet "modelingVariant" = {
        "large" {
            double radius = 2

        }
        "small" {
            double radius = 1

        }
    }
}
```

Notice how the `variants` and `variantSets` are a type of `metadata`. But for some reason, you cannot set the value like `spherePrim.GetPrim().SetMetadata("variantSets", "small")`.

Notice how `large` is the last-set variant set. This is a result of us calling `variantSet.SetVariantSelection('large')` last. You could have cleared the variant set by doing `variantSet.SetVariantSelection('')` which would completely remove that `variant` metadata section from your prim.

## Create layers

```python
stage = Usd.Stage.CreateNew(r"D:\all_francois\git_repos\demos\HelloWorld.usda")
root_layer = stage.GetRootLayer()

# Create multiple new sublayers.
sub_layer_1 = Sdf.Layer.CreateAnonymous(r"D:\all_francois\git_repos\demos\HelloWorld_1.usda")
sub_layer_2 = Sdf.Layer.CreateAnonymous(r"D:\all_francois\git_repos\demos\HelloWorld_2.usda")
sub_layer_3 = Sdf.Layer.CreateAnonymous(r"D:\all_francois\git_repos\demos\HelloWorld_3.usda")

# Add the sublayers to the root layer by setting their identifiers in the subLayerPaths list.
root_layer.subLayerPaths.append(sub_layer_1.identifier)
root_layer.subLayerPaths.append(sub_layer_2.identifier)
root_layer.subLayerPaths.append(sub_layer_3.identifier)

# Save your changes
stage.Save()
```

## Change prim paths / Reparent prims

```python
edit = Sdf.BatchNamespaceEdit()
edit.Add("/current/prim/path", "/new/prim/path")
layer = Sdf.Layer.FindOrOpen(usd_file)

# Note that if these edits would not work, you would not even know.
# Everything will execute without errors.
# So you can check the success first with
print(layer.CanApply(edit))

layer.Apply(edit)  # Note that this does not save out the file changes at all. You still need layer.Save() or something.
```

## Compare Two Usd Files

I don't know if a better method exists, but for now this is the best I know of. Please update if you find anything better.

```python
def usd_contents_match(file_one, file_two):
    """Compared two USD files.

    Args:
        file_one(string): The path to the file
        file_two(string): The path to the file
    """
    with open(file_one, 'r') as file1, open(file_two, 'r') as file2:
        file1_contexts = file1.read()
        file2_contexts = file2.read()

        # A pattern to match this part of the usda:
        # doc """..."""
        # We don't care about the doc metadata matching. We only care about the stage
        # being the same.
        doc_metadata_pattern = r'(doc = """)([\s\S]*?)(""")'

        file1_cleaned = re.sub(doc_metadata_pattern, "", file1_contexts)
        file2_cleaned = re.sub(doc_metadata_pattern, "", file2_contexts)
        return file1_cleaned == file2_cleaned
```

## RuntimeError: Accessed

If you ever get an error like `RuntimeError: Accessed <pxr.Usd.Object object at 0x0000000003E1FA48>` then it is possible that you are interacting with something that is invalid. Check it with `print(prim.IsValid())`.

## Connections

Take this usda as an example
```
def Shader "test"
{
    float inputs:input.connect = </another.outputs:b>
}
```

Here are some results for connection information off of that file

```python
from pxr import Usd
stage = Usd.Stage.Open(r"...the_file.usda")
prim = stage.GetPrimAtPath("/test")
for attribute in prim.GetAttributes():
    for connection in attribute.GetConnections():
        print(type(connection)) # <class 'pxr.Sdf.Path'>
        print(connection) # /another.outputs:b
        print(connection.pathString) # /another.outputs:b
        print(connection.GetPrimPath()) # /another     
```

# Classes Section

# Usd.Stage

https://openusd.org/docs/api/class_usd_stage.html

```python
# Importing the necessary modules
from pxr import Usd

# Creating and Opening Stages
stage = Usd.Stage.CreateNew("new_stage.usda")    # Create a new stage
stage = Usd.Stage.Open("existing_stage.usda")    # Open an existing stage
stage = Usd.Stage.CreateInMemory()               # Create a stage in memory

# Accessing Stage Metadata
stage.GetRootLayer()          # Get the root layer of the stage
stage.GetSessionLayer()       # Get the session layer
stage.GetDefaultPrim()        # Get the default prim (if set)
stage.SetDefaultPrim(prim)    # Set the default prim
stage.GetPrimAtPath("/path")  # Get the prim at a specific path

# Modifying the Stage
stage.DefinePrim("/path/to/prim", "Xform")   # Define a new prim of type Xform
stage.OverridePrim("/path/to/prim")          # Create an override for a prim
stage.RemovePrim("/path/to/prim")            # Remove a prim

# Iterating Over Prims
for prim in stage.Traverse():                # Traverse all prims in stage
    print(prim.GetPath())

# Saving the Stage
stage.Save()                 # Save the stage to its root layer file
stage.SaveSessionLayers()    # Save the session layer

# Editing Layers
layer_stack = stage.GetLayerStack()         # Get the list of layers composing the stage
edit_target = stage.GetEditTarget()         # Get the current edit target
stage.SetEditTarget(layer)                  # Set a layer as the edit target

# Managing Variants
prim = stage.GetPrimAtPath("/path/to/prim")
variant_sets = prim.GetVariantSets()          # Access the variant sets on a prim
variant_set = variant_sets.GetVariantSet("variantSetName")
variant_set.AddVariant("variantName")         # Add a variant
variant_set.SetVariantSelection("variantName")# Set the active variant

# Time Management
stage.GetStartTimeCode()      # Get the start time code of the stage
stage.GetEndTimeCode()        # Get the end time code of the stage
stage.SetStartTimeCode(0.0)   # Set the start time code
stage.SetEndTimeCode(24.0)    # Set the end time code

# Layer Offsets
layer_offset = stage.GetTimeCodesPerSecond()  # Get time scaling information
stage.SetTimeCodesPerSecond(24.0)             # Set time codes per second

# Other Utilities
stage.Flatten()                # Flatten the stage into a single layer
stage.Export("output.usda")    # Export the stage to a file
stage.Reload()                 # Reload all layers in the stage

# Debugging and Information
stage.GetPrimPaths()           # Get paths of all prims
stage.GetPopulationMask()      # Get the population mask
stage.SetPopulationMask(mask)  # Set the population mask
stage.ClearPopulationMask()    # Clear the population mask
stage.IsEditTargetLayerMuting()# Check if a layer is muted
stage.MuteLayer("layer_name")  # Mute a specific layer
stage.UnmuteLayer("layer_name")# Unmute a specific layer
```

# Usd.Layer

https://openusd.org/docs/api/class_sdf_layer.html

```python
# Importing the necessary modules
from pxr import Sdf, Usd

# Creating and Opening Layers
layer = Sdf.Layer.CreateNew("new_layer.usda")   # Create a new layer
layer = Sdf.Layer.FindOrOpen("existing_layer.usda")  # Find or open an existing layer
layer = Sdf.Layer.Find("existing_layer.usda")        # Find an already loaded layer

# Accessing Layer Information
print(layer.identifier)         # Get the layer's unique identifier (e.g., file path)
print(layer.realPath)           # Get the resolved file path
print(layer.version)            # Get the version of the layer
print(layer.comment)            # Get or set the comment string for the layer
layer.comment = "My custom comment"

# Managing Layer Content
layer.Save()                    # Save the layer to its file
layer.Export("output.usda")     # Export the layer to another file
layer.Reload(force=True)        # Reload the layer from its file, optionally forcing it

# Root Prims
print(layer.pseudoRoot)         # Get the root prim of the layer
print(layer.defaultPrim)        # Get the default prim
layer.defaultPrim = "RootPrim"  # Set the default prim

# Time Information
print(layer.startTimeCode)      # Get the start time code
print(layer.endTimeCode)        # Get the end time code
layer.startTimeCode = 0.0       # Set the start time code
layer.endTimeCode = 24.0        # Set the end time code
print(layer.timeCodesPerSecond) # Get the time codes per second
layer.timeCodesPerSecond = 24.0 # Set the time codes per second

# Metadata
print(layer.GetAllMetadata())   # Get all metadata as a dictionary
layer.SetMetadata("customKey", "customValue") # Set custom metadata
print(layer.GetMetadata("customKey"))         # Get specific metadata
layer.ClearMetadata("customKey")              # Remove specific metadata

# SubLayers
print(layer.subLayerPaths)      # Get the list of sub-layer paths
layer.subLayerPaths.append("sub_layer.usda")  # Add a sub-layer
layer.subLayerPaths.remove("sub_layer.usda")  # Remove a sub-layer
layer.subLayerPaths = ["layer1.usda", "layer2.usda"]  # Set all sub-layer paths

# Layer Offsets
offsets = layer.GetSubLayerOffset(0)          # Get the offset for a sub-layer
layer.SetSubLayerOffset(0, Sdf.LayerOffset(2, 0.5))  # Set a sub-layer offset
print(offsets.offset)                         # Time offset
print(offsets.scale)                          # Time scale

# Layer Muting
layer.IsMuted()                   # Check if the layer is muted
layer.SetMuted(True)              # Mute the layer
layer.SetMuted(False)             # Unmute the layer

# Debugging and Validation
print(layer.ExportToString())     # Export the layer's content to a string
layer.ExportToDotGraph("graph.dot")  # Export a DOT graph of the layer's contents
print(layer.Anonymize())          # Create an anonymous layer (useful for debugging)
print(layer.IsDirty())            # Check if the layer has unsaved changes
print(layer.IsAnonymous())        # Check if the layer is anonymous
print(layer.Validate())           # Validate the layer's contents (returns True/False)

# Flattening
flattened_layer = layer.Flatten() # Flatten the layer into a single layer

# Layer Composition Information
print(layer.GetPrimAtPath("/path"))           # Get a prim from the layer by path
print(layer.ListFields("/path"))             # List fields on a specified path
print(layer.Query("/path", "fieldName"))     # Query a specific field at a path
layer.SetField("/path", "fieldName", value)  # Set a field at a specific path
layer.ClearField("/path", "fieldName")       # Clear a field at a specific path
```

# Usd.Prim

https://openusd.org/docs/api/class_usd_prim.html

```python
# Importing the necessary modules
from pxr import Usd, Sdf, Gf

# Getting a Prim
stage = Usd.Stage.Open("stage.usda")
prim = stage.GetPrimAtPath("/path/to/prim")   # Get a prim by path
print(prim.IsValid())                         # Check if the prim is valid

# Accessing Prim Properties
print(prim.GetName())                         # Get the prim's name
print(prim.GetPath())                         # Get the prim's path as Sdf.Path
print(prim.GetTypeName())                     # Get the prim's type name
print(prim.IsActive())                        # Check if the prim is active
print(prim.IsLoaded())                        # Check if the prim is loaded
print(prim.IsModel())                         # Check if the prim is a model
print(prim.IsGroup())                         # Check if the prim is a group
print(prim.HasDefiningSpecifier())            # Check if the prim has a defining specifier
print(prim.GetSpecifier())                    # Get the prim's specifier (e.g., Def, Over)

# Setting Prim Properties
prim.SetActive(False)                         # Deactivate the prim
prim.SetSpecifier(Sdf.SpecifierDef)           # Set the prim's specifier
prim.SetTypeName("Xform")                     # Set the prim's type name

# Metadata
print(prim.GetAllMetadata())                  # Get all metadata as a dictionary
prim.SetMetadata("customKey", "customValue")  # Set custom metadata
print(prim.GetMetadata("customKey"))          # Get specific metadata
prim.ClearMetadata("customKey")               # Clear specific metadata

# Attributes
attributes = prim.GetAttributes()             # Get a list of attributes
attr = prim.GetAttribute("attrName")          # Get a specific attribute
for attr in attributes:                       # Iterate through attributes
    print(attr.GetName(), attr.Get())

# Relationships
relationships = prim.GetRelationships()       # Get a list of relationships
rel = prim.GetRelationship("relName")         # Get a specific relationship
for rel in relationships:                     # Iterate through relationships
    print(rel.GetName())

# Children and Hierarchy
children = prim.GetChildren()                 # Get direct children
descendants = prim.GetDescendants()           # Get all descendants
parent = prim.GetParent()                     # Get the parent prim
for child in children:                        # Iterate through child prims
    print(child.GetPath())

# Variants
variant_sets = prim.GetVariantSets()          # Access the variant sets
variant_set = variant_sets.GetVariantSet("variantSetName")
variant_set.AddVariant("variantName")         # Add a variant
variant_set.SetVariantSelection("variantName")# Set the active variant

# Composition
print(prim.HasAuthoredReferences())           # Check if the prim has references
references = prim.GetReferences()             # Get the references object
references.AddReference("referenced.usda")    # Add a reference
references.ClearReferences()                  # Clear all references

# Payloads
print(prim.HasAuthoredPayloads())             # Check if the prim has payloads
payloads = prim.GetPayloads()                 # Get the payloads object
payloads.AddPayload("payload.usda")           # Add a payload
payloads.ClearPayloads()                      # Clear all payloads

# Custom Data
print(prim.GetCustomData())                   # Get all custom data
prim.SetCustomDataByKey("key", "value")       # Set custom data by key
print(prim.GetCustomDataByKey("key"))         # Get specific custom data
prim.ClearCustomDataByKey("key")              # Clear specific custom data

# Instance Information
print(prim.IsInstance())                      # Check if the prim is an instance
print(prim.IsInstanceProxy())                 # Check if the prim is an instance proxy
print(prim.GetInherits())                     # Get the inherits object
inherits = prim.GetInherits()
inherits.AddInherit("/path/to/parent")        # Add an inheritance
inherits.ClearInherits() 
```

# Sdf.Path

https://openusd.org/docs/api/class_sdf_path.html

```python
# Importing the necessary module
from pxr import Sdf

# Creating Paths
path = Sdf.Path("/")                          # Create the root path
path = Sdf.Path("/Model/Geom/Cube")           # Create a path to a prim
path = Sdf.Path(".")                          # Create the current path
path = Sdf.Path("..")                         # Create the parent path

# Querying Path Properties
print(path.IsAbsolutePath())                  # Check if the path is absolute
print(path.IsPrimPath())                      # Check if the path refers to a prim
print(path.IsPropertyPath())                  # Check if the path refers to a property
print(path.IsTargetPath())                    # Check if the path refers to a target
print(path.IsMapperPath())                    # Check if the path refers to a mapper
print(path.IsExpressionPath())                # Check if the path refers to an expression
print(path.IsEmpty())                         # Check if the path is empty

# Accessing Path Components
print(path.GetName())                         # Get the base name of the last component
print(path.GetParentPath())                   # Get the parent path
print(path.GetPrimPath())                     # Get the prim path (removes property suffix)
print(path.GetPrimOrPrimVariantSelectionPath()) # Get the path without variant selection
print(path.GetVariantSelection())             # Get the variant selection as a tuple
print(path.GetPropertyName())                 # Get the property name (if it's a property path)

# Modifying Paths
new_path = path.AppendPath("Child")           # Append a child to the path
new_path = path.AppendProperty("propName")    # Append a property to the path
new_path = path.AppendVariantSelection("variantSet", "variant")  # Add a variant selection
new_path = path.ReplaceName("NewName")        # Replace the last component's name
new_path = path.ReplacePrefix("/Old", "/New") # Replace a prefix in the path

# Checking Relationships Between Paths
other_path = Sdf.Path("/Model/Geom")
print(path.HasPrefix(other_path))             # Check if 'other_path' is a prefix of 'path'
print(path.GetCommonPrefix(other_path))       # Get the common prefix of two paths

# Path Comparisons
print(path == other_path)                     # Check if two paths are equal
print(path < other_path)                      # Compare paths lexicographically

# Iterating Over Path Components
for component in path.GetPrefixes():          # Iterate over all prefixes of the path
    print(component)

# Special Path Constants
print(Sdf.Path.EmptyPath())                   # Get an empty path
print(Sdf.Path.AbsoluteRootPath())            # Get the absolute root path
print(Sdf.Path.RelativeRootPath())            # Get the relative root path

# Serialization
print(path.pathString)                        # Get the string representation of the path
print(str(path))    
```
