# Understanding USD

## Table of Contents

- [Great Sources](#great-sources)
- [General Terminology](#general-terminology)
    - [Prim(Primitive)](#primprimitive)
    - [Path](#path)
    - [Layer](#layer)
        - [Layer Stack](#layer-stack)
        - [Edit Target](#edit-target)
    - [Properties](#properties)
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
    - [Metadata](#metadata)
        - [defaultPrim](#defaultprim)
        - [kind](#kind)
        - [instanceable](#instanceable)
        - [startTimeCode](#starttimecode)
        - [endTimeCode](#endtimecode)
        - [upAxis](#upaxis)
        - [documentation](#documentation)
    - [Composition](#composition)
        - [Local/Sublayer](#localsublayer)
        - [Inherits](#inherits)
        - [Variants](#variants)
        - [Reference](#reference)
        - [Payload](#payload)
        - [Specializes](#specializes)
    - [Stage](#stage)
    - [Opinion](#opinion)
    - [Specifier](#specifier)
        - [def](#def)
        - [over](#over)
        - [class](#class)

## Great Sources
* Good beginner explanation: https://remedy-entertainment.github.io/USDBook/motivation.html
* Good place to ask for help: https://forum.aousd.org/latest
* Understanding USD through Houdini's eyes: https://www.sidefx.com/docs/houdini/solaris/usd.html
* The actual source code (good to read through when stuck): https://github.com/PixarAnimationStudios/OpenUSD
* Official documentation: https://openusd.org/release/api/index.html
* Amazing glossary to Ctrl+F search for terms: https://openusd.org/release/glossary.html#

## General Terminology

Be sure to check out https://openusd.org/release/glossary.html# for more terms that might not be documented here.

### Prim(Primitive)
* The parent/child nodes in the hierarchy
* Can have different types like `xForm`, `Mesh`, `Scope` & users can create custom types
* Does not hold data, is just a container

---

### Path
* The slash(`/`) path to a Prim(slashes) or Property(full stop)
* Like `/this/is/my/prim.property`
* Paths are always unique, it is the ID of something

---

### Layer
* A saveable hierarchy
* Usually in the form of `usd`, `usda`, `usdc`, `usdz`
* Infinitely stackable

#### Layer Stack
* The internal stack of Layers that create the current Layer being viewed.
* The order is important (in `usdview`, the top one is the most important, like Photoshop layers)
* Only does straight up merging, nothing fancy.

#### Edit Target
When you have a composition open with multiple layers, you can set an `EditTarget` to have all of your changes get saved to that layer.

When not set, the default layer created is called a `Session Layer` and is a layer sitting above all existing layers.

---

### Properties
* Two types: Attributes(actual value) & Relationship(points to another property/prim)
* They have a `name`(key) and `value`
* They can have a namespace like `material:binding`. Where `material` is the namespace and `binding` the `name`(key). Namespaces are just groupings.

#### Relationships
Relationships aren't actual values, but point to something else. Like `rel target = </World/Target>` which points to the prim `/World/Target`.

A `Relationship` is Local, pointing to something in the current Layer (like a child-parent constraint). Which is different to a `Reference` which points to another Layer like `reference = @car_model.usd@`

#### Attributes
Attributes are actual values being set. Like `int[] faceVertexCounts = [4, 4, 4, 4, 4, 4]`

##### xformOp:translate
Specifies the translation transformation of a prim
##### xformOp:rotateXYZ
Specifies the rotation transformation of a prim using XYZ Euler angles
##### xformOp:scale
Specifies the scale transformation of a prim
##### xformOpOrder
Defines the order of transformation operations
##### primvars:displayColor
Defines the color of the prim for display purposes
##### primvars:displayOpacity
Defines the opacity of the prim for display purposes
##### visibility
Specifies the visibility of a prim (e.g., "inherited" or "invisible")
##### points
Defines the vertex positions of a mesh
##### normals
Defines the normal vectors of a mesh
##### extent
Specifies the bounding box of a prim
##### purpose
* A Property(Attribute)
* Defines when an item will be displayed
* Doesn't currently support custom values
###### default
Includes all of the below
###### guide
Generally an outline indication, like a bounding box
###### proxy
A viewport version of the item
###### render
A high resolution render version of the item

---

### Metadata
* Extra information saved on a Layer, Prim or Property.
* Not animatable (static value)
* Some are not important, like `notes`, but some DCCs/Tools could code around certain ones, like `subLayers` is extremely important and should not be edited.

Here are some important/commonly used Metadata keys: 

#### defaultPrim
If no path is given, this Prim will be used/referenced when a layer is referenced. It must point to a root(PseudoRoot) Prim. Not a path. Not specifying one will result in a warning. It is recommended to always set one for layers that will be referenced or payloaded.

#### kind
* A metadata key that defines the type of Prim. For example `Model`, `Group`, `Assembly`, `Component`.
* They allow for easier traversing and understanding of the Prim's intention.
* For example a Group Kind should not hold geometry data. But a Component Kind might.
* Studios can use and create these in their own ways, USD ships with a few defaults to use:
    * `model`	base class for all model kinds. model is considered an abstract type and should not be assigned as any Prim's kind
    * `group`	models that simply group other models
    * `assembly`	an important group model, often a published asset or reference to a published asset
    * `component`	a “leaf model” that can contain no other models
    * `subcomponent`	an identified, important “sub part” of a component model
#### instanceable
`True`/`False` value. Tells USD to turn the asset into a `Prototype` (a singleton local copy) and have all other copies point to this same `Prototype`. Generally you need a `references` on the Prim as well, which points to the original instanceable source object.
#### startTimeCode
Defines the start time of the scene for time-sampled animations
#### endTimeCode
Defines the end time of the scene for time-sampled animations
#### upAxis
Specifies the up axis for the scene, usually "Y" or "Z"
#### documentation
Provides a human-readable description of the prim or property

---

### Composition
Defines how multiple Layer Stacks are merged. There are 6 types. These Composition Arcs have strengths. If the same value is targeted by multiple Arcs, a certain one will resolve. The order is: `LIVRPS (Liver Peas)`. It will resolve from left to right, stopping at the first one found.
#### Local/Sublayer
Straight forward layering of one thing over another
#### Reference
Looks like `reference = @car_model.usd@`. Points to a Layer from a different file, or something in the current file.
#### Variants
A Metadata type. It holds multiple Variants. Each variant is essentially a Layer Stack being imported. You can put anything in a Variant but only 1 can ever be active.
#### Payload
Remember "it pays to load it". Basically lazy loading something. In other words, it won't load until you turn it on. Used to store large models/data behind to not overwhelm scenes.
Looks like payload = @car_model.usd@
#### Inherits
Similar to instancing. Basically you can make on prim Inherit another. Therefore copying all it's properties and children. Changing the original prim will change the others live. You can inherit a Class Prim type.
#### Specializes
Creating a specialized version of something. Similar to Inherit, creating a Variant and overriding certain values. Except it's opinion always wins.

---

### Stage
* The final result of all merging
* You can flatten and export this (like exporting a jpg in Photoshop)

---

### Specifier
When defining a prim, there are 3 ways to do so: `def`, `over` & `class`
#### def
A concrete definition. It creates the item.
```
def Mesh "Cube"
{
    float3[] points = [(1, 1, 1), (1, -1, 1), (-1, -1, 1), (-1, 1, 1), (1, 1, -1), (1, -1, -1), (-1, -1, -1), (-1, 1, -1)]
    int[] faceVertexCounts = [4, 4, 4, 4, 4, 4]
    int[] faceVertexIndices = [0, 1, 2, 3, 0, 3, 7, 4, 3, 2, 6, 7, 1, 5, 6, 2, 5, 4, 7, 6, 0, 4, 5, 1]
    color3f[] primvars:displayColor = [(0, 0, 1)]
}
```
#### over
Only an override. Will override if the Prim already exists, but will not create one from scratch.
```
over "Cube"
{
    color3f[] primvars:displayColor = [(1, 0, 0)] # Change the color to red
}
```
#### class
An abstract Prim definition and does not contribute to the scene by default, but other prims can inherit it.
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
---

### Opinion
An opinion is merely the act of setting a value to something in a Layer. You want the thing to have a certain value, which is your opinion, but another Layer could be placed on top of yours, thus overriding your opinion. For example `int[] faceVertexCounts = [4, 4, 4, 4, 4, 4]` is an opinion. Honestly, the word sounds more important than it really is.

---