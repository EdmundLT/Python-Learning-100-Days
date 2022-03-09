from os import makedirs
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

maker = CoffeeMaker()
coins_machine = MoneyMachine()
menu = Menu()
machine_on = True
while machine_on:
    ans = input(f"What would you like? {menu.get_items()}: ")
    if ans == "off":
        machine_on = False
    if ans == "report":
        maker.report()
        coins_machine.report()
    else:
        order = menu.find_drink(ans)
        if coins_machine.make_payment(order.cost) and maker.is_resource_sufficient(order):
            maker.make_coffee(order)
