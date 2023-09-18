import hou

############################################################################################################
# ADD SPARE PARM TO NODE

# Get the HDA node
hda_node = hou.node("/path/to/your/HDA")

# Add an parm
new_parm = hou.StringParmTemplate("my_int_property", "My Int Property", 1) # The 1 is for the number of components

# If you want it to get placed at a certain position, use this
parm_group = hda_node.parmTemplateGroup()
existing_parm = parm_group.find("some_parm")
parm_group.insertBefore(existing_parm, new_parm)
hda_node.setParmTemplateGroup(parm_group)

# If you don't care about the position and you just want it to get added to the bottom of the list then just use this
hda_node.addSpareParmTuple(new_parm)

# If you want to create a folder type of parm
parm_folder = hou.FolderParmTemplate(
    name="tags",
    label="Tags",
    folder_type=hou.folderType.Simple
)
hda_node.addSpareParmTuple(parm_folder)

# If you want to add a parm to a folder parm
parm_group = node.parmTemplateGroup()
tags_folder = parm_group.find("tags") # This is your folder parm's name
parm_group.appendToFolder(tags_folder, new_parm)
node.setParmTemplateGroup(parm_group)

############################################################################################################
# ADD SPARE PARM TO NODE