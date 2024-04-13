class ShapeCalculator:
  def get_area(self):
      pass

  def get_perimeter(self):
      pass

  def get_diagonal(self):
      pass

  def get_picture(self):
      pass

  def set_width(self, width):
      self.width = width

  def set_height(self, height):
      self.height = height

  def set_side(self, side):
      self.side = side


class Rectangle(ShapeCalculator):
  def __init__(self, width, height):
      self.set_width(width)
      self.set_height(height)

  def get_area(self):
      return self.width * self.height

  def get_perimeter(self):
      return 2 * (self.width + self.height)

  def get_diagonal(self):
      return (self.width ** 2 + self.height ** 2) ** 0.5

  def get_picture(self):
    if self.width <= 0 or self.height <= 0:
        return "Shape not supported"
    elif self.width > 50 or self.height > 50:
        return "Too big for picture."
    else:
        return ('*' * self.width + '\n') * self.height

  def get_amount_inside(self, shape):
    return (self.width // shape.width) * (self.height // shape.height)
  def __str__(self):
    return f"{self.__class__.__name__}(width={self.width}, height={self.height})"



    
class Square(Rectangle):
  def __init__(self, side):
      super().__init__(side, side)

  def set_side(self, side):
      super().set_side(side)
      self.width = side
      self.height = side

  def get_picture(self):
    if self.width <= 0 or self.height <= 0:
        return "Shape not supported"
    elif self.width > 50 or self.height > 50:
        return "Too big for picture."
    else:
        return ('*' * self.width + '\n') * self.height
  def __str__(self):
    return f"{self.__class__.__name__}(side={self.width})"


