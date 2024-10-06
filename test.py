from pxr import Usd, UsdGeom, Sdf
path = r"D:\all_francois\git_repos\demos\HelloWorld_test.usda"


stage = Usd.Stage.CreateNew(r"D:\all_francois\git_repos\demos\HelloWorld.usda")
root_layer = stage.GetRootLayer()

# Create multiple new sublayers.
sub_layer_1 = Sdf.Layer.CreateNew(r"D:\all_francois\git_repos\demos\HelloWorld_1.usda")
sub_layer_2 = Sdf.Layer.CreateNew(r"D:\all_francois\git_repos\demos\HelloWorld_2.usda")
sub_layer_3 = Sdf.Layer.CreateNew(r"D:\all_francois\git_repos\demos\HelloWorld_3.usda")

# Add the sublayers to the root layer by setting their identifiers in the subLayerPaths list.
root_layer.subLayerPaths.append(sub_layer_1.identifier)
root_layer.subLayerPaths.append(sub_layer_2.identifier)
root_layer.subLayerPaths.append(sub_layer_3.identifier)

# Save your changes
stage.Save()