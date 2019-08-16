# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer_files/converter.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(782, 493)
        Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout = QtWidgets.QGridLayout(Frame)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(Frame)
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(Frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_2.setHorizontalSpacing(12)
        self.gridLayout_2.setVerticalSpacing(9)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.radioButton_output_directory = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton_output_directory.setObjectName("radioButton_output_directory")
        self.buttonGroup = QtWidgets.QButtonGroup(Frame)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton_output_directory)
        self.gridLayout_2.addWidget(self.radioButton_output_directory, 1, 4, 1, 1)
        self.pushButton_output_options = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_output_options.setObjectName("pushButton_output_options")
        self.gridLayout_2.addWidget(self.pushButton_output_options, 0, 2, 1, 1)
        self.comboBox_tilt_tables = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_tilt_tables.setEnabled(False)
        self.comboBox_tilt_tables.setObjectName("comboBox_tilt_tables")
        self.gridLayout_2.addWidget(self.comboBox_tilt_tables, 1, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.comboBox_output_type = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_output_type.setMinimumSize(QtCore.QSize(200, 0))
        self.comboBox_output_type.setObjectName("comboBox_output_type")
        self.comboBox_output_type.addItem("")
        self.comboBox_output_type.addItem("")
        self.comboBox_output_type.addItem("")
        self.comboBox_output_type.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_output_type, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.frame_3)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 0, 3, 3, 1)
        self.lineEdit_output_folder = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_output_folder.setEnabled(False)
        self.lineEdit_output_folder.setReadOnly(True)
        self.lineEdit_output_folder.setObjectName("lineEdit_output_folder")
        self.gridLayout_2.addWidget(self.lineEdit_output_folder, 1, 5, 1, 1)
        self.pushButton_browse = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_browse.setEnabled(False)
        self.pushButton_browse.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_browse.setObjectName("pushButton_browse")
        self.gridLayout_2.addWidget(self.pushButton_browse, 1, 6, 1, 1)
        self.radioButton_output_same = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton_output_same.setChecked(True)
        self.radioButton_output_same.setObjectName("radioButton_output_same")
        self.buttonGroup.addButton(self.radioButton_output_same)
        self.gridLayout_2.addWidget(self.radioButton_output_same, 0, 4, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_declination = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_declination.setEnabled(False)
        self.lineEdit_declination.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_declination.setObjectName("lineEdit_declination")
        self.horizontalLayout_3.addWidget(self.lineEdit_declination)
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.pushButton_help = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_help.sizePolicy().hasHeightForWidth())
        self.pushButton_help.setSizePolicy(sizePolicy)
        self.pushButton_help.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-help-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_help.setIcon(icon)
        self.pushButton_help.setIconSize(QtCore.QSize(22, 22))
        self.pushButton_help.setFlat(True)
        self.pushButton_help.setObjectName("pushButton_help")
        self.horizontalLayout_3.addWidget(self.pushButton_help)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 2, 1, 1, 2)
        self.gridLayout.addWidget(self.frame_3, 2, 0, 1, 1)
        self.frame = QtWidgets.QFrame(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 40))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(4, 2, -1, 2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_add = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_add.sizePolicy().hasHeightForWidth())
        self.pushButton_add.setSizePolicy(sizePolicy)
        self.pushButton_add.setMinimumSize(QtCore.QSize(0, 0))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-Add File-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_add.setIcon(icon1)
        self.pushButton_add.setIconSize(QtCore.QSize(36, 36))
        self.pushButton_add.setFlat(True)
        self.pushButton_add.setObjectName("pushButton_add")
        self.horizontalLayout.addWidget(self.pushButton_add)
        self.pushButton_remove = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_remove.sizePolicy().hasHeightForWidth())
        self.pushButton_remove.setSizePolicy(sizePolicy)
        self.pushButton_remove.setMinimumSize(QtCore.QSize(0, 0))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-Delete File.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_remove.setIcon(icon2)
        self.pushButton_remove.setIconSize(QtCore.QSize(36, 36))
        self.pushButton_remove.setFlat(True)
        self.pushButton_remove.setObjectName("pushButton_remove")
        self.horizontalLayout.addWidget(self.pushButton_remove)
        self.pushButton_clear = QtWidgets.QPushButton(self.frame)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-remove-property-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_clear.setIcon(icon3)
        self.pushButton_clear.setIconSize(QtCore.QSize(36, 36))
        self.pushButton_clear.setFlat(True)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.horizontalLayout.addWidget(self.pushButton_clear)
        self.pushButton_convert = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_convert.sizePolicy().hasHeightForWidth())
        self.pushButton_convert.setSizePolicy(sizePolicy)
        self.pushButton_convert.setMinimumSize(QtCore.QSize(0, 0))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-Circled Play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_convert.setIcon(icon4)
        self.pushButton_convert.setIconSize(QtCore.QSize(36, 36))
        self.pushButton_convert.setFlat(True)
        self.pushButton_convert.setObjectName("pushButton_convert")
        self.horizontalLayout.addWidget(self.pushButton_convert)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Frame", "Files to Convert"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Frame", "Status"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Frame", "Size"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Frame", "Start Time"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Frame", "Containing Folder"))
        self.radioButton_output_directory.setText(_translate("Frame", "Save output to:"))
        self.pushButton_output_options.setText(_translate("Frame", "Options..."))
        self.label_3.setText(_translate("Frame", "Output type:"))
        self.comboBox_output_type.setItemText(0, _translate("Frame", "Discrete Channels"))
        self.comboBox_output_type.setItemText(1, _translate("Frame", "Current"))
        self.comboBox_output_type.setItemText(2, _translate("Frame", "Compass Heading"))
        self.comboBox_output_type.setItemText(3, _translate("Frame", "Yaw/Pitch/Roll"))
        self.label.setText(_translate("Frame", "Meter Model:"))
        self.pushButton_browse.setText(_translate("Frame", "..."))
        self.radioButton_output_same.setText(_translate("Frame", "Save output to same directory as source files"))
        self.label_2.setText(_translate("Frame", "Declination:"))
        self.label_4.setText(_translate("Frame", "Degrees East"))
        self.pushButton_add.setText(_translate("Frame", "Add file"))
        self.pushButton_remove.setText(_translate("Frame", "Remove File"))
        self.pushButton_clear.setText(_translate("Frame", "Clear List"))
        self.pushButton_convert.setText(_translate("Frame", "Convert"))
        self.pushButton_convert.setShortcut(_translate("Frame", "Ctrl+S"))

from . import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())

