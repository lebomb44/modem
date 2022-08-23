#! /usr/bin/env python3
# coding: utf-8


""" Modem main """


import signal
import sys
import time

import fct
import lbsms



sms=lbsms.Sms("ttyUSB7")


def exit():
    """ Stop SMS thread """
    fct.log("Stopping Modem")
    sms.stop()
    time.sleep(2.0)


def signal_term_handler(signal_, frame_):
    """ Capture Ctrl+C signal and exit program """
    fct.log('Got SIGTERM, exiting...')
    exit()
    sys.exit(0)


if __name__ == '__main__':
    signal.signal(signal.SIGTERM, signal_term_handler)
    sms.start()
    fct.log("Modem started")
    try:
        pass
    except KeyboardInterrupt:
        exit()

