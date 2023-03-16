from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main():
  terminate = False
  coffee_maker = CoffeeMaker()
  menu = Menu()
  money_machine = MoneyMachine()
  while not terminate:
    options = menu.get_items()
    request = input(f"What would you like to order? ({options}): ")
    if request == "off":
      print("Shutting down. Bye Bye!")
      break
    elif request == "report":
      coffee_maker.report()
      money_machine.report()
      continue
    order = menu.find_drink(request)
    if not coffee_maker.is_resource_sufficient(order) or not money_machine.make_payment(order.cost):
      break
    coffee_maker.make_coffee(order)

main()