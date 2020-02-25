# pylint: disable=missing-module-docstring
import pytest

import unipixel

from . import utils
from . import resources

PARAMS = utils.product_dict(**{
    "pin": [None],
    "n": [10],
    "auto_write": [True, False],
    "bpp": [3, 4],
    "pixel_order": [unipixel.RGB, unipixel.GRB, unipixel.RGBW, unipixel.GRBW, None]
})

@pytest.fixture(params=PARAMS)
def test_strip(request):
    param = request.param
    strip = unipixel.UniPixel(**param)

    if param["pixel_order"] == unipixel.RGB:
        input_set = resources.RGB
        output_set = resources.RGB

    elif param["pixel_order"] == unipixel.GRB:
        input_set = resources.GRB
        output_set = resources.RGB

    elif param["pixel_order"] == unipixel.RGBW:
        input_set = resources.RGBW["input"]
        output_set = resources.RGBW["output"]

    elif param["pixel_order"] == unipixel.GRBW:
        input_set = resources.GRBW
        output_set = resources.RGBW["output"]

    elif param["pixel_order"] is None:
        input_set = resources.GRBW
        output_set = resources.RGBW["output"]

    else:
        if not isinstance(param["pixel_order"], tuple) and param["pixel_order"] is not None:
            raise TypeError("pixel_order must be a tuple or None")

        raise ValueError("Unknown pixel_order")


    return (strip, input_set, output_set, param)
