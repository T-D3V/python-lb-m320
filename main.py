from drawing import drawing
from circle import circle
from rectangle import rectangle
from point import point

def main():
  image = drawing()
  image.AddForm(circle(point(16, 22), "blue", 2))
  image.AddForm(circle(point(5, 19), "blue", 1))
  image.AddForm(rectangle(point(4, 20), "blue", 8, 2))
  image.AddForm(rectangle(point(12, 20), "blue", 8, 12))
  image.AddForm(rectangle(point(20, 20), "blue", 8, 2))
  image.AddForm(circle(point(29, 19), "blue", 1))
  image.AddForm(rectangle(point(12, 8), "blue", 2, 8))
  image.AddForm(rectangle(point(18, 8), "blue", 2, 8))
  print(f"The whole area rounded to 2 decimals is {image.ComputeArea():.2f}.")

if __name__  == "__main__":
  main()