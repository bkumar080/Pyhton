import turtle

def draw_square(some_turtle):

         for j in range(0,360,5):
            some_turtle.right(5)
            for i in range(1,3):
                some_turtle.forward(50)
                some_turtle.right(45)
                some_turtle.forward(50)
                some_turtle.right(135)
def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    #Create the turtle Brad - Draw a square
    brad = turtle.Turtle()
    brad.color("yellow")
    brad.speed(1000)
    draw_square(brad)

    #Create the turtle Brad - Draw a square
    brad.right(90)
    brad.forward(150)

    window.exitonclick()

draw_art()
