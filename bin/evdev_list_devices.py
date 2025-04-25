#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Based on  lutris/util/joypad.py

import sys

try:
    import evdev
except ImportError:
    evdev = None
except AttributeError as err:
    # 'evdev' versions 1.5 and earlier are incompatible with Python 3.11
    # and produce this exception; we won't be able to use these.
    sys.stderr.write(f"python3-evdev failed to load, and won't be available: {err}")
    evdev = None

def get_devices() -> None:
    if not evdev:
        sys.stderr.write("python3-evdev not installed, controller support not available")
        sys.exit()

    for dev in evdev.list_devices():
        #print(f"Checking {str(dev)}")
        try:
            print(f"{dev} : {evdev.InputDevice(dev).fd}")
            print(f"{dev} : {evdev.InputDevice(dev).name}")
        except RuntimeError:
            pass
    return None

if __name__ == '__main__':
    get_devices()
