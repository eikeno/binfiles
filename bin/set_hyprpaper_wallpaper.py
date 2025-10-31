#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Accepts a filename as arguement, and will symlink it to the file defined
# by __DEFWALLP__ and use hyprctl to preload and display the new image.
# If you want the change to permanent, modify default hyprpaper configuration
# to use value of __DEFWALLP__ as default image.
# Eikeno 2025-10-31

import os
import subprocess
import sys

__DEFWALLP__ = "~/.hypr_wallpaper.default"


def usage():
    print("set_wallpaper [FILENAME]")
    print(
        """
Make sure to create a file or symlink .hypr_wallpaper.default
containing or pointing to a valid wallpaper image."""
    )
    sys.exit(1)


def runproc(cmd_l):
    process = subprocess.run(
        cmd_l,
        capture_output=True,
    )
    return process.stdout


def start():
    if not os.path.exists(os.path.expanduser(__DEFWALLP__)):
        usage()
        sys.exit(1)
    else:
        print("ok")


def check_image(imagefile):
    if not os.path.exists(imagefile.strip()):
        raise RuntimeError(f"File Not found: {imagefile}.")
    return True


def unlink_default():
    f = os.path.expanduser(__DEFWALLP__).strip()
    if os.path.exists(f):
        os.unlink(f)
    return True


def setlink(imagefile):
    f = os.path.expanduser(__DEFWALLP__).strip()
    os.symlink(imagefile, f)
    return True


def update():
    f = os.path.expanduser(__DEFWALLP__).strip()
    t = os.readlink(f).strip()

    o1 = runproc(["/usr/bin/hyprctl", "hyprpaper", "preload", "%s" % t])
    o2 = runproc(["/usr/bin/hyprctl", "hyprpaper", "wallpaper", f"HDMI-A-1,", "%s" % t])

    return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()

    check_image(str(sys.argv[1]).strip())
    unlink_default()
    setlink(sys.argv[1])
    update()
