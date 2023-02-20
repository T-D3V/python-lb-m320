from rectangle import rectangle
from point import point

def test_rectangle1():
  rect = rectangle(point(1,1), "blue", 3.4, 4)
  assert rect.area == 13.6
  
def test_rectangle():
  rect = rectangle(point(1,1), "blue", 3.4, 0)
  assert rect.area == 0