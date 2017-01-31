import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_triangle(some_turtle):
        some_turtle.forward(200)
        some_turtle.left(135)
        some_turtle.forward(100)
        some_turtle.left(90)
        some_turtle.forward(100)
        some_turtle.right(45)
        some_turtle.forward(100)
        
def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    #Create the turtle Brad - Draw a square
    brad = turtle.Turtle()
    brad.color("yellow")
    brad.speed(2)
    draw_square(brad)

    #Create the turtle Angie - Draw a Ciricle
    angie = turtle.Turtle()
    angie.color("blue")
    angie.circle(100)

    #Create the turtle Bob - Draw a Triangle
    bob = turtle.Turtle()
    bob.color("yellow")
    bob.speed(2)
    draw_triangle(bob)
    
    window.exitonclick()

draw_art()
