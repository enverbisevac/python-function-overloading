"""Virtual namespace
"""

from function import Function

class Namespace(object):
    """Namespace is singleton class that is responsible
    for holding all the functions.
    """
    __instance = None

    def __init__(self):
        if self.__instance is None:
            self.function_map = dict()
            Namespace.__instance = self
        else:
            raise Exception('cannot instantiate a virtual Namespace again')

    @staticmethod
    def get_instance():
        if Namespace.__instance is None:
            Namespace()
        return Namespace.__instance

    def register(self, fn):
        """register the function in the virtual namespace and returns
        an instance of callable Function that wraps the
        function fn
        """
        func = Function(fn, self)
        self.function_map[func.key()] = fn
        return func

    def get(self, fn, *args):
        """get returns the matching function from the virtual namespace.

        return None if it did not fund any matching function.
        """
        func = Function(fn, self)
        return self.function_map.get(func.key(args=args))

    def __call__(self, *args, **kwargs):
        """Overriding the __call__ function which makes the
        instance callable.
        """
        # fetching the function to be invoked from the virtual namespace
        # through the arguments.
        fn = Namespace.get_instance().get(self.fn, *args)
        if not fn:
            raise Exception("no matching function found.")

        # invoking the wrapped function and returning the value.
        return fn(*args, **kwargs)
