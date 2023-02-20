from form import form
from point import point
import math

class circle(form):
  __radius:float
  area:float
  circumfrence:float
  
  def __init__(self, location: point, colour: str, radius: float) -> None:
    super().__init__(location, colour)
    self.__radius = radius
    self.area = math.pow(self.__radius, 2) * math.pi
    self.circumfrence = self.__radius*2*math.pi
    