#!/usr/bin/env python3
# encoding: utf-8
import os
import LeActList
import threading
import sys
import Serial_Servo_Running as SSR
import time
import config_serial_servo

while True:
    try:
        SSR.runAction('36')
        time.sleep(5)
    except Exception as e:
        print(e)
        break