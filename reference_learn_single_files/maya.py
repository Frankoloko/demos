##############################################################################################################
# CREATE A SHELF BUTTON WITH A RIGHT CLICK MENU

# This one will still keep the default Open/Edit etc default shelf tool right click menu options
id = "fff"
shelf_button = cmds.shelfButton(
    id,
    label="My Button",
    image="pythonFamily.png",
    command='print("Hi")',
    parent="Francois", # This shelf already has to exist
    width=35,
    height=35,
)
cmds.shelfButton(id, edit=True, menuItem=("Item1", 'print("1")'), menuItemPython=0)
cmds.shelfButton(id, edit=True, menuItem=("Item2", 'print("2")'), menuItemPython=0)

# OR

# This one will replace the menu items you have
new_shelf_button = cmds.shelfButton(
    "awd",
    label="My Button",
    image="pythonFamily.png",
    command='print("Hi")',
    parent="Francois", # This shelf already has to exist
    width=35,
    height=35,
    noDefaultPopup=True
)
popup_menu = cmds.popupMenu(parent=new_shelf_button, button=3)
menu_command_1 = cmds.menuItem(label="Item1", sourceType="python", parent=popup_menu, command='print("1")')
menu_command_2 = cmds.menuItem(label="Item2", sourceType="python", parent=popup_menu, command='print("2")')

##############################################################################################################
# SAVE METADATA IN A SCENE

cmds.dataStructure(format='raw', asString='name=NotesStruct:string=Notes')
cmds.addMetadata(streamName='previs_wip', channelName='previs_wip', scene=True, structure='NotesStruct')
cmds.editMetadata(streamName='previs_wip', channelName='previs_wip', scene=True, index=7, memberName='Notes', stringValue="These are my notes")
cmds.getMetadata(scene=True, index=7, memberName='Notes')

##############################################################################################################
# DISPLAY MESSAGES IN MAYA'S STATUS BAR BOTTOM-RIGHT

import pymel.core as pm
pm.displayInfo("test")
pm.displayWarning("test")
pm.displayError("test")