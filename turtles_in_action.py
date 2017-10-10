# Turtles Square

import turtle

def draw():
	
	window = turtle.Screen()
	window.bgcolor("red")
	
	
	fred = turtle.Turtle()
	fred.shape("turtle")
	fred.color("white")
	fred.speed(2)
	
	for i in range(1, 36):
		square(fred)
		fred.right(10)
	
	fred.right(100)
	fred.forward(300)
	
	window.exitonclick()
	

def square(actor):
	
	for i in range(1, 5):
		actor.forward(100)
		actor.right(90)


draw()
