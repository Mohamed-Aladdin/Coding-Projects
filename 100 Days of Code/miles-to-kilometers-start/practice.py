## NB. *args type is mainly a tuple thus they're positional arguments.

def add(*args):
  print(args)
  print(type(args))

  sum = 0
  for n in args:
    sum += n
  return sum

print(add(1,2,3,4,5))

## NB. **kwargs type is mainly a dictionary thus they're keyword arguments.

def calculate(n, **kwargs):
  print(kwargs)
  print(type(kwargs))
  n += kwargs["add"]
  print(n)
  n *= kwargs["multiply"]
  print(n)

calculate(5, add=10, multiply=3)

class Car:
  def __init__(self, **kw):
    self.make = kw.get("make")
    self.model = kw.get("model")
    self.color = kw.get("color")
    self.seats = kw.get("seats")

my_car = Car(make="Nissan", Model="GT-R", color="Yellow")
print(my_car.make)