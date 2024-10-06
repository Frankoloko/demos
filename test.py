from pxr import Usd, UsdGeom, Sdf
path = r"D:\all_francois\git_repos\demos\HelloWorld.usda"
stage = Usd.Stage.CreateNew(path)




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


# # Unset the variant selection for the variant set
# variantSet.SetVariantSelection('')





spherePrim.GetPrim().SetMetadata("variantSets", "small")  







# Save your changes
stage.Save()