from function import Function
from namespace import Namespace
from overload import overload
from helper import processing_time


@processing_time
@overload
def area(l, b):
  return l * b

@processing_time
@overload
def area(r):
  import math
  return math.pi * r ** 2

@processing_time
def area1(l, b):
  return l * b

@processing_time
def area2(r):
  import math
  return math.pi * r ** 2


if __name__ == "__main__":
    print(area(3, 4))
    print(area(7))
    print(area1(3, 4))
    print(area2(7))
