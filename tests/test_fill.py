# pylint: disable=missing-module-docstring,missing-function-docstring,unused-import,wildcard-import
from string import Template
from contextlib import nullcontext

import pytest

import unipixel

from . import resources
from . import utils


def test_fill(test_strip, capsys):
    test_strip, input_set, output_set, params = test_strip

    if params["pixel_order"] is None and params["bpp"] < 4:
        case = pytest.raises(ValueError)
    else:
        case = nullcontext()

    with case:
        for _, (input_color, output_color) in enumerate(zip(input_set, output_set)):
            test_strip.fill(input_color)
            if not params["auto_write"]:
                test_strip.show()

            out, _ = capsys.readouterr()

            expected = Template(u"\x1b[38;2;${R};${G};${B}m\u2588\x1b[0m")
            r, g, b = output_color
            expected = expected.substitute(R=r, G=g, B=b)
            expected = "\r" + expected * 10

            assert out == expected
