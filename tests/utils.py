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
