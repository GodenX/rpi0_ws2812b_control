# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(310, 285)
        MainWindow.setMinimumSize(QtCore.QSize(310, 285))
        MainWindow.setMaximumSize(QtCore.QSize(310, 285))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("app.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(32, 32))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 291, 231))
        self.widget.setObjectName("widget")
        self.device_select = QtWidgets.QComboBox(self.widget)
        self.device_select.setGeometry(QtCore.QRect(60, 1, 121, 21))
        self.device_select.setObjectName("device_select")
        self.device_select.addItem("")
        self.device_select.addItem("")
        self.device_select.addItem("")
        self.led_switch = QtWidgets.QPushButton(self.widget)
        self.led_switch.setEnabled(False)
        self.led_switch.setGeometry(QtCore.QRect(200, 0, 81, 23))
        self.led_switch.setCheckable(True)
        self.led_switch.setObjectName("led_switch")
        self.device_str = QtWidgets.QLabel(self.widget)
        self.device_str.setGeometry(QtCore.QRect(10, 3, 71, 21))
        self.device_str.setObjectName("device_str")
        self.brightness_str = QtWidgets.QLabel(self.widget)
        self.brightness_str.setGeometry(QtCore.QRect(10, 40, 71, 21))
        self.brightness_str.setObjectName("brightness_str")
        self.brightness_dp = QtWidgets.QLabel(self.widget)
        self.brightness_dp.setGeometry(QtCore.QRect(260, 40, 21, 21))
        self.brightness_dp.setObjectName("brightness_dp")
        self.brightness_slider = QtWidgets.QSlider(self.widget)
        self.brightness_slider.setGeometry(QtCore.QRect(90, 41, 151, 21))
        self.brightness_slider.setMaximum(48)
        self.brightness_slider.setPageStep(8)
        self.brightness_slider.setOrientation(QtCore.Qt.Horizontal)
        self.brightness_slider.setObjectName("brightness_slider")
        self.effect01_pb = QtWidgets.QPushButton(self.widget)
        self.effect01_pb.setGeometry(QtCore.QRect(120, 160, 41, 31))
        self.effect01_pb.setCheckable(True)
        self.effect01_pb.setObjectName("effect01_pb")
        self.effect02_pb = QtWidgets.QPushButton(self.widget)
        self.effect02_pb.setGeometry(QtCore.QRect(180, 160, 41, 31))
        self.effect02_pb.setCheckable(True)
        self.effect02_pb.setObjectName("effect02_pb")
        self.effect03_pb = QtWidgets.QPushButton(self.widget)
        self.effect03_pb.setGeometry(QtCore.QRect(240, 160, 41, 31))
        self.effect03_pb.setCheckable(True)
        self.effect03_pb.setObjectName("effect03_pb")
        self.customize_display_pb = QtWidgets.QPushButton(self.widget)
        self.customize_display_pb.setGeometry(QtCore.QRect(120, 80, 161, 21))
        self.customize_display_pb.setObjectName("customize_display_pb")
        self.str_input = QtWidgets.QLineEdit(self.widget)
        self.str_input.setGeometry(QtCore.QRect(120, 120, 111, 21))
        self.str_input.setObjectName("str_input")
        self.mode2_select = QtWidgets.QRadioButton(self.widget)
        self.mode2_select.setGeometry(QtCore.QRect(10, 165, 91, 21))
        self.mode2_select.setObjectName("mode2_select")
        self.mode1_select = QtWidgets.QRadioButton(self.widget)
        self.mode1_select.setGeometry(QtCore.QRect(10, 120, 91, 21))
        self.mode1_select.setObjectName("mode1_select")
        self.mode0_select = QtWidgets.QRadioButton(self.widget)
        self.mode0_select.setGeometry(QtCore.QRect(10, 80, 91, 21))
        self.mode0_select.setObjectName("mode0_select")
        self.display_pb = QtWidgets.QPushButton(self.widget)
        self.display_pb.setEnabled(False)
        self.display_pb.setGeometry(QtCore.QRect(50, 200, 191, 31))
        self.display_pb.setObjectName("display_pb")
        self.str_color_pb = QtWidgets.QPushButton(self.widget)
        self.str_color_pb.setGeometry(QtCore.QRect(240, 120, 41, 23))
        self.str_color_pb.setObjectName("str_color_pb")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 310, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu_file = QtWidgets.QMenu(self.menuBar)
        self.menu_file.setObjectName("menu_file")
        self.menu_help = QtWidgets.QMenu(self.menuBar)
        self.menu_help.setObjectName("menu_help")
        MainWindow.setMenuBar(self.menuBar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionServer = QtWidgets.QAction(MainWindow)
        self.actionServer.setObjectName("actionServer")
        self.actionPowerOFF = QtWidgets.QAction(MainWindow)
        self.actionPowerOFF.setObjectName("actionPowerOFF")
        self.actionReboot = QtWidgets.QAction(MainWindow)
        self.actionReboot.setObjectName("actionReboot")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setWhatsThis("")
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menu_file.addAction(self.actionServer)
        self.menu_file.addAction(self.actionReboot)
        self.menu_file.addAction(self.actionPowerOFF)
        self.menu_file.addAction(self.actionExit)
        self.menu_help.addAction(self.actionHelp)
        self.menu_help.addAction(self.actionAbout)
        self.menuBar.addAction(self.menu_file.menuAction())
        self.menuBar.addAction(self.menu_help.menuAction())

        self.retranslateUi(MainWindow)
        self.brightness_slider.valueChanged['int'].connect(self.brightness_dp.setNum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LEDControlTool"))
        self.device_select.setStatusTip(_translate("MainWindow", "Select the device."))
        self.device_select.setItemText(0, _translate("MainWindow", "LED0"))
        self.device_select.setItemText(1, _translate("MainWindow", "LED1"))
        self.device_select.setItemText(2, _translate("MainWindow", "LED2"))
        self.led_switch.setStatusTip(_translate("MainWindow", "ON/OFF switch."))
        self.led_switch.setText(_translate("MainWindow", "OFF"))
        self.device_str.setText(_translate("MainWindow", "<html><head/><body><p>Device</p></body></html>"))
        self.brightness_str.setText(_translate("MainWindow", "<html><head/><body><p>Brightness</p></body></html>"))
        self.brightness_dp.setText(_translate("MainWindow", "0"))
        self.brightness_slider.setStatusTip(_translate("MainWindow", "Change the brightness."))
        self.effect01_pb.setStatusTip(_translate("MainWindow", "Display with effect01."))
        self.effect01_pb.setText(_translate("MainWindow", "01"))
        self.effect02_pb.setStatusTip(_translate("MainWindow", "Display with effect02."))
        self.effect02_pb.setText(_translate("MainWindow", "02"))
        self.effect03_pb.setStatusTip(_translate("MainWindow", "Display with effect03."))
        self.effect03_pb.setText(_translate("MainWindow", "03"))
        self.customize_display_pb.setStatusTip(_translate("MainWindow", "Customize Display."))
        self.customize_display_pb.setText(_translate("MainWindow", "Customize Display"))
        self.str_input.setStatusTip(_translate("MainWindow", "Enter the string to display."))
        self.mode2_select.setStatusTip(_translate("MainWindow", "Display with mode2."))
        self.mode2_select.setText(_translate("MainWindow", "Mode2"))
        self.mode1_select.setStatusTip(_translate("MainWindow", "Display with mode1."))
        self.mode1_select.setText(_translate("MainWindow", "Mode1"))
        self.mode0_select.setStatusTip(_translate("MainWindow", "Display with mode0."))
        self.mode0_select.setText(_translate("MainWindow", "Mode0"))
        self.display_pb.setStatusTip(_translate("MainWindow", "Display."))
        self.display_pb.setText(_translate("MainWindow", "Display"))
        self.str_color_pb.setStatusTip(_translate("MainWindow", "Set the color for string."))
        self.str_color_pb.setText(_translate("MainWindow", "color"))
        self.menu_file.setTitle(_translate("MainWindow", "File"))
        self.menu_help.setTitle(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setStatusTip(_translate("MainWindow", "Exit."))
        self.actionServer.setText(_translate("MainWindow", "Server Config.."))
        self.actionServer.setStatusTip(_translate("MainWindow", "Server Config."))
        self.actionPowerOFF.setText(_translate("MainWindow", "PowerOFF"))
        self.actionPowerOFF.setStatusTip(_translate("MainWindow", "Shutdown the Raspberry Pi."))
        self.actionReboot.setText(_translate("MainWindow", "System Reboot"))
        self.actionReboot.setStatusTip(_translate("MainWindow", "Reboot the Raspberry Pi."))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionHelp.setStatusTip(_translate("MainWindow", "Help."))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionAbout.setStatusTip(_translate("MainWindow", "About."))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save the config."))

