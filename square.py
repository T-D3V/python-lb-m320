from form import form
from point import point

class square(form):
  __side:float
  area:float
  circumfrence:float
  
  def __init__(self, location: point, colour: str, side: float) -> None:
    super().__init__(location, colour)
    self.__side = side
    self.area = self.__side**2
    self.circumfrence = self.__side * 4
    