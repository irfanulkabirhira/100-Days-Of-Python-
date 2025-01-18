from prettytable import PrettyTable
table = PrettyTable()
table.add_column("pokemon Name", ["Pikacu" , "Squirte" , "Charmader"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# For left alignment
table.align = "l"
print(table)
