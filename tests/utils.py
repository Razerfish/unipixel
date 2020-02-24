import itertools

def product_dict(**kwargs):
    keys = kwargs.keys()
    vals = kwargs.values()

    product = []
    for item in itertools.product(*vals):
        product.append(dict(zip(keys, item)))

    return product

