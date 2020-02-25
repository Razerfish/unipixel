# pylint: disable=missing-module-docstring
import pytest

import unipixel

from . import utils

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

    return (strip, param)
