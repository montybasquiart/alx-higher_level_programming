#!/usr/bin/python3
def safe_function(fct, *args):
    """A function that executes a function safely.
    """
    import sys
    try:
        result = fct(*args)
        return result
    except Exception as error:
        sys.stderr.write("Exception: {}\n".format(error))
        return None
