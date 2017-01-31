import turtle

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    angie = turtle.Turtle()
    angie.color("yellow")
    angie.speed(100)
    for k in range (0,3):
        for j in range(0,360,10):
            angie.right(10)
            angie.circle(50*(k+1))

    window.exitonclick()

draw_art()
