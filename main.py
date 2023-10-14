# from turtle import Turtle, Screen
from prettytable import PrettyTable

# timmy = Turtle()
# print(timmy)
#
# timmy.shape("turtle")
# timmy.color("coral")
# my_screen = Screen()
# print(my_screen.canvheight)
# for _ in range(0, 4):
#     timmy.forward(100)
#     timmy.left(90)
#     timmy.forward(100)
#     timmy.left(90)
#     timmy.forward(100)
#     timmy.left(90)
#     timmy.forward(100)
#     # timmy.onclick()
# my_screen.exitonclick()

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)