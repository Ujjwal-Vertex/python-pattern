import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
flower = turtle.Turtle()
flower.shape("turtle")
flower.color("red")
flower.speed(5)

# Function to draw a petal
def draw_petal():
    flower.circle(50, 60)  # Draw a part of a circle
    flower.left(120)
    flower.circle(50, 60)  # Draw the other part of the circle
    flower.left(120)

# Draw the flower
for _ in range(6):
    draw_petal()  # Draw a petal
    flower.left(60)  # Rotate to draw the next petal

# Hide the turtle after drawing
flower.hideturtle()

# Keep the window open
turtle.done()
