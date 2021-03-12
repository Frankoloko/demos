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

# cancel_button.setFixedWidth(70)

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