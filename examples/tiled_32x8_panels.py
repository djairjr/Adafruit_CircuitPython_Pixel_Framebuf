# SPDX-FileCopyrightText: 2020 Melissa LeBlanc-Williams, written for Adafruit Industries
# SPDX-License-Identifier: MIT
"""
This example runs on an Seeed Xiao RP2040
"""
import board
import neopixel

# My custom version
from tile_framebuf import TileFramebuffer

pixel_pin = board.D6
pixel_width = 32
pixel_height = 8
num_tiles = 2

pixels = neopixel.NeoPixel(
    pixel_pin,
    pixel_width * pixel_height * num_tiles, # dont forget to multiply for num_tiles
    brightness=0.1,
    auto_write=False,
)

pixel_framebuf = TileFramebuffer(
    pixels,
    pixel_width,
    pixel_height,
    num_tiles,
)

pixel_framebuf.fill(0x000088)
pixel_framebuf.pixel(5, 1, 0xFFFF00)
# Drawing a diagonal line in screen
pixel_framebuf.line(0, 0, 31, 15, 0x00FF00)
pixel_framebuf.display()
