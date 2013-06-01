# Copyright (c) 2013 Ondrej Kipila <ok100 at lavabit dot com>
# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING file for more details.

import argparse
import subprocess


def check_output(command):
    return subprocess.check_output(command, shell=True).decode()


def parse_args():
    parser = argparse.ArgumentParser(prog='lyvi')
    parser.add_argument('command', nargs='?', help='send a command to player')
    parser.add_argument('-c', '--config-file', help='path to an alternate config file')
    parser.add_argument('-d', '--debug', help='enable debug mode', action='store_true')
    parser.add_argument('-l', '--list-players', help='print a list of supported players', action='store_true')
    parser.add_argument('-v', '--version', help='print version information', action='store_true')
    return parser.parse_args()


def running(process):
    return True if process in check_output('ps -C %s' % process) else False