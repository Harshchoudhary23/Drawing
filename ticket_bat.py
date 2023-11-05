import turtle

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("lightgreen")

# Create a turtle for drawing
pen = turtle.Turtle()
pen.speed(2)  # Set the drawing speed

# Draw the stadium
pen.penup()
pen.goto(0, -150)
pen.pendown()
pen.begin_fill()
pen.color("green")
pen.circle(150)
pen.end_fill()

# Draw the cricket bat
pen.penup()
pen.goto(-20, -150)
pen.pendown()
pen.color("brown")
pen.begin_fill()
pen.goto(-20, -20)
pen.goto(20, -20)
pen.goto(20, -150)
pen.goto(-20, -150)
pen.end_fill()

# Draw the cricket ball
pen.penup()
pen.goto(50, -150)
pen.pendown()
pen.color("red")
pen.begin_fill()
pen.circle(15)
pen.end_fill()

# Hide the turtle and display the result
pen.hideturtle()
wn.exitonclick()
