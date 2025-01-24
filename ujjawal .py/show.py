import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create the turtle object
flower = turtle.Turtle()
flower.shape("turtle")
flower.color("purple")
flower.speed(10)

# Function to draw a petal
def draw_petal():
    flower.circle(100, 60)  # Draw a part of the circle (a petal shape)
    flower.left(120)
    flower.circle(100, 60)  # Draw the other part of the circle
    flower.left(120)

# Draw the flower with multiple petals
for _ in range(6):
    draw_petal()
    flower.left(60)  # Rotate the flower to create the next petal

# Hide the turtle after drawing
flower.hideturtle()

# Keep the window open
turtle.done()
