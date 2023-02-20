from square import square
from point import point

def test_square1():
  squ = square(point(1,1), "blue", 0.25)
  assert squ.area == 0.0625
  
def test_rectangle():
  squ = square(point(1,1), "blue", 0)
  assert squ.area == 0