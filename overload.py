from namespace import Namespace

def overload(fn):
    """overload is the decorator that wraps the function
    and returns a callable object of type Function.
    """
    return Namespace.get_instance().register(fn)
