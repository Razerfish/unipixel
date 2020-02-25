# pylint: disable=missing-module-docstring,missing-function-docstring,unused-import,wildcard-import
from string import Template

import pytest

import unipixel

from . import resources
from . import utils


# I know that contextlib contains a nullcontext class but it isn't supported until python3.7
# pylint: disable=invalid-name,missing-class-docstring
class nullcontext():
    def __enter__(self):
        return None
    def __exit__(self, exc_type, exc_value, traceback):
        return False
# pylint: enable=invalid-name,missing-class-docstring


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
