import hou

############################################################################################################
# ADDUIBNG

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
