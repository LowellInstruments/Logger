# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'options.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(440, 320)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(440, 320))
        Dialog.setMaximumSize(QtCore.QSize(440, 320))
        Dialog.setModal(True)
        self.pushButton_save = QtWidgets.QPushButton(Dialog)
        self.pushButton_save.setGeometry(QtCore.QRect(270, 290, 75, 23))
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton_cancel = QtWidgets.QPushButton(Dialog)
        self.pushButton_cancel.setGeometry(QtCore.QRect(360, 290, 75, 23))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.pushButton_defaults = QtWidgets.QPushButton(Dialog)
        self.pushButton_defaults.setGeometry(QtCore.QRect(10, 290, 101, 23))
        self.pushButton_defaults.setObjectName("pushButton_defaults")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 421, 271))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 451, 141))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton_iso8601_time = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_iso8601_time.setChecked(True)
        self.radioButton_iso8601_time.setObjectName("radioButton_iso8601_time")
        self.buttonGroup = QtWidgets.QButtonGroup(Dialog)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton_iso8601_time)
        self.gridLayout.addWidget(self.radioButton_iso8601_time, 0, 0, 1, 1)
        self.radioButton_legacy_time = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_legacy_time.setObjectName("radioButton_legacy_time")
        self.buttonGroup.addButton(self.radioButton_legacy_time)
        self.gridLayout.addWidget(self.radioButton_legacy_time, 1, 0, 1, 1)
        self.radioButton_elapsed_time = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_elapsed_time.setObjectName("radioButton_elapsed_time")
        self.buttonGroup.addButton(self.radioButton_elapsed_time)
        self.gridLayout.addWidget(self.radioButton_elapsed_time, 2, 0, 1, 1)
        self.radioButton_posix_time = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_posix_time.setObjectName("radioButton_posix_time")
        self.buttonGroup.addButton(self.radioButton_posix_time)
        self.gridLayout.addWidget(self.radioButton_posix_time, 3, 0, 1, 1)
        self.checkBox_average_bursts = QtWidgets.QCheckBox(self.tab)
        self.checkBox_average_bursts.setGeometry(QtCore.QRect(20, 170, 201, 17))
        self.checkBox_average_bursts.setChecked(True)
        self.checkBox_average_bursts.setObjectName("checkBox_average_bursts")
        self.checkBox_declination = QtWidgets.QCheckBox(self.tab)
        self.checkBox_declination.setGeometry(QtCore.QRect(20, 200, 331, 17))
        self.checkBox_declination.setObjectName("checkBox_declination")
        self.lineEdit_declination = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_declination.setEnabled(False)
        self.lineEdit_declination.setGeometry(QtCore.QRect(360, 200, 31, 20))
        self.lineEdit_declination.setObjectName("lineEdit_declination")
        self.tabWidget.addTab(self.tab, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.tab_4)
        self.radioButton_5.setGeometry(QtCore.QRect(20, 20, 251, 17))
        self.radioButton_5.setChecked(True)
        self.radioButton_5.setObjectName("radioButton_5")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(Dialog)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.radioButton_5)
        self.radioButton_6 = QtWidgets.QRadioButton(self.tab_4)
        self.radioButton_6.setGeometry(QtCore.QRect(20, 50, 171, 17))
        self.radioButton_6.setObjectName("radioButton_6")
        self.buttonGroup_2.addButton(self.radioButton_6)
        self.lineEdit = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit.setGeometry(QtCore.QRect(40, 80, 231, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_browse = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_browse.setGeometry(QtCore.QRect(280, 80, 25, 23))
        self.pushButton_browse.setMaximumSize(QtCore.QSize(25, 16777215))
        self.pushButton_browse.setObjectName("pushButton_browse")
        self.tabWidget.addTab(self.tab_4, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.checkBox_declination.toggled['bool'].connect(self.lineEdit_declination.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_save.setText(_translate("Dialog", "Save"))
        self.pushButton_cancel.setText(_translate("Dialog", "Cancel"))
        self.pushButton_defaults.setText(_translate("Dialog", "Restore Defaults"))
        self.groupBox.setTitle(_translate("Dialog", "Time Format"))
        self.radioButton_iso8601_time.setText(_translate("Dialog", "ISO 8601 (yyyy-mm-ddTHH:MM:SS.SSS)"))
        self.radioButton_legacy_time.setText(_translate("Dialog", "Legacy (yyyy-mm-dd, HH:MM:SS.SSS)"))
        self.radioButton_elapsed_time.setText(_translate("Dialog", "Elapsed Time (seconds)"))
        self.radioButton_posix_time.setToolTip(_translate("Dialog", "UTC (no time zone adjustment)"))
        self.radioButton_posix_time.setText(_translate("Dialog", "POSIX Time Stamp (seconds since Jan 1, 1970)"))
        self.checkBox_average_bursts.setText(_translate("Dialog", "Average Bursts (recommended)"))
        self.checkBox_declination.setText(_translate("Dialog", "Apply declination adjustment to Current and Heading (degrees)"))
        self.lineEdit_declination.setText(_translate("Dialog", "0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "General"))
        self.radioButton_5.setText(_translate("Dialog", "Use Factory Calibration Values"))
        self.radioButton_6.setText(_translate("Dialog", "Use Custom Calibration File"))
        self.pushButton_browse.setText(_translate("Dialog", "..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "Calibration Coefficients (advanced)"))

from . import icons_rc
