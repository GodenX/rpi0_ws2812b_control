#!/usr/bin/python3
"""
-------------------------------------------------
   File Name：     app
   Description :
   Author :       jackie
   date：          2019-05-15 16:44
-------------------------------------------------
   Change Activity:
                   2019-05-15 16:44:
-------------------------------------------------
"""
__author__ = 'jackie'

import sys
import re
import time
import logging.handlers
from PyQt5.QtWidgets import QApplication, QMainWindow, QStyleFactory, QWidget, QPushButton, QMessageBox, QInputDialog, \
    QLabel
from PyQt5 import QtCore
from mainwindow import *
from server_config import *
from mqtt_client import *

logging.getLogger().setLevel(logging.DEBUG)
mqtt = MyMQTTClient()
mqtt_config = {"Host": "", "Port": 0, "Username": "", "Password": ""}


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)

        self.connect_status = QLabel()
        self.connect_status.setText("Disconnected !")
        self.timer_id = None
        self.topic = "/LED0/Rx"
        self.msg = "123"

        self.main_ui.statusBar.addPermanentWidget(self.connect_status)
        self.main_ui.display_pb.clicked.connect(self.send_cmd)
        self.main_ui.actionExit.triggered.connect(QtCore.QCoreApplication.instance().quit)

    def send_cmd(self):
        global mqtt
        reply = mqtt.pub(self.topic, self.msg)
        logging.debug(reply)

    def check_connect_status(self):
        self.timer_id = self.startTimer(1000, timerType=QtCore.Qt.VeryCoarseTimer)

    def timerEvent(self, event):
        global mqtt, mqtt_config
        try:
            if mqtt.check_connection():
                self.connect_status.setText("Connected !")
            else:
                self.connect_status.setText("Disconnected !")
        except:
            self.connect_status.setText("Disconnected !")


class ServerConfig(QMainWindow, Ui_ServerConfigDlg):
    def __init__(self):
        super(ServerConfig, self).__init__()
        self.config_ui = Ui_ServerConfigDlg()
        self.config_ui.setupUi(self)

        self.config_ui.connect_pb.clicked.connect(self.connect2mqtt)

    def connect2mqtt(self):
        global mqtt, mqtt_config
        host_str = self.config_ui.host_input.text()
        port_str = self.config_ui.port_input.text()
        try:
            host = re.search(r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}", host_str).group()
            port = int(re.search(r"\d{1,4}", port_str).group())
            username = self.config_ui.username_input.text()
            password = self.config_ui.password_input.text()
            reply = mqtt.connect(host, port, username, password)
            logging.debug(reply)
            if reply == 0:
                mqtt_config["Host"] = host
                mqtt_config["Port"] = port
                mqtt_config["Username"] = username
                mqtt_config["Password"] = password
                self.close()
        except Exception as e:
            logging.error(e)
            QMessageBox.warning(self, "Error", "Please enter the current Host and Port !", QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Fusion"))

    main = MainWindow()
    server_config = ServerConfig()

    main.main_ui.actionServer.triggered.connect(server_config.show)
    server_config.config_ui.connect_pb.clicked.connect(main.check_connect_status)

    main.show()
    server_config.show()

    sys.exit(app.exec_())
