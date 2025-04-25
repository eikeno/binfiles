#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Computes the complementary color in hex notation
# Can be useful used alongside https://www.npmjs.com/package/parker for CSS tasks.

import sys
from colorsys import rgb_to_hsv, hsv_to_rgb
from colormap import rgb2hex, hex2rgb
from typing import List, Tuple

def complementary(r: int, g: int, b: int) -> tuple[float, float, float]:
   """returns RGB components of complementary color"""
   hsv = rgb_to_hsv(r, g, b)
   return hsv_to_rgb((hsv[0] + 0.5) % 1, hsv[1], hsv[2])

def rgb_complementary(hexa: str) -> str:
   r, g, b = hex2rgb(hexa)
   R, G, B = complementary(r, g, b)

   return rgb2hex(int(R), int(G), int(B))

if __name__ == '__main__':
   print(rgb_complementary(sys.argv[1]))



