import turtle as t

tim = t.Turtle()

# num_sides = 10


def drew_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 11):
    drew_shape(shape_side_n)

