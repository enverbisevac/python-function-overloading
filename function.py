from inspect import getfullargspec


class Function(object):
    """Function is a wrap over standard python function.
    """

    def __init__(self, fn, namespace):
        self.fn = fn
        self.namespace = namespace

    def __call__(self, *args, **kwargs):
        """Overriding the __call__ function which makes the
        instance callable.
        """
        # fetching the function to be invoked from the virtual namespace
        # through the arguments.
        fn = self.namespace.get_instance().get(self.fn, *args)
        if not fn:
            raise Exception("no matching function found.")

        # invoking the wrapped function and returning the value.
        return fn(*args, **kwargs)

    def key(self, args=None):
        """Returns the key that will uniquely identify
        a function (even when it is overloaded).
        """
        # if args not specified, extract the argumentsfrom the
        # function definition
        if args is None:
            args = getfullargspec(self.fn).args

        return tuple([
            self.fn.__module__,
            self.fn.__class__,
            self.fn.__name__,
            len(args or []),
        ])