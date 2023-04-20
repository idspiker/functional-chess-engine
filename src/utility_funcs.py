from functools import reduce


def apply_functions(functions, params, results=tuple()):
    """
    Opposite of map - calls every function with the given values and 
    returns the results in a tuple
    """
    if len(functions) == 0:
        return results

    return apply_functions(
        functions[1:], params, (*results, functions[0](*params))
    )


def check_conditions(functions, params):
    return reduce(lambda x, y: x or y, apply_functions(functions, params))
