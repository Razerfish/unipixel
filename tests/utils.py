"""
Testing utilities for Unipixel
"""
import itertools

def product_dict(**kwargs):
    """
    Returns the cartesian product of a dict of lists.
    """
    keys = kwargs.keys()
    vals = kwargs.values()

    product = []
    for item in itertools.product(*vals):
        product.append(dict(zip(keys, item)))

    return product

# I know that contextlib contains a nullcontext class but it isn't supported until python3.7
# pylint: disable=invalid-name,missing-class-docstring
class nullcontext():
    def __enter__(self):
        return None
    def __exit__(self, exc_type, exc_value, traceback):
        return False
# pylint: enable=invalid-name,missing-class-docstring
