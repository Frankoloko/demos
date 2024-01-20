# ---------------------------------- Basic Demo ----------------------------------

# import sys
# from PySide2 import QtCore, QtGui, QtWidgets
# app = QtWidgets.QApplication.instance()

# IF YOU ARE NOT IN MAYA OR SOME OTHER DCC, USE THIS
# if not app:
#     app = QtWidgets.QApplication(sys.argv)

# window = QtWidgets.QWidget()
# window.resize(800, 600) # If you want this

# button1 = QtWidgets.QPushButton("One")
# button2 = QtWidgets.QPushButton("Two")
# button3 = QtWidgets.QPushButton("Three")

# layout = QtWidgets.QVBoxLayout()

# layout.addWidget(button1)
# layout.addWidget(button2)
# layout.addWidget(button3)

# window.setWindowTitle('A Title')
# window.setLayout(layout)
# window.show()

# # sys.exit(app.exec_()) # IF YOU ARE NOT IN MAYA OR SOME OTHER DCC, USE THIS

# ---------------------------------- STARTER ----------------------------------
# This one has "keep window on top" and "delete older windows" added

# import sys
# from PySide2 import QtCore, QtGui, QtWidgets
# app = QtWidgets.QApplication.instance()

# IF YOU ARE NOT IN MAYA OR SOME OTHER DCC, USE THIS
# if not app:
#     app = QtWidgets.QApplication(sys.argv)

# window = QtWidgets.QWidget()
# window.resize(800, 600) # If you want this

# button1 = QtWidgets.QPushButton("One")
# button2 = QtWidgets.QPushButton("Two")
# button3 = QtWidgets.QPushButton("Three")

# layout = QtWidgets.QVBoxLayout()

# layout.addWidget(button1)
# layout.addWidget(button2)
# layout.addWidget(button3)

# # Delete the window if it is already running
# window_name = 'SAM_QT'
# open_widgets = QtWidgets.QApplication.instance().topLevelWidgets()
# for item in open_widgets:
#     if item.objectName() == window_name:
#         item.deleteLater()

# # For the above to work, you need to set the name on your window as well
# self.window.setObjectName(window_name)

# # For keeping window on top
# # In most cases, you need a main window to parent the QtCore.Qt.Tool to, you would do it like this:
# app = QtWidgets.QApplication.instance()
# if not app:
#     app = QtWidgets.QApplication(sys.argv)
# main_window = None
# current_software = self.SAM.Helpful_Code.get_current_software()
# if current_software == 'maya':
#     main_window = next(w for w in app.topLevelWidgets() if w.objectName() == 'MayaWindow')
# if current_software == 'houdini':
#     import hou
#     main_window = hou.qt.mainWindow()
# self.window.setParent(main_window)
# window.setWindowFlags(QtCore.Qt.Tool)

# window.setWindowTitle('A Title')
# window.setLayout(layout)
# window.show()

# # sys.exit(app.exec_()) # IF YOU ARE NOT IN MAYA OR SOME OTHER DCC, USE THIS

# ---------------------------------- Getting the QApplication ----------------------------------

# app = QtWidgets.QApplication.instance()
# if not app:
#     app = QtWidgets.QApplication(sys.argv)

# maya_window = next(w for w in app.topLevelWidgets() if w.objectName()=='MayaWindow')

# ---------------------------------- Block signals ----------------------------------

# When you are changing this from a code side, and it is causing on-change type of triggers
# Then you can use this to block/enable signals
# I have found that it doesn't always work as expected though
# QComboBox_versions.blockSignals(False)
# QComboBox_versions.blockSignals(True)

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

# ---------------------------------- Layout spacing ----------------------------------

# lay_main.addSpacing(10)

# ---------------------------------- Popup Messages ----------------------------------

# # Basic info
# QtWidgets.QMessageBox.about(None, "Hallo!", "Hey im a message")

# # Yes/No question
# message_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, "title", "Question", QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
# if QtWidgets.QMessageBox.Yes == message_box.exec_():
#     print('Yes pressed')
# else:
#     print('No pressed')
# print('Done')

# ---------------------------------- Lambda ----------------------------------

# button.clicked.connect(print_this)
# button.clicked.connect(lambda:print_this('pass a value'))

# ---------------------------------- All Controls ----------------------------------

# # Input Box
# line_edit = QtWidgets.QLineEdit()
# line_edit.setText('Here we set the value in the box')
# line_edit.setAlignment(QtCore.Qt.AlignCenter) # Centre the text if you need it
# value = line_edit.text()

# # Spin Box (for integer values only)
# line_edit = QtWidgets.QSpinBox()

# # Button
# def print_this():
#     print('We ran the function!')
# button = QtWidgets.QPushButton("One")
# button.clicked.connect(print_this)

# # Label
# label = QtWidgets.QLabel("This is a label")
# label.setText('Here we changed the text')

# # Make label bigger
# html_settings = "<font size=5> This is my label </font>"
# lbl_title = QtWidgets.QLabel(html_settings)

# # More font stuff
# my_font = QtGui.QFont("Times", 12, QtGui.QFont.Bold)
# label = QtWidgets.QLabel("Select")
# label.setWordWrap(True)
# label.setAlignment(QtCore.Qt.AlignCenter)
# label.setFont(my_font)

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

# # List Widget
# # Without headers/columns
# items = ['something', 'another', 'one more']
# list_widget = QtWidgets.QListWidget()
# list_widget.addItems(items)
# # Enable multiple selections
# list_widget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)

# # Tree Widget
# # Without headers/columns
# tree_widget = QtWidgets.QTreeWidget()
# tree_widget.setHeaderHidden(True)
# sequence_0010 = QtWidgets.QTreeWidgetItem(tree_widget, ['0010'])
# shot_010 = QtWidgets.QTreeWidgetItem(sequence_0010, ['010'])
# sequence_0020 = QtWidgets.QTreeWidgetItem(tree_widget, ['0020'])
# shot_020 = QtWidgets.QTreeWidgetItem(sequence_0020, ['020'])

# # With headers/columns
# tree_widget = QtWidgets.QTreeWidget()
# tree_widget.setHeaderLabels(['ID', 'Name'])
# sequence_0010 = QtWidgets.QTreeWidgetItem(tree_widget, ['0010', 'Underwater'])
# shot_010 = QtWidgets.QTreeWidgetItem(sequence_0010, ['010', 'SharkAttack'])
# sequence_0020 = QtWidgets.QTreeWidgetItem(tree_widget, ['0020', 'Beach'])
# shot_020 = QtWidgets.QTreeWidgetItem(sequence_0020, ['020', 'Arrival'])

# # Images
# image = QtGui.QImage(50, 50, QtGui.QImage.Format_Indexed8) # 50, 50 is the sizes
# image.fill(QtGui.qRgb(10, 10, 10)) # A default background colour (not required)
# image.load('C:\\Users\\francois.kruger\\Desktop\\test.png')
# # You need to put an image in a label to make it a widget for addWidget
# image_label = QtWidgets.QLabel(' ')
# image_label.setPixmap(QtGui.QPixmap.fromImage(image))
# # Create the layout
# layout = QtWidgets.QVBoxLayout()
# layout.addWidget(image_label)
# layout.setAlignment(QtCore.Qt.AlignCenter) # If you want to centre things, AlignHCenter and AlignVCenter are also options to use

# # Group Boxes
# lay_btn = QtWidgets.QVBoxLayout()
# lay_btn.addWidget(button)
# gbx = QtWidgets.QGroupBox('A group of stuff')
# gbx.setLayout(layout_two)
# lay_main.addWidget(gbx)

# ---------------------------------- Set Tool Tips ----------------------------------

# cancel_button.setToolTip('This is what you get if you hover over the tool')

# ---------------------------------- Set Visibility (show/hide) ----------------------------------

# cancel_button.setVisible(True)
# cancel_button.setVisible(False)

# cancel_button.show()
# cancel_button.hide()

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
# lay_main.setHorizontalSpacing(15)
# lay_main.setVerticalSpacing(20)

# # Set column widths
# lay_main.setColumnMinimumWidth(i, width)

# # Create strech/width values from the columns
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

# # Align the items in the cell
# lay_main.addWidget(cbx_selected, 1, 1)
# vs
# lay_main.addWidget(cbx_selected, 1, 1, 1, 1, QtCore.Qt.AlignCenter)


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
# scroll.setWidgetResizable(True) # This makes the items in the scroll area fill the scroll area (width and hieght)
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

# ---------------------------------- Window close event ----------------------------------

# window = QtWidgets.QWidget()
# window.closeEvent = closeEvent
# def closeEvent(event):
#     print('Window X pressed')

# ---------------------------------- Set Window Flags / Keep Window On Top ----------------------------------

# my_window = QtWidgets.QWidget()
# # Both of these work, in different ways
# my_window.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint) # This causes the window to stay on top of ALL applications
# my_window.setWindowFlags(QtCore.Qt.Tool) # This one is better to use I think

# # In most cases, you need a main window to parent the QtCore.Qt.Tool to, you would do it like this:
# app = QtWidgets.QApplication.instance()
# if not app:
#     app = QtWidgets.QApplication(sys.argv)
# main_window = None
# current_software = self.SAM.Helpful_Code.get_current_software()
# if current_software == 'maya':
#     main_window = next(w for w in app.topLevelWidgets() if w.objectName() == 'MayaWindow')
# if current_software == 'houdini':
#     import hou
#     main_window = hou.qt.mainWindow()
# self.window.setParent(main_window)

# NOTE: You need to do this self.window.setParent(main_window) AND self.window.setWindowFlags(QtCore.Qt.Tool) for it to work correctly

# ---------------------------------- MousePressed/Clicked close event ----------------------------------

# from functools import partial

# widget = QtWidgets.QWidget()
# widget.mousePressEvent = partial(my_function, 'some_value')

# def my_function(some_value, QMouseEvent):
#     print(some_value)

# ---------------------------------- Delete/Remove Layouts and Widgets ----------------------------------

# # For widgets
# layout.removeWidget(your_widget)
# your_widget = QtWidgets.QWidget()
# lay_main.addWidget(your_widget)


# # For layouts
# # This is a little bit more complex but you HAVE to do it this way (you can't do it like the above, it will cause a lot of issues even though it might work)
# # Here we basically loop through the layout, delete all its children, and then delete it self

# # Delete old layout and all its children
# if self.lay_assets.count():
#     self.U_delete_layout_children(self.lay_assets)
#     self.lay_assets.deleteLater()

# # Reload the assets list
# self.lay_assets = self.B_asset_list()
# self.lay_main.insertLayout(1, self.lay_assets)

# def U_delete_layout_children(layout):
#     """
#         This will run through a layout item and delete all of it's children
#     """
#     if layout is not None:
#         while layout.count():
#             item = layout.takeAt(0)
#             widget = item.widget()
#             if widget is not None:
#                 widget.deleteLater()
#             else:
#                 self.U_delete_layout_children(item.layout())

# ---------------------------------- Loading bar ----------------------------------

# import sys
# from PySide2 import QtCore, QtGui, QtWidgets

# class LoadingBar:
#     def __init__(self):
#         self.app = QtWidgets.QApplication.instance()
#         if not self.app:
#             self.app = QtWidgets.QApplication(sys.argv)

#         self.progress_bar = QtWidgets.QProgressBar()

#         layout = QtWidgets.QVBoxLayout()
#         layout.addWidget(self.progress_bar)

#         self.window = QtWidgets.QWidget()
#         self.window.setLayout(layout)
#         # self.window.closeEvent = self.closeEvent # This seems to exit Maya for some reason
#         self.window.show()

#     def update(self, value):
#         if value >= 100:
#             self.window.close()
#         else:
#             self.progress_bar.setValue(value)
#             self.app.processEvents()

#     def closeEvent(self, event):
#         sys.exit()

# # Using the class:

# import time
# loading_bar = LoadingBar()
# completed = 0
# while completed < 100:
#     completed += 10
#     loading_bar.update(completed)
#     time.sleep(1)

# ---------------------------------- Delete already running windows ----------------------------------

# # Delete the window if it is already running
# window_name = 'SAM_QT'
# open_widgets = QtWidgets.QApplication.instance().topLevelWidgets()
# for item in open_widgets:
#     if item.objectName() == window_name:
#         item.deleteLater()

# # For the above to work, you need to set the name on your window as well
# self.window.setObjectName(window_name)

# ---------------------------------- Horizontal Line ----------------------------------

# This just creates a horizontal line
# frm_line = QtWidgets.QFrame()
# frm_line.setFrameShape(QtWidgets.QFrame.HLine)
# frm_line.setFrameShadow(QtWidgets.QFrame.Sunken)
# layout.addWidget(frm_line)

# ---------------------------------- Dropdown Menu Push Button ----------------------------------

# from PySide2 import QtCore, QtGui, QtWidgets

# def menu_clicked(menu_item):
#     print(menu_item)

# my_menu = QtWidgets.QMenu()
# my_menu.triggered.connect(lambda x: menu_clicked(x.text()))
# my_menu.addAction('test')

# button1 = QtWidgets.QPushButton()
# button1.setFixedWidth(18)
# button1.setMenu(my_menu)

# layout = QtWidgets.QVBoxLayout()
# layout.addWidget(button1)

# window = QtWidgets.QWidget()
# window.resize(800, 600)
# window.setLayout(layout)
# window.show()

# ---------------------------------- Dropdown Menu Push Button ----------------------------------

# https://stackoverflow.com/questions/2052907/qt-repaint-redraw-update-do-something

# Repaint / Update / Redraw the UI
# You can call "repaint" on most QT controls, such as:
# button1.repaint()

# ---------------------------------- SetData / Set Data ----------------------------------

# # RUN IN MAYA
# from PySide2 import QtCore, QtGui, QtWidgets

# things = {
#     "one": "the/path/to/one.ma",
#     "two": "the/path/to/two.ma",
#     "three": "the/path/to/three.ma",
# }
# list_widget = QtWidgets.QListWidget()
# for key, value in things.items():
#     item = QtWidgets.QListWidgetItem(key)
#     # This number can be anything, it's like a memory pointer
#     # Just don't reuse it somewhere else for other data
#     item.setData(99, value)  
#     list_widget.addItem(item)

# layout = QtWidgets.QVBoxLayout()
# layout.addWidget(list_widget)

# window = QtWidgets.QWidget()
# window.setLayout(layout)
# window.show()

# def list_item_clicked():
#     list_item = list_widget.currentItem()
#     print(list_item.data(99))

# list_widget.itemClicked.connect(
#     list_item_clicked
# )