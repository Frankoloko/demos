# https://openusd.org/release/api/index.html

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

root_layer = self.superset_stage.GetRootLayer()
original_state = root_layer.ExportToString()
prim = self.superset_stage.GetDefaultPrim()
prim.GetVariantSets().GetAllVariantSelections()
self.superset_stage.Reload() # Reload the file