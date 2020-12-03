#CC Ben kilgore
import turtle

def draw_circle(turtle, color, size, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()
    turtle.pendown()

tommy = turtle.Turtle()
tommy.shape("turtle")
tommy.speed(500)

draw_circle(tommy, "green", 50, 25, 0) 
draw_circle(tommy, "blue", 50, 0, 0)
draw_circle(tommy, "yellow", 50, -25, 0)
draw_circle(tommy, "#ff00ff" , 50, -50, 0)
draw_circle(tommy, "#0000ff" , 40, -60, 10)
draw_circle(tommy, "#FF0000" , 50, 25, 0)  
draw_circle(tommy, "#000000" , 50, 30, 10)
draw_circle(tommy, "#5500FF" , 50, 30, 10)
draw_circle(tommy, "#00FFE6"  , 50, 20, 10)
draw_circle(tommy, "#44FF00"  , 50, 30, 10)
draw_circle(tommy, "#FFB300"  , 50, 30, 10)
draw_circle(tommy, "#FF9999"  , 50, 30, 10)
draw_circle(tommy, "#830276"  , 50, 30, 10)
draw_circle(tommy, "#BDA6EB"  , 50, 30, 10)
draw_circle(tommy, "#FF3333"  , 50, 30, 10)