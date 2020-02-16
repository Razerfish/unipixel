# pylint: disable=missing-module-docstring,missing-function-docstring,unused-import
from string import Template

import pytest

import unipixel
from testing_resources import RGB, RGBW


def test_rgb(capsys):
    test_strip = unipixel.UniPixel(None, 10, bpp=3, auto_write=False, pixel_order=unipixel.RGB)

    for color in RGB:
        test_strip.fill(color)
        test_strip.show()
        out, _ = capsys.readouterr()

        expected = Template(u"\x1b[38;2;${R};${G};${B}m\u2588\x1b[0m")
        expected = expected.substitute(R=color[0], G=color[1], B=color[2])
        expected = "\r" + expected * 10

        assert out == expected

def test_rgbw(capsys):
    test_strip = unipixel.UniPixel(None, 10, bpp=4, auto_write=False, pixel_order=unipixel.RGBW)

    rgbw_input = RGBW["input"]
    rgbw_output = RGBW["output"]

    for i, _ in enumerate(rgbw_input):
        test_strip.fill(rgbw_input[i])
        test_strip.show()
        out, __ = capsys.readouterr()

        expected = Template(u"\x1b[38;2;${R};${G};${B}m\u2588\x1b[0m")
        r, g, b = rgbw_output[i]
        expected = expected.substitute(R=r, G=g, B=b)
        expected = "\r" + expected * 10

        assert out == expected
