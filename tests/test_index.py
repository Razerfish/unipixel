from string import Template

import pytest

import unipixel

from . import resources
from . import utils


def test_set_index(test_strip, capsys):
    test_strip, params = test_strip

    if params["pixel_order"] == unipixel.RGB:
        test_data = zip(resources.index_rgb, resources.index_rgb)

    elif params["pixel_order"] == unipixel.GRB:
        test_data = zip(resources.index_grb, resources.index_rgb)

    elif params["pixel_order"] == unipixel.RGBW:
        test_data = zip(resources.index_rgbw["input"], resources.index_rgbw["output"])

    elif params["pixel_order"] == unipixel.GRBW:
        test_data = zip(resources.index_grbw, resources.index_rgbw["output"])

    elif params["pixel_order"] is None:
        test_data = zip(resources.index_grbw, resources.index_rgbw["output"])

    else:
        if not isinstance(params["pixel_order"], tuple) and params["pixel_order"] is not None:
            raise TypeError("pixel_order must be a tuple or None")

        raise ValueError("Unkown pixel_order" + str(type(params["pixel_order"])))

    if params["pixel_order"] is None and params["bpp"] < 4:
        case = pytest.raises(ValueError)
    else:
        case = utils.nullcontext()

    with case:
        pixel_template = Template(u"\x1b[38;2;${R};${G};${B}m\u2588\x1b[0m")

        reference_strip = []
        for i in range(16):
            reference_strip.append(pixel_template.substitute(R=0, G=0, B=0))

        for i, (in_color, out_color) in enumerate(test_data):
            r, g, b = out_color
            reference_strip[i] = pixel_template.substitute(R=r, G=g, B=b)

            reference_string = "\r"
            for pixel in reference_strip:
                reference_string += pixel

            test_strip[i] = in_color
            if not params["auto_write"]:
                test_strip.show()

            out, _ = capsys.readouterr()

            assert out == reference_string


def test_set_index_reverse(test_strip, capsys):
    test_strip, params = test_strip

    if params["pixel_order"] == unipixel.RGB:
        test_data = zip(resources.index_rgb, resources.index_rgb)

    elif params["pixel_order"] == unipixel.GRB:
        test_data = zip(resources.index_grb, resources.index_rgb)

    elif params["pixel_order"] == unipixel.RGBW:
        test_data = zip(resources.index_rgbw["input"], resources.index_rgbw["output"])

    elif params["pixel_order"] == unipixel.GRBW:
        test_data = zip(resources.index_grbw, resources.index_rgbw["output"])

    elif params["pixel_order"] is None:
        test_data = zip(resources.index_grbw, resources.index_rgbw["output"])

    else:
        if not isinstance(params["pixel_order"], tuple) and params["pixel_order"] is not None:
            raise TypeError("pixel_order must be a tuple or None")

        raise ValueError("Unkown pixel_order" + str(type(params["pixel_order"])))

    if params["pixel_order"] is None and params["bpp"] < 4:
        case = pytest.raises(ValueError)
    else:
        case = utils.nullcontext()

    with case:
        pixel_template = Template(u"\x1b[38;2;${R};${G};${B}m\u2588\x1b[0m")

        reference_strip = []
        for i in range(16):
            reference_strip.append(pixel_template.substitute(R=0, G=0, B=0))

        for i, (in_color, out_color) in enumerate(test_data):
            r, g, b = out_color
            reference_strip[i - 16] = pixel_template.substitute(R=r, G=g, B=b)

            reference_string = "\r"
            for pixel in reference_strip:
                reference_string += pixel

            test_strip[i] = in_color
            if not params["auto_write"]:
                test_strip.show()

            out, _ = capsys.readouterr()

            assert out == reference_string


def test_slice(test_strip, capsys):
    test_strip, params = test_strip

    if params["pixel_order"] == unipixel.RGB:
        test_data = zip(resources.index_rgb, resources.index_rgb)

    elif params["pixel_order"] == unipixel.GRB:
        test_data = zip(resources.index_grb, resources.index_rgb)

    elif params["pixel_order"] == unipixel.RGBW:
        test_data = zip(resources.index_rgbw["input"], resources.index_rgbw["output"])

    elif params["pixel_order"] == unipixel.GRBW:
        test_data = zip(resources.index_grbw, resources.index_rgbw["output"])

    elif params["pixel_order"] is None:
        test_data = zip(resources.index_grbw, resources.index_rgbw["output"])

    else:
        if not isinstance(params["pixel_order"], tuple) and params["pixel_order"] is not None:
            raise TypeError("pixel_order must be a tuple or None")

        raise ValueError("Unkown pixel_order" + str(type(params["pixel_order"])))

    if params["pixel_order"] is None and params["bpp"] < 4:
        case = pytest.raises(ValueError)
    else:
        case = utils.nullcontext()

    with case:
        pixel_template = Template(u"\x1b[38;2;${R};${G};${B}m\u2588\x1b[0m")

        reference_strip = []
        for i in range(16):
            reference_strip.append(pixel_template.substitute(R=0, G=0, B=0))

        for i, (in_color, out_color) in enumerate(test_data):
            r, g, b = out_color
            reference_strip[1:-1] = [pixel_template.substitute(R=r, G=g, B=b)] * 14

            reference_string = "\r"
            for pixel in reference_strip:
                reference_string += pixel

            test_strip[1:-1] = [in_color] * 14
            if not params["auto_write"]:
                test_strip.show()

            out, _ = capsys.readouterr()

            assert out == reference_string
