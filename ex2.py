import turtle as t


t.bgcolor("black")

circle_turtle = t.Turtle()
circle_turtle.speed(1)  
circle_turtle.color("cyan")

radius = 10


while True:
    circle_turtle.penup()  
    circle_turtle.sety(-radius)  
    circle_turtle.pendown()  
    circle_turtle.circle(radius) 
    radius += 10 

t.done()
