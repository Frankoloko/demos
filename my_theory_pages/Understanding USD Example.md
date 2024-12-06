### Component

The raw asset data. A model + shader combination: model_layer.usda + shader_layer.usda

Variants can also be components, that layer in the base_layer.usda before adding new overs and changes.

### Collection

A collection of components. For example face_component_layer.usda + body_component_layer.usda

A parallel connection of layers:
- face_layer.usda
- body_layer.usda
- clothes_layer.usda

Note that this is also where you would create variants.

This is also where you could save xform data, variant selects and so on.

This is also the one that will nest the most. You can have many collections inside collections.

### Item

A series connection of layers:
- asset_layer.usda + animation_layer.usda + fx_layer.usda

### Stage

A collection of items.

Here you can also add any overwrites you would need to make minor unique adjustments.