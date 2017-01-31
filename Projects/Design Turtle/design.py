import turtle

def draw_square(some_turtle):
    for k in range (0,3):
         for j in range(0,360,5):
            some_turtle.right(5)
            for i in range(1,5):
                some_turtle.forward(100+(k*100))
                some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    #Create the turtle Brad - Draw a square
    brad = turtle.Turtle()
    brad.color("yellow")
    brad.speed(1000)
    draw_square(brad)

    window.exitonclick()

draw_art()
