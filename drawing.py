from form import form

class drawing:
  __forms:list[form] = []
  
  def ComputeArea(self) -> float:
    res:float = 0
    for form in self.__forms:
      res += form.area
    return res
  
  def AddForm(self, f:form) -> None:
    self.__forms.append(f)