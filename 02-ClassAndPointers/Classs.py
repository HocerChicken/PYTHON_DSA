class Cookie: 
  def __init__(self, color):
    self.color = color
  def set_color(self, color):
    self.color = color
  def get_color(self):
    return self.color
  
cookie1 = Cookie('green')

print(cookie1.get_color())

cookie1.set_color("Blue")

print("the color of cookie after set it is blue", cookie1.get_color())