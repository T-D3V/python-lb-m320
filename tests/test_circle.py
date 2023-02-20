from circle import circle
from point import point

def test_circle1():
  circ = circle(point(1,1), "blue", 9)
  assert circ.area == 254.46900494077323
  
def test_circle2():
  circ = circle(point(1,1), "blue", 0)
  assert circ.area == 0