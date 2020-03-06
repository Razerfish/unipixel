from string import Template

import pytest

import unipixel

from . import utils

def test_deinit(test_strip, capsys):
    test_strip, params = test_strip

    if params["pixel_order"] == unipixel.RGB:
        test_data = (255, 255, 255)

    elif params["pixel_order"] == unipixel.GRB:
        test_data = (255, 255, 255)

    elif params["pixel_order"] == unipixel.RGBW:
        test_data = (255, 255, 255, 255)

    elif params["pixel_order"] == unipixel.GRBW:
        test_data = (255, 255, 255, 255)

    elif params["pixel_order"] is None:
        test_data = (255, 255, 255, 255)

    else:
        if not isinstance(params["pixel_order"], tuple) and params["pixel_order"] is not None:
            raise TypeError("pixel_order must be a tuple or None")

        raise ValueError("Unknown pixel_order")

    if params["pixel_order"] is None and params["bpp"] < 4:
        case = pytest.raises(ValueError)
    else:
        case = utils.nullcontext()

    with case:
        test_strip.fill(test_data)
        if not params["auto_write"]:
            test_strip.show()

        out, _ = capsys.readouterr()

        pixel_template = Template(u"\x1b[38;2;${R};${G};${B}m\u2588\x1b[0m")

        expected = "\r" + pixel_template.substitute(R=255, G=255, B=255) * 16

        assert out == expected

        test_strip.deinit()

        expected = "\r" + pixel_template.substitute(R=0, G=0, B=0) * 16
        expected = expected + "\n"

        out, _ = capsys.readouterr()

        assert out == expected
