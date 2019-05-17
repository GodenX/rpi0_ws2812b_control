#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     app
   Description :
   Author :       jackie
   date：          2019-05-05 22:44
-------------------------------------------------
   Change Activity:
                   2019-05-05 22:44:
-------------------------------------------------
"""
__author__ = 'jackie'

import logging.handlers
import json
import paho.mqtt.client


class MyMQTTClient(object):
    def __init__(self, client_id=""):
        self._client = paho.mqtt.client.Client(client_id)
        self._client.on_connect = self._on_connect
        self._client.on_message = self._on_message

    def _on_connect(self, client, userdata, flags, rc):
        logging.info("MQTT connected with result code " + str(rc))

    def _on_message(self, client, userdata, msg):
        try:
            var = json.loads(msg.payload.decode("utf-8"))
            logging.debug(var)

        except Exception as e:
            logging.error(e)

    def check_connection(self):
        self.pub("/check_status", "")
        if not self._client.socket():
            try:
                self._client.reconnect()
            except:
                pass
            finally:
                return False
        else:
            return True

    def disconnect(self):
        return self._client.disconnect()

    def connect(self, hostname, port, username="", password=""):
        self._client.username_pw_set(username, password)
        return self._client.connect(hostname, port)

    def sub(self, rx_topic):
        return self._client.subscribe(rx_topic)

    def pub(self, tx_topic, msg):
        return self._client.publish(tx_topic, payload=msg, qos=0, retain=False)

    def run(self):
        self._client.loop_forever()
