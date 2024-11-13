import turtle

screen = turtle.Screen()
screen.bgcolor("black")

spiral_turtle = turtle.Turtle()
spiral_turtle.speed(0)  
spiral_turtle.color("cyan")

angle = 10  
distance = 1  


while True:
    spiral_turtle.forward(distance)
    spiral_turtle.right(angle)
    distance += 0.5 

turtle.done()
