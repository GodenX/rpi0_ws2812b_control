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
import os
import json
import logging.handlers
import webbrowser
from PyQt5.QtWidgets import QApplication, QMainWindow, QStyleFactory, QWidget, QPushButton, QMessageBox, QInputDialog, \
    QLabel, QButtonGroup, QColorDialog
from PyQt5 import QtCore, QtGui
from mainwindow import *
from server_config import *
import mqtt_client

logging.getLogger().setLevel(logging.DEBUG)
mqtt = mqtt_client.MyMQTTClient()
version = "v0.2"


class MySignal(QWidget):
    trigger = QtCore.pyqtSignal()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)

        self.connect_status = QLabel()
        self.connect_status.setText("Disconnected !")
        self.disconnect = MySignal()
        self.timer_id = None
        self.retry_count = 0

        self.led_parameter = {"current_led": "LED0", "led_status": {"LED0": False, "LED1": False, "LED2": False},
                              "topic": "/LED0/Rx", "brightness": 0, "payload": None}
        self.led_payload = {"Command": "", "Wait_s": 0, "Value": {}}
        self.mode_payload = {"mode0": "", "mode1": "", "mode2": ""}

        self.main_ui.device_select.currentIndexChanged[str].connect(self.set_device)
        self.main_ui.led_switch.clicked.connect(self.led_switch_control)
        self.main_ui.brightness_slider.valueChanged[int].connect(self.set_brightness)
        self.main_ui.brightness_slider.setValue(40)
        self.mode = QButtonGroup(self)
        self.mode.addButton(self.main_ui.mode0_select, 0)
        self.mode.addButton(self.main_ui.mode1_select, 1)
        self.mode.addButton(self.main_ui.mode2_select, 2)
        self.mode.buttonClicked.connect(self.mode_select)
        self.main_ui.customize_display_pb.clicked.connect(self.mode0_display)
        self.main_ui.str_input.editingFinished.connect(self.mode1_display)
        self.main_ui.str_color_pb.clicked.connect(self.color_dialog)
        self.effect_select = QButtonGroup(self)
        self.effect_select.addButton(self.main_ui.effect01_pb, 3)
        self.effect_select.addButton(self.main_ui.effect02_pb, 4)
        self.effect_select.addButton(self.main_ui.effect03_pb, 5)
        self.effect_select.buttonClicked.connect(self.mode2_display)
        self.main_ui.display_pb.clicked.connect(self.send_cmd)

        self.main_ui.actionReboot.triggered.connect(self.system_reboot)
        self.main_ui.actionPowerOFF.triggered.connect(self.system_halt)
        self.main_ui.actionExit.triggered.connect(self.closeapp)
        self.main_ui.actionHelp.triggered.connect(self.help)
        self.main_ui.actionAbout.triggered.connect(self.about)

        self.disconnect.trigger.connect(self.disconnected)
        self.main_ui.statusBar.addPermanentWidget(self.connect_status)

    def set_device(self, device):
        device_list = {"LED0": "/LED0/Rx", "LED1": "/LED1/Rx", "LED2": "/LED2/Rx"}
        self.led_parameter["current_led"] = device
        self.led_parameter["topic"] = device_list[self.led_parameter["current_led"]]
        logging.debug(self.led_parameter["topic"])
        if self.led_parameter["led_status"][self.led_parameter["current_led"]] != self.main_ui.led_switch.isChecked():
            self.main_ui.led_switch.toggle()
            if self.led_parameter["led_status"][self.led_parameter["current_led"]]:
                self.main_ui.led_switch.setText("ON")
            else:
                self.main_ui.led_switch.setText("OFF")

    def led_switch_control(self):
        if self.main_ui.led_switch.isChecked():
            self.led_parameter["led_status"][self.led_parameter["current_led"]] = True
            self.main_ui.led_switch.setText("ON")
            self.led_parameter["payload"] = '''{"Command":"system_control", "Wait_s":0, "Value":{"cmd":"PowerON"}}'''
        else:
            self.led_parameter["led_status"][self.led_parameter["current_led"]] = False
            self.main_ui.led_switch.setText("OFF")
            self.led_parameter["payload"] = '''{"Command":"system_control", "Wait_s":0, "Value":{"cmd":"PowerOFF"}}'''
        self.send_cmd()

    def set_brightness(self, value):
        self.led_parameter["brightness"] = value
        logging.debug("brightness: %d" % self.led_parameter["brightness"])

    def mode_select(self):
        mode_list = {"0": "mode0", "1": "mode1", "2": "mode2"}
        last_mode = self.led_payload["Command"]
        self.mode_payload[last_mode] = self.led_parameter["payload"]
        self.led_payload["Command"] = mode_list[str(self.sender().checkedId())]
        self.led_parameter["payload"] = self.mode_payload[self.led_payload["Command"]]
        logging.debug(self.led_parameter["payload"])

    def mode0_display(self):
        QMessageBox.information(self, "Help", "Please wait for developing !", QMessageBox.Ok)

    def color_dialog(self):
        try:
            color = QtGui.QColor(QColorDialog.getColor().name())
            color_number = (int(color.green()) * 65536) + (int(color.red()) * 256) + (int(color.blue()))
            self.led_payload["Value"] = {"Brightness": self.led_parameter["brightness"],
                                         "str": self.main_ui.str_input.text(), "color": color_number}
            self.led_parameter["payload"] = json.dumps(self.led_payload)
            logging.debug(self.led_parameter["payload"])
        except Exception as e:
            logging.error(e)
            QMessageBox.warning(self, "Warning", "Color can not be set !", QMessageBox.Ok)

    def mode1_display(self):
        self.led_payload["Value"] = {"Brightness": self.led_parameter["brightness"],
                                     "str": self.main_ui.str_input.text()}
        self.led_parameter["payload"] = json.dumps(self.led_payload)
        logging.debug(self.led_parameter["payload"])

    def mode2_display(self):
        effect_list = {"3": "effect01", "4": "effect02", "5": "effect03"}
        self.led_payload["Value"] = {"Brightness": self.led_parameter["brightness"],
                                     "effect": effect_list[str(self.sender().checkedId())]}
        self.led_parameter["payload"] = json.dumps(self.led_payload)
        logging.debug(self.led_parameter["payload"])

    def send_cmd(self):
        global mqtt
        if self.led_parameter["payload"]:
            reply = mqtt.pub(self.led_parameter["topic"], self.led_parameter["payload"])
            logging.debug("Publish result code: %s" % reply)
        else:
            QMessageBox.warning(self, "Error", "No message can be send !", QMessageBox.Ok)

    def system_reboot(self):
        reply = QMessageBox.question(self, "Confirm it", "The Raspberry Pi will be reboot !",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.led_parameter[
                "payload"] = '''{"Command":"system_control", "Wait_s":0, "Value":{"cmd":"SystemReboot"}}'''
            self.send_cmd()

    def system_halt(self):
        reply = QMessageBox.question(self, "Confirm it",
                                     "The Raspberry Pi will be turned off !\r\nTo restart it , you should disconnect\r\nthe cable of power , then connect it\r\n again !",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.led_parameter["payload"] = '''{"Command":"system_control", "Wait_s":0, "Value":{"cmd":"SystemHalt"}}'''
            self.send_cmd()

    def help(self):
        url = os.path.abspath('.') + "/help.html"
        webbrowser.open_new(url)

    def about(self):
        global version
        QMessageBox.information(self, "About", ("LEDControlTool - " + version), QMessageBox.Ok)

    def check_connect_status(self):
        self.connect_status.setText("Connected !")
        self.timer_id = self.startTimer(5000, timerType=QtCore.Qt.VeryCoarseTimer)
        self.main_ui.led_switch.setEnabled(True)
        self.main_ui.display_pb.setEnabled(True)

    def disconnected(self):
        QMessageBox.warning(self, "Warning", "Lose the connection with server !", QMessageBox.Ok)
        self.main_ui.led_switch.setEnabled(False)
        self.main_ui.display_pb.setEnabled(False)

    def timerEvent(self, event):
        global mqtt
        try:
            reply = mqtt.pub("/check_status", "")
            if reply[0] == 0:
                self.connect_status.setText("Connected !")
                self.retry_count = 0
            else:
                self.retry_count = self.retry_count + 1
                if self.retry_count <= 2:
                    self.connect_status.setText("Disconnected,Retry %d!" % self.retry_count)
                else:
                    self.connect_status.setText("Disconnected !")
                    self.killTimer(self.timer_id)
                    self.retry_count = 0
                    self.disconnect.trigger.emit()
                mqtt.reconnect()
        except Exception as e:
            logging.error(e)
            self.connect_status.setText("Disconnected !")
            self.killTimer(self.timer_id)
            self.retry_count = 0
            self.disconnect.trigger.emit()

    def closeapp(self):
        global mqtt
        reply = QMessageBox.question(self, "Confirm it",
                                     "If you haven't turn off the LED,\r\nit will keep on working !",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            mqtt.disconnect()
            QtCore.QCoreApplication.instance().quit()

    def closeEvent(self, event):
        global mqtt
        reply = QMessageBox.question(self, "Confirm it",
                                     "If you haven't turned the LED off,\r\nit will keep on working !",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            mqtt.disconnect()
            QtCore.QCoreApplication.instance().quit()
        else:
            event.ignore()


class ServerConfig(QMainWindow, Ui_ServerConfigDlg):
    def __init__(self):
        super(ServerConfig, self).__init__()
        self.config_ui = Ui_ServerConfigDlg()
        self.config_ui.setupUi(self)

        self.mqtt_config = {"Host": "", "Port": 0, "Username": "", "Password": ""}
        self.conf_path = os.path.abspath('.') + "/server.conf"
        self.connected = MySignal()

        self.config_ui.connect_pb.clicked.connect(self.connect2mqtt)
        self.connected.trigger.connect(self.save)

    def connect2mqtt(self):
        global mqtt
        host_str = self.config_ui.host_input.text()
        port_str = self.config_ui.port_input.text()
        try:
            self.mqtt_config["Host"] = re.search(r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}", host_str).group()
            self.mqtt_config["Port"] = int(re.search(r"\d{1,4}", port_str).group())
            self.mqtt_config["Username"] = self.config_ui.username_input.text()
            self.mqtt_config["Password"] = self.config_ui.password_input.text()
            reply = mqtt.connect(self.mqtt_config["Host"], self.mqtt_config["Port"], self.mqtt_config["Username"],
                                 self.mqtt_config["Password"])
            logging.debug("MQTT server result code: %s" % reply)
            if reply == 0:
                self.connected.trigger.emit()
                self.close()
        except Exception as e:
            logging.error(e)
            QMessageBox.warning(self, "Error", "Please enter the current Host and Port !", QMessageBox.Ok)

    def show_window(self):
        try:
            if os.path.exists(self.conf_path):
                with open(self.conf_path, "r") as conf:
                    text = conf.read()
                self.mqtt_config = json.loads(text)
                self.config_ui.host_input.setText(self.mqtt_config["Host"])
                self.config_ui.port_input.setText(str(self.mqtt_config["Port"]))
                self.config_ui.username_input.setText(self.mqtt_config["Username"])
                self.config_ui.password_input.setText(self.mqtt_config["Password"])
                logging.debug(self.mqtt_config)
        except Exception as e:
            logging.error(e)
        finally:
            self.show()

    def save(self):
        try:
            with open(self.conf_path, "w+") as conf:
                conf.write(json.dumps(self.mqtt_config))
        except Exception as e:
            logging.error(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Fusion"))

    main = MainWindow()
    server_config = ServerConfig()

    main.main_ui.actionServer.triggered.connect(server_config.show_window)
    main.disconnect.trigger.connect(server_config.show_window)
    server_config.connected.trigger.connect(main.check_connect_status)

    main.show()
    server_config.show_window()

    sys.exit(app.exec_())
