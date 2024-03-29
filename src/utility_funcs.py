from functools import reduce, partial


def apply_functions(functions, params, results=tuple()):
    """
    Calls every function with the given values and 
    returns the results in a tuple
    """
    return (
        results 
        if len(functions) == 0 
            else apply_functions(
                functions[1:], params, (*results, functions[0](*params))
            )
    )


def check_conditions(functions, params):
    return reduce(logical_or, apply_functions(functions, params))


def combine_on_condition(*items):
    return tuple(map(lambda i: i[0], filter(lambda i: i[1], items)))


def is_empty(container):
    return len(container) == 0


def map_filter(filter_func, map_func, container):
    return tuple(map(map_func, filter(filter_func, container)))


def logical_or(x, y):
    return x or y


flatten = partial(reduce, lambda x, y: (*x, *y))
