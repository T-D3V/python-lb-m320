from form import form
from point import point

class rectangle(form):
  __side1:float
  __side2:float
  area:float
  circumfrence:float
  
  def __init__(self, location: point, colour: str, side1: float, side2: float) -> None:
    super().__init__(location, colour)
    self.__side1 = side1
    self.__side2 = side2
    self.area = self.__side1 * self.__side2
    self.circumfrence = 2*(self.__side1 + self.__side2)