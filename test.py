from pxr import Usd, UsdGeom, Sdf
path = r"D:\all_francois\git_repos\demos\HelloWorld.usda"
stage = Usd.Stage.CreateNew(path)





# Define a new prim at the specified path
prim = stage.DefinePrim("/MyPrim", "Xform")

# Add metadata to the prim
prim.SetMetadata("dude", "I am a comment")

















# Save your changes
stage.Save()