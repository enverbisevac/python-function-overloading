import time


def processing_time(fn):
  """my_decorator is a custom decorator that wraps any function
  and prints on stdout the time for execution.
  """
  def wrapper_function(*args, **kwargs):
    start_time = time.time()

    # invoking the wrapped function and getting the return value.
    value = fn(*args, **kwargs)
    print("the function execution took:", (time.time() - start_time) * 1000, "miliseconds")

    # returning the value got after invoking the wrapped function
    return value

  return wrapper_function