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

        raise ValueError("Unknown pixel_order")

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


def test_get_index(test_strip):
    test_strip, params = test_strip

    if params["pixel_order"] == unipixel.RGB:
        test_data = resources.index_rgb

    elif params["pixel_order"] == unipixel.GRB:
        test_data = resources.index_grb

    elif params["pixel_order"] == unipixel.RGBW:
        test_data = resources.index_rgbw["input"]

    elif params["pixel_order"] == unipixel.GRBW:
        test_data = resources.index_grbw

    elif params["pixel_order"] is None:
        test_data = resources.index_grbw

    else:
        if not isinstance(params["pixel_order"], tuple) and params["pixel_order"] is not None:
            raise TypeError("pixel_order must be a tuple or None")
        raise ValueError("Unknown pixel order")

    if params["pixel_order"] is None and params["bpp"] < 4:
        case = pytest.raises(ValueError)
    else:
        case = utils.nullcontext()

    with case:
        pixel_template = Template(u"\x1b[38;2;${R};${G};${B}m\u2588\x1b[0m")

        for i in range(len(test_strip)):
            test_strip[i] = test_data[i]

        for i in range(len(test_strip)):
            assert test_strip[i] == test_data[i]


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

        raise ValueError("Unknown pixel_order")

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


def test_set_slice(test_strip, capsys):
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

        raise ValueError("Unknown pixel_order")

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


def test_get_slice(test_strip):
    test_strip, params = test_strip

    if params["pixel_order"] == unipixel.RGB:
        test_data = resources.index_rgb

    elif params["pixel_order"] == unipixel.GRB:
        test_data = resources.index_grb

    elif params["pixel_order"] == unipixel.RGBW:
        test_data = resources.index_rgbw["input"]

    elif params["pixel_order"] == unipixel.GRBW:
        test_data = resources.index_grbw

    elif params["pixel_order"] is None:
        test_data = resources.index_grbw

    else:
        if not isinstance(params["pixel_order"], tuple) and params["pixel_order"] is not None:
            raise TypeError("pixel_order must be a tuple or None")
        raise ValueError("Unknown pixel order")

    if params["pixel_order"] is None and params["bpp"] < 4:
        case = pytest.raises(ValueError)
    else:
        case = utils.nullcontext()

    with case:
        for i in range(len(test_strip)):
            test_strip[i] = test_data[i]

        assert test_strip[1:15] == test_data[1:15]
        assert test_strip[0:-1] == test_data[0:-1]
        assert test_strip[0:7] == test_data[0:7]
        assert test_strip[8:15] == test_data[8:15]
        assert test_strip[8:-1] == test_data[8:-1]
