# import another_module

from prettytable import PrettyTable

# print(another_module.another_variable)

# from turtle import Turtle , Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)


table = PrettyTable()
# table.add_column("Name", ["Hira", "Matin"])
# table.add_column("Age", [23, 26])

table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
table.add_rows(
    [
        ["Adelaide", 1295, 1158259, 600.5],
        ["Brisbane", 5905, 1857594, 1146.4],
        ["Darwin", 112, 120900, 1714.7],
        ["Hobart", 1357, 205556, 619.5],
        ["Sydney", 2058, 4336374, 1214.8],
        ["Melbourne", 1566, 3806092, 646.9],
        ["Perth", 5386, 1554769, 869.4],
    ]
)


table.align = 'l'

print(table)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()