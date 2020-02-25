# pylint: disable=missing-module-docstring,missing-function-docstring,unused-import,wildcard-import
from string import Template

import pytest

import unipixel

from . import resources
from . import utils


def test_fill(test_strip, capsys):
    test_strip, params = test_strip

    if params["pixel_order"] == unipixel.RGB:
        input_set = resources.RGB
        output_set = resources.RGB

    elif params["pixel_order"] == unipixel.GRB:
        input_set = resources.GRB
        output_set = resources.RGB

    elif params["pixel_order"] == unipixel.RGBW:
        input_set = resources.RGBW["input"]
        output_set = resources.RGBW["output"]

    elif params["pixel_order"] == unipixel.GRBW:
        input_set = resources.GRBW
        output_set = resources.RGBW["output"]

    elif params["pixel_order"] is None:
        input_set = resources.GRBW
        output_set = resources.RGBW["output"]

    else:
        if not isinstance(params["pixel_order"], tuple) and params["pixel_order"] is not None:
            raise TypeError("pixel_order must be a tuple or None")

        raise ValueError("Unknown pixel_order")

    if params["pixel_order"] is None and params["bpp"] < 4:
        case = pytest.raises(ValueError)
    else:
        case = utils.nullcontext()

    with case:
        for (input_color, output_color) in zip(input_set, output_set):
            test_strip.fill(input_color)
            if not params["auto_write"]:
                test_strip.show()

            out, _ = capsys.readouterr()

            expected = Template(u"\x1b[38;2;${R};${G};${B}m\u2588\x1b[0m")
            r, g, b = output_color
            expected = expected.substitute(R=r, G=g, B=b)
            expected = "\r" + expected * 10

            assert out == expected
