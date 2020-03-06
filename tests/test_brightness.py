from string import Template

import pytest

import unipixel

from . import resources
from . import utils


def test_brightness(test_strip, capsys):
    test_strip, params = test_strip

    if params["pixel_order"] == unipixel.RGB:
        test_data = zip(resources.RGB, resources.RGB)

    elif params["pixel_order"] == unipixel.GRB:
        test_data = zip(resources.GRB, resources.RGB)

    elif params["pixel_order"] == unipixel.RGBW:
        test_data = zip(resources.RGBW["input"], resources.RGBW["output"])

    elif params["pixel_order"] == unipixel.GRBW:
        test_data = zip(resources.GRBW, resources.RGBW["output"])

    elif params["pixel_order"] is None:
        test_data = zip(resources.GRBW, resources.RGBW["output"])

    else:
        if not isinstance(params["pixel_order"], tuple) and params["pixel_order"] is not None:
            raise TypeError("pixel_order must be a tuple or None")
        
        raise ValueError("Unknown pixel_order")

    if params["pixel_order"] is None and params["bpp"] < 4:
        case = pytest.raises(ValueError)
    else:
        case = utils.nullcontext()

    with case:
        pixel_template = Template(u"\x1b[38;2;${R};${G};${B}m\u2588\x1b[0m")

        for (input_color, output_color) in test_data:
            test_strip.fill(input_color)
            r, g, b = output_color
            brightness = 0.0
            for i in range(4):
                brightness = round(brightness + 0.25, 2)
                # Clear stdout
                capsys.readouterr()
                test_strip.brightness = brightness

                if not params["auto_write"]:
                    test_strip.show()

                out, _ = capsys.readouterr()
                expected = "\r" + pixel_template.substitute(R=int(r*brightness), G=int(g*brightness), B=int(b*brightness)) * 16

                assert out == expected
