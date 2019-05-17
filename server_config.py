# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'server_config.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ServerConfigDlg(object):
    def setupUi(self, ServerConfigDlg):
        ServerConfigDlg.setObjectName("ServerConfigDlg")
        ServerConfigDlg.resize(260, 165)
        ServerConfigDlg.setMinimumSize(QtCore.QSize(260, 165))
        ServerConfigDlg.setMaximumSize(QtCore.QSize(260, 165))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ServerConfigDlg.setWindowIcon(icon)
        self.widget = QtWidgets.QWidget(ServerConfigDlg)
        self.widget.setGeometry(QtCore.QRect(10, 0, 241, 161))
        self.widget.setObjectName("widget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.widget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(-1, 9, 71, 101))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.host_str = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.host_str.setObjectName("host_str")
        self.verticalLayout_2.addWidget(self.host_str)
        self.port_str = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.port_str.setObjectName("port_str")
        self.verticalLayout_2.addWidget(self.port_str)
        self.username_str = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.username_str.setObjectName("username_str")
        self.verticalLayout_2.addWidget(self.username_str)
        self.password_str = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.password_str.setObjectName("password_str")
        self.verticalLayout_2.addWidget(self.password_str)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.widget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(79, 9, 151, 101))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.host_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.host_input.setObjectName("host_input")
        self.verticalLayout_3.addWidget(self.host_input)
        self.port_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.port_input.setObjectName("port_input")
        self.verticalLayout_3.addWidget(self.port_input)
        self.username_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.username_input.setObjectName("username_input")
        self.verticalLayout_3.addWidget(self.username_input)
        self.password_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.password_input.setObjectName("password_input")
        self.verticalLayout_3.addWidget(self.password_input)
        self.connect_pb = QtWidgets.QPushButton(self.widget)
        self.connect_pb.setGeometry(QtCore.QRect(15, 122, 91, 31))
        self.connect_pb.setObjectName("connect_pb")
        self.cancel_pb = QtWidgets.QPushButton(self.widget)
        self.cancel_pb.setGeometry(QtCore.QRect(130, 122, 91, 31))
        self.cancel_pb.setObjectName("cancel_pb")

        self.retranslateUi(ServerConfigDlg)
        self.cancel_pb.clicked.connect(ServerConfigDlg.close)
        QtCore.QMetaObject.connectSlotsByName(ServerConfigDlg)

    def retranslateUi(self, ServerConfigDlg):
        _translate = QtCore.QCoreApplication.translate
        ServerConfigDlg.setWindowTitle(_translate("ServerConfigDlg", "Server Config"))
        self.host_str.setText(_translate("ServerConfigDlg", "<html><head/><body><p align=\"center\">Host</p></body></html>"))
        self.port_str.setText(_translate("ServerConfigDlg", "<html><head/><body><p align=\"center\">Port</p></body></html>"))
        self.username_str.setText(_translate("ServerConfigDlg", "<html><head/><body><p align=\"center\">UserName</p></body></html>"))
        self.password_str.setText(_translate("ServerConfigDlg", "<html><head/><body><p align=\"center\">Password</p></body></html>"))
        self.connect_pb.setText(_translate("ServerConfigDlg", "Connect"))
        self.cancel_pb.setText(_translate("ServerConfigDlg", "Cancel"))

