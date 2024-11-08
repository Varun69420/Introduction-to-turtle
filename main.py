import turtle #importing library

turtle.Screen().bgcolor("Aqua")

turtle.Screen().setup(300,400)

polygon = turtle.Turtle() #defined variable


num_sides = 10 #variable

side_length = 25

angle = 360.0 / num_sides

#iterate loop for total number of side

for i in range(num_sides):

 polygon.forward(side_length)

 polygon.right(angle)


turtle.done()