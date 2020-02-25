# pylint: disable=missing-module-docstring,missing-function-docstring,unused-import,wildcard-import
from string import Template

import pytest

import unipixel

from . import resources
from . import utils


def run_fill(test_strip, input_set, output_set, auto_write, capsys):
    for _, (input_color, output_color) in enumerate(zip(input_set, output_set)):
        test_strip.fill(input_color)
        if not auto_write:
            test_strip.show()
        out, _ = capsys.readouterr()

        expected = Template(u"\x1b[38;2;${R};${G};${B}m\u2588\x1b[0m")
        r, g, b = output_color
        expected = expected.substitute(R=r, G=g, B=b)
        expected = "\r" + expected * 10

        yield (out, expected)


def test_fill(test_strip, capsys):
    test_strip, input_set, output_set, params = test_strip

    if params["pixel_order"] is None and params["bpp"] < 4:
        with pytest.raises(ValueError):
            for _ in run_fill(test_strip, input_set, output_set, params["auto_write"], capsys):
                pass
    else:
        for out, expected in run_fill(test_strip, input_set, output_set,
                                      params["auto_write"], capsys):
            assert out == expected
