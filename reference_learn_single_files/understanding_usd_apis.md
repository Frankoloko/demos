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

## Change prim paths / Reparent prims

```python
edit = Sdf.BatchNamespaceEdit()
edit.Add("/current/prim/path", "/new/prim/path")
layer = Sdf.Layer.FindOrOpen(usd_file)

# Note that if these edits would not work, you would not even know.
# Everything will execute without errors.
# So you can check the success first with
print(layer.CanApply(edit))

layer.Apply(edit)
```