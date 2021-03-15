# ---------------------------------- Basic Demo ----------------------------------

# import sys
# from PySide2 import QtCore, QtGui, QtWidgets
# app = QtWidgets.QApplication(sys.argv) # IF YOU ARE NOT IN MAYA OR SOME OTHER DCC, USE THIS

# window = QtWidgets.QWidget()
# window.resize(800, 600) # If you want this

# button1 = QtWidgets.QPushButton("One")
# button2 = QtWidgets.QPushButton("Two")
# button3 = QtWidgets.QPushButton("Three")

# layout = QtWidgets.QVBoxLayout()

# layout.addWidget(button1)
# layout.addWidget(button2)
# layout.addWidget(button3)

# window.setLayout(layout)
# window.show()

# sys.exit(app.exec_()) # IF YOU ARE NOT IN MAYA OR SOME OTHER DCC, USE THIS

# ---------------------------------- Set ID's or other info ----------------------------------

# # If an object inherits from QObject (most QtWidgets do) then you can use this:

# btn = QtWidgets.QPushButton('Press Me')
# btn.setProperty('the_key', 'the value') # Set the value
# btn.property('the_key') # Read the value

# ---------------------------------- Different Ways To Set Layout ----------------------------------

# some_widget = QtWidgets.QWidget()
# vertical_layout_main = QtWidgets.QVBoxLayout(some_widget)

# The above is exactly the same as the below

# some_widget = QtWidgets.QWidget()
# vertical_layout_main = QtWidgets.QVBoxLayout()
# some_widget.setLayout(vertical_layout_main)

# ---------------------------------- Popup Message ----------------------------------

# QtWidgets.QMessageBox.about(None, "Hallo!", "Hey im a message")

# ---------------------------------- Lambda ----------------------------------

# button.clicked.connect(print_this)
# button.clicked.connect(lambda:print_this('pass a value'))

# ---------------------------------- All Controls ----------------------------------

# # Input Box
# line_edit = QtWidgets.QLineEdit()
# line_edit.setText('Here we set the value in the box')
# value = line_edit.text()

# # Button
# def print_this():
#     print('We ran the function!')
# button = QtWidgets.QPushButton("One")
# button.clicked.connect(print_this)

# # Label
# label = QtWidgets.QLabel("This is a label")
# label.setText('Here we changed the text')

# # Checkbox
# def changed(automatically_passed_value):
#     print(automatically_passed_value) # Will print True or False
# check_box = QtWidgets.QCheckBox("A checkbox can have its own label")
# check_box.clicked.connect(changed)
# check_box.isChecked()
# check_box.setChecked(True)

# # Dropdown
# def changed(automatically_passed_value):
#     print(automatically_passed_value)
# combo_box = QtWidgets.QComboBox()
# combo_box.addItems(['One', 'Two', 'Three'])
# combo_box.currentIndexChanged.connect(changed) # Will print the Index
# combo_box.currentTextChanged.connect(changed) # Will print the Text
# value = combo_box.currentIndex()
# value = combo_box.currentText()
# combo_box.setCurrentIndex(1)
# combo_box.setCurrentText('Two')
# combo_box.clear() # You have to run this if you want to change the values inside
# combo_box.addItems(['One', 'Two', 'Two_point_one', 'Three'])

# ---------------------------------- Set Tool Tips ----------------------------------

# cancel_button.setToolTip('This is what you get if you hover over the tool')

# ---------------------------------- Set Item Widths ----------------------------------

# cancel_button.setFixedWidth(70) # A fixed pixel size
# my_layout.addWidget(some_button, 100) # Will size it to 100% width, you can make it any % you want

# ---------------------------------- Aligned Items ----------------------------------

# # Align items to the side (with a spacing in the middle)
# h_layout = QtWidgets.QHBoxLayout()
# h_layout.addWidget(cancel_button)
# h_layout.addStretch() # This is the important part
# h_layout.addWidget(save_button)

# # Align items to the left/top (with a spacing at the right/bottom)
# h_layout = QtWidgets.QHBoxLayout()
# h_layout.addWidget(cancel_button)
# h_layout.addWidget(save_button)
# h_layout.addStretch() # This is the important part

# # Align items to the right/bottom (with a spacing at the left/top)
# h_layout = QtWidgets.QHBoxLayout()
# h_layout.addStretch() # This is the important part
# h_layout.addWidget(cancel_button)
# h_layout.addWidget(save_button)

# ---------------------------------- Nesting Layouts ----------------------------------

# h_layout_1 = QtWidgets.QHBoxLayout()
# h_layout_1.addWidget(button1)
# h_layout_1.addWidget(button2)

# h_layout_2 = QtWidgets.QHBoxLayout()
# h_layout_2.addWidget(button3)
# h_layout_2.addWidget(button4)

# v_layout =  QtWidgets.QVBoxLayout()
# v_layout.addLayout(h_layout_1) # Using "addLayout" is the important part
# v_layout.addLayout(h_layout_2)

# window.setLayout(v_layout)
# window.show()

# ---------------------------------- Top Menu Bar ----------------------------------

# main_window = QtWidgets.QMainWindow() # This needs to be a QMainWindow (to add a menu bar)

# menu_bar = main_window.menuBar()
# menu = menu_bar.addMenu('Some damn title!')
# myAction = menu.addAction('My!')
# myAction = menu.addAction('Two!')
# menu.addSeparator()
# anotherAction = menu.addAction('Another!')

# myAction.triggered.connect(myFunc)
# anotherAction.triggered.connect(anotherFunc)

# main_window.show()

# ---------------------------------- shiboken2 Example ----------------------------------

# # shiboken2 basically converts Maya cmds UI elements, to Qt element

# from PySide2 import QtCore, QtGui, QtWidgets
# from maya import cmds
# import maya.OpenMayaUI as OpenMayaUI
# import shiboken2
# import maya.OpenMayaUI as mui

# window = QtWidgets.QWidget()

# something= cmds.window()
# cmds.paneLayout()
# panel = cmds.modelPanel()

# ptr = mui.MQtUtil.findControl(panel)
# model_panel_widget = shiboken2.wrapInstance(long(ptr), QtWidgets.QWidget)

# grid_layout = QtWidgets.QGridLayout()
# grid_layout.addWidget(model_panel_widget)
# window.setLayout(grid_layout)

# window.show()

# ---------------------------------- Grid Layout ----------------------------------

# # Create main layout
# lay_main = QtWidgets.QGridLayout()

# # Create columns on the layout
# lay_main.setColumnStretch(0, 1)
# lay_main.setColumnStretch(1, 1)
# lay_main.setColumnStretch(2, 1)
# lay_main.setColumnStretch(3, 1)

# # Add controls to layout
# lay_main.addWidget(lbx_dcc, 0, 0) # Left value is the row, right value is the column
# lay_main.addWidget(lbx_type, 0, 1)
# lay_main.addWidget(lbx_asset, 0, 2)
# lay_main.addWidget(lbx_task, 0, 3)
# lay_main.addWidget(btn_open, 1, 3)

# ---------------------------------- Scroll Layout ----------------------------------

# # QScrollArea is not a container. QScrollArea is a "scrolling view" for another widget.
# # You shouldn't set up layout on QScrollArea. You should create widget,
# # fill it with proper layout and then use QScrollArea::setWidget(QWidget *) to make it scrollable.

# from PySide2 import QtWidgets

# # Create many controls and put them onto a layout
# lay_items = QtWidgets.QVBoxLayout()
# for l in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#     lay_items.addWidget(QtWidgets.QPushButton(l))

# # --- THIS (BELOW) IS THE PART THAT GETS ADDED ---
# # Create scroll item
# scroll = QtWidgets.QScrollArea()
# scroll.setWidgetResizable(True) # This makes the items in the scroll area fill the scroll area (or at least the width)
# scroll.setFixedHeight(400)

# # Here you need to create a temp QWidget, because QScrollArea only takes in QWidgets (not layouts)
# temp_widget = QtWidgets.QWidget()
# temp_widget.setLayout(lay_items) # Add controls layout to this widget
# scroll.setWidget(temp_widget)
# # --- THIS (ABOVE) IS THE PART THAT GETS ADDED ---

# # Put the scroll in your main layout
# layout = QtWidgets.QVBoxLayout()
# layout.addWidget(scroll) # AND DON'T FORGET TO DO THIS

# window = QtWidgets.QWidget()
# window.setLayout(layout)
# window.show()

# ---------------------------------- Set background color ----------------------------------

# btn = QtWidgets.QPushButton('Press Me')
# btn.setStyleSheet("background-color:red;")