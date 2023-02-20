from point import point

#This is an abstract class, there are more forms which extend from it, normally in python you'd use a protocol for this, but this works too.
class form:
  #location and colour are given values, in the current state of the program not implemented, but the variables are there.
  _location: point
  _colour: str
  area: float
  circumfrence: float
  
  def __init__(self, location: point, colour: str) -> None:
    self._location = location
    self._colour = colour