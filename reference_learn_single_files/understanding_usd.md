# Understanding USD

This document assumes you know a little about USD and that you've played around with `usdview` a bit. The idea of this document is to give you a bit of a better/deeper explanation of what USD things are. Start at the top and read through the document step by step. If you get stuck, go a few steps up and figure out what you are misunderstanding.

I also tried to design the document around using ctrl+f. So if you are looking for something, try a ctrl+f search.

**It's best to read the top description of each section and then come back to the inner sections at a later stage.**

## Table of Contents

0. [Sources](#sources)
1. [Prim(Primitive)](#primprimitive)
    - [PrimSpec](#primspec)
2. [Path](#path)
3. [Layer](#layer)
    - [Layer Stack](#layer-stack)
    - [Edit Target](#edit-target)
    - [Layer Offset](#layer-offset)
4. [Properties](#properties)
    - [Relationships](#relationships)
    - [Attributes](#attributes)
        - [xformOp:translate](#xformoptranslate)
        - [xformOp:rotateXYZ](#xformoprotatexyz)
        - [xformOp:scale](#xformopscale)
        - [xformOpOrder](#xformoporder)
        - [primvars:displayColor](#primvarsdisplaycolor)
        - [primvars:displayOpacity](#primvarsdisplayopacity)
        - [visibility](#visibility)
        - [points](#points)
        - [normals](#normals)
        - [extent](#extent)
        - [purpose](#purpose)
            - [default](#default)
            - [guide](#guide)
            - [proxy](#proxy)
            - [render](#render)
    - [PropertySpec](#PropertySpec)
    - [PropertyStack](#PropertyStack)
5. [Metadata](#metadata)
    - [defaultPrim](#defaultprim)
    - [kind](#kind)
        - [model](#model)
        - [group](#group)
        - [assembly](#assembly)
        - [component](#component)
        - [subcomponent](#subcomponent)
    - [instanceable](#instanceable)
    - [startTimeCode](#starttimecode)
    - [endTimeCode](#endtimecode)
    - [upAxis](#upaxis)
    - [documentation](#documentation)
    - [active](#active)
6. [Composition](#composition)
    - [Local/Sublayer](#localsublayer)
    - [Inherits](#inherits)
    - [Variants](#variants)
    - [Reference](#reference)
    - [Payload](#payload)
    - [Specializes](#specializes)
7. [Stage](#stage)
8. [Specifier](#specifier)
    - [def](#def)
    - [over](#over)
    - [class](#class)
9. [Opinion](#opinion)
10. [Resolvers](#resolvers)


## Sources
* Good beginner explanation: https://remedy-entertainment.github.io/USDBook/motivation.html
* Good place to ask for help: https://forum.aousd.org/latest
* Understanding USD through Houdini's eyes: https://www.sidefx.com/docs/houdini/solaris/usd.html
* The actual source code (good to read through the classes when stuck): https://github.com/PixarAnimationStudios/OpenUSD
* Official documentation: https://openusd.org/release/api/index.html
* Amazing glossary to Ctrl+F search for terms: https://openusd.org/release/glossary.html#

## Prim(Primitive)
Everything about USD starts at a Prim. Prims are the fundamental nodes in the USD structure. These are the items you see in the tree graph. They can be geometry, empty groups, or just about anything. See [here](https://remedy-entertainment.github.io/USDBook/terminology/prims.html)
* The parent/child nodes in the hierarchy
* Can have different types like `xForm`, `Mesh`, `Scope` & users can create custom types
* Does not hold data, is just a container

### PrimSpec

A weird-ish term to get used to. Basically a `Prim` is the actual constructed object and the `PrimSpec` is the details of that object before it is constructed (the written down version of the Prim). Another way to think of it, is that `PrimSpec` is all the layers and opinions that might resolve and `Prim` is the final result when everything got resolved.

## Path
Path's are the IDs of everything in the USD structure. You use the Path to access and edit/change things.
* The slash(`/`) path to a Prim(slashes) or Property(full stop)
* Like `/this/is/my/prim.property`
* Paths are always unique, it is the ID of something

## Layer
A layer is essentially one scene with many nodes inside it. One `usd` file. You can also view it as one Photoshop layer. The concept of USD relates really well to the design of Photoshop. The idea being you can stack multiple Layers(scenes) on top of each other and have one resulting scene at the end.
* A saveable hierarchy
* Usually in the form of `usd`, `usda`, `usdc`, `usdz`
* Infinitely stackable

### Layer Stack
* The internal stack of Layers that create the current Layer being viewed.
* The order is important (in `usdview`, the top one is the most important, like Photoshop layers)
* Only does straight up merging, nothing fancy.

### Edit Target
When you have a composition open with multiple layers, you can set an `EditTarget` to have all of your changes get saved to that layer.

When not set, the default layer created is called a `Session Layer` and is a layer sitting above all existing layers.

### Layer Offset
When layering something in, you can apply an `offset`(time) and `scale` change. This is useful when an animation starts later in a shot or so on.

```
(
    subLayers = [
        @./someAnimation.usd@ (offset = 10; scale = 0.5)
    ]
)
```

### Session Layer

A Session Layer is a temporary type of layer that holds all edits a person is making. For example, if you open a `.usd` file in `usdview` and you select variants and enable/disable prims in the viewport, these changes are being saved to your current session layer. This layer can of course be exported as an official new layer to add to the stage.

## Properties
Properties are key-value pairs that live on Prims. They can hold just about any information and can also be keyed to change over time (imagine an x-axis value changing over time).
* Two types: Attributes(actual value) & Relationship(points to another property/prim)
* They have a `name`(key) and `value`
* They can have a namespace like `material:binding`. Where `material` is the namespace and `binding` the `name`(key). Namespaces are just groupings.

### Relationships
Relationships aren't actual values, but point to something else. Like `rel target = </World/Target>` which points to the prim `/World/Target`.

A `Relationship` is Local, pointing to something in the current Layer (like a child-parent constraint). Which is different to a `Reference` which points to another Layer like `reference = @car_model.usd@`

### Attributes
Attributes are actual values being set. Like `int[] faceVertexCounts = [4, 4, 4, 4, 4, 4]`

#### xformOp:translate
Specifies the translation transformation of a prim
#### xformOp:rotateXYZ
Specifies the rotation transformation of a prim using XYZ Euler angles
#### xformOp:scale
Specifies the scale transformation of a prim
#### xformOpOrder
Defines the order of transformation operations
#### primvars:displayColor
Defines the color of the prim for display purposes
#### primvars:displayOpacity
Defines the opacity of the prim for display purposes
#### visibility
Specifies the visibility of a prim (e.g., "inherited" or "invisible")
#### points
Defines the vertex positions of a mesh
#### normals
Defines the normal vectors of a mesh
#### extent
Specifies the bounding box of a prim
#### purpose
* A Property(Attribute)
* Defines when an item will be displayed
* Doesn't currently support custom values
##### default
Includes all of the below
##### guide
Generally an outline indication, like a bounding box
##### proxy
A viewport version of the item
##### render
A high resolution render version of the item

### PropertySpec

Similar to `PrimSpec` this just refers to the written format of a property. Before evaluation/composition it is a `PropertySpec` and after it becomes the final created `Property`.

### PropertyStack

As you would imagine, it is merely the stack of properties that together create the final resolved property.

## Metadata
Also a key-value pair like `Properties` with the main difference being that it can't be animated/keyed.
* Extra information saved on a Layer, Prim or Property.
* Not animatable (static value)
* Some are not important, like `notes`, but some DCCs/Tools could code around certain ones, like `subLayers` is extremely important and should not be edited.

### defaultPrim
If no path is given, this Prim will be used/referenced when a layer is referenced. It must point to a root(PseudoRoot) Prim. Not a path. Not specifying one will result in a warning. It is recommended to always set one for layers that will be referenced or payloaded.

### kind
* A metadata key that defines the type of Prim. For example `Model`, `Group`, `Assembly`, `Component`.
* They allow for easier traversing and understanding of the Prim's intention.
* For example a Group Kind should not hold geometry data. But a Component Kind might.
* Studios can use and create these in their own ways, USD ships with a few defaults to use:
#### model
Base class for all model kinds. model is considered an abstract type and should not be assigned as any Prim's kind
#### group
Models that simply group other models
#### assembly
An important group model type, often a published asset or reference to a published assets. Think of assembling together certain models to create a decorated table or dirty variant.
#### component
A "leaf model" that can contain no other models
#### subcomponent
An identified, important "sub part" of a component model

### instanceable
`True`/`False` value. Tells USD to turn the asset into a `Prototype` (a singleton local copy) and have all other copies point to this same `Prototype`. Generally you need a `references` on the Prim as well, which points to the original instanceable source object.
### startTimeCode
Defines the start time of the scene for time-sampled animations
### endTimeCode
Defines the end time of the scene for time-sampled animations
### upAxis
Specifies the up axis for the scene, usually "Y" or "Z"
### documentation
Provides a human-readable description of the prim or property
### active
`True`/`False` value. It enables/disables the entire Prim and all it's children from being composed.

## Composition
When Layers are stacked together, you have different methods of merging them. Similar to layer types in Photoshop, one could be a simple merge, but another could be an Overlay or other types of merges. The Composition defines how multiple Layer Stacks are merged. There are 6 types. These Composition Arcs have strengths. If the same value is targeted by multiple Arcs, a certain one will resolve. The order is: `LIVRPS (Liver Peas)`. It will resolve from left to right, stopping at the first one found. [Here](https://remedy-entertainment.github.io/USDBook/terminology/LIVRPS.html) is a good explanation of it.
### Local/Sublayer
Straight forward layering of one thing over another
### Reference
Looks like `reference = @car_model.usd@`. Points to a Layer from a different file, or something in the current file.
### Variants
A Metadata type. It holds multiple Variants. Each variant is essentially a Layer Stack being imported. You can put anything in a Variant but only 1 can ever be active.
### Payload
Remember "it pays to load it". Basically lazy loading something. In other words, it won't load until you turn it on. Used to store large models/data behind to not overwhelm scenes.
Looks like payload = @car_model.usd@
### Inherits
Similar to instancing. Basically you can make on prim Inherit another. Therefore copying all it's properties and children. Changing the original prim will change the others live. You can inherit a Class Prim type.
### Specializes
Creating a specialized version of something. Similar to Inherit, creating a Variant and overriding certain values. Except it's opinion always wins.

## Stage
The final scene after all Layer resolving has occurred. It is essentially also just another new Layer, but a Stage is a more formal term for the "resolved layer stack".
* The final result of all merging
* You can flatten and export this (like exporting a jpg in Photoshop)

## Specifier
When defining a prim, there are 3 ways to do so: `def`, `over` & `class`. These change how exactly a Prim is created within the Layer/Stage.
### def
A concrete definition. It creates the item like normal.
```
def Mesh "Cube"
{
    float3[] points = [(1, 1, 1), (1, -1, 1), (-1, -1, 1), (-1, 1, 1), (1, 1, -1), (1, -1, -1), (-1, -1, -1), (-1, 1, -1)]
    int[] faceVertexCounts = [4, 4, 4, 4, 4, 4]
    int[] faceVertexIndices = [0, 1, 2, 3, 0, 3, 7, 4, 3, 2, 6, 7, 1, 5, 6, 2, 5, 4, 7, 6, 0, 4, 5, 1]
    color3f[] primvars:displayColor = [(0, 0, 1)]
}
```
### over
Only an override. Will override if the Prim already exists, but will not create one from scratch.
```
over "Cube"
{
    color3f[] primvars:displayColor = [(1, 0, 0)] # Change the color to red
}
```
### class
An abstract Prim definition and does not contribute to the scene by default, but other prims can inherit it. Mostly used if you wanted to create a type of template for other Prims to source off of.
```
class "CubeTemplate"
{
    def Mesh "Cube"
    {
        float3[] points = [(1, 1, 1), (1, -1, 1), (-1, -1, 1), (-1, 1, 1), (1, 1, -1), (1, -1, -1), (-1, -1, -1), (-1, 1, -1)]
        int[] faceVertexCounts = [4, 4, 4, 4, 4, 4]
        int[] faceVertexIndices = [0, 1, 2, 3, 0, 3, 7, 4, 3, 2, 6, 7, 1, 5, 6, 2, 5, 4, 7, 6, 0, 4, 5, 1]
        color3f[] primvars:displayColor = [(0, 0, 1)]
    }
}

def "World"
{
    instance "FirstCube" (instanceable = true) = </CubeTemplate>
    instance "SecondCube" (instanceable = true) = </CubeTemplate>
    "FirstCube".xformOp:translate = (2, 0, 0)
    "SecondCube".xformOp:translate = (-2, 0, 0)
}
```

## Opinion
An opinion is merely the act of setting a value to something in a Layer. You want the thing to have a certain value, which is your opinion, but another Layer could be placed on top of yours, thus overriding your opinion. For example `int[] faceVertexCounts = [4, 4, 4, 4, 4, 4]` is an opinion. Honestly, the word sounds more important than it really is...in my opinion :P

## Resolvers

When constructing references to other assets/files, you don't ever want to reference hardcoded paths. Because if your server location ever changes, hundreds of assets might break. `Resolvers` help you keep paths dynamic.

For example, we know the `Dog` asset lives in `/project/assets/animals/Dog`. But let's say the project folder moves to `/external/clients/project/assets/animals/Dog`. Now your assets would break if you had the path hardcoded. Instead you would only put `/assets/animals/Dog` in your usd scene, and the `Resolver` would resolve (with config settings) where to find that asset.

Another example, a common references is `Get me the Latest version the Dog asset`. Since we use the term `Latest` there, we don't know whether it means v1 or v10 or v100. So hardcoding `/some/path/Dog_v100` would be a mistake. Another example would be getting the `Approved` version, which might not be the Latest version. These are examples of what `Resolvers` would do. Essentially, turn the `Dog-Approved` into `/path/to/Dog_v15`.

USD ships with a default resolver called `ArResolver`. It is pretty basic, but allows studios to customize the resolving to their own needs. For example, something with `Latest` and `Approved` flags would look like this:

Creating the Custom Resolver (custom_resolver_init.py)
```python
from pxr import Ar
import os
import re

class AdvancedVersioningResolver(Ar.Resolver):
    def __init__(self):
        super().__init__()

    def Resolve(self, assetPath, latest=True, approved=False):
        # ANYTHING IN HERE IS CUSTOM FOR EACH STUDIO AND SO ARE THE ARGUMENTS ADDED ABOVE (latest, approved)...

        base_path, extension = os.path.splitext(assetPath)
        directory = os.path.dirname(base_path)
        base_name = os.path.basename(base_path)

        # Example pattern: "wood_v1_approved.jpg"
        pattern = re.compile(rf"{re.escape(base_name)}_v(\d+)(_approved)?{re.escape(extension)}")

        # Find all matching files and their versions
        matching_files = []
        for f in os.listdir(directory):
            match = pattern.match(f)
            if match:
                version = int(match.group(1))
                is_approved = bool(match.group(2))
                matching_files.append((version, is_approved, f))

        # Determine the file based on the criteria
        if not matching_files:
            return ""
        
        if approved:
            # Filter to approved files only
            approved_files = [f for f in matching_files if f[1]]
            if not approved_files:
                return ""
            matching_files = approved_files
        
        if latest:
            # Sort by version and get the latest
            matching_files.sort(key=lambda x: x[0], reverse=True)
        
        return os.path.join(directory, matching_files[0][2])

# Register the custom resolver
Ar.RegisterResolver(AdvancedVersioningResolver)
```
Using the Custom Resolver
```python
from pxr import Ar

# Create an instance of the custom resolver
resolver = Ar.GetResolver()

# Assuming the search path is set to the assets directory
resolver.ConfigureResolverForAssetPath('/project/assets')

# Create a context to manage the search path
with Ar.ResolverContextBinder(resolver.CreateDefaultContext()):
    # Resolve the path for the latest and approved version of the wood texture
    latest_approved_wood_texture_path = resolver.Resolve('textures/wood.jpg', latest=True, approved=True)
    print(f"Resolved latest approved wood texture path: {latest_approved_wood_texture_path}")
    
    # Resolve the path for the latest (regardless of approval) version of the wood texture
    latest_wood_texture_path = resolver.Resolve('textures/wood.jpg', latest=True, approved=False)
    print(f"Resolved latest wood texture path: {latest_wood_texture_path}")
    
    # Resolve the path for the approved (not necessarily the latest) version of the wood texture
    approved_wood_texture_path = resolver.Resolve('textures/wood.jpg', latest=False, approved=True)
    print(f"Resolved approved wood texture path: {approved_wood_texture_path}")
```
You can then set up applications like `usdview` to use this resolver by pointing to the `custom_resolver_init.py` mentioned above (since it has the `Ar.RegisterResolver` line in it).

```sh
export USD_PLUGIN_PATH=/path/to/your/custom_resolver_init_directory:$USD_PLUGIN_PATH
usdview /path/to/your/scene.usd
```
And in the `.usd` file it would look like this:
```
#usda 1.0
(
    defaultPrim = "Scene"
)

def Scope "Scene" {
    def Shader "WoodShader" {
        asset inputs:diffuseTexture = @textures/wood?latest=true&approved=true@
    }
}
```
You can also write the values in custom attributes, but this would require you to create custom asset resolving code (more complicated):
```
#usda 1.0
(
    defaultPrim = "Scene"
)

def Scope "Scene" {
    def Shader "WoodShader" {
        asset inputs:diffuseTexture = @textures/wood.jpg@
        uniform token latest = "true"
        uniform token approved = "true"
    }
}
```