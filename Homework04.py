import turtle

t = turtle.Turtle()
s = turtle.Screen()

def draw(x, y, size, depth, dot):
    half = size / 2

    if (depth != 0):
        # Top line
        t.penup()
        t.goto(x - half, y + half)
        t.pendown()
        t.goto(x + half, y + half)
        
        # Center line
        t.penup()
        t.goto(x, y + half)
        t.pendown()
        t.goto(x, y - half)

        # Bottom line
        t.penup()
        t.goto(x - half, y - half)
        t.pendown()
        t.goto(x + half, y - half)
        
        # Draw 4 more
        draw(x - half, y + half, half, depth - 1, dot)
        draw(x + half, y + half, half, depth - 1, dot)
        draw(x - half, y - half, half, depth - 1, dot)
        draw(x + half, y - half, half, depth - 1, dot)

    else:
        t.penup()
        t.goto(x, y)
        t.dot(dot)
        return True

def main():
    t.speed(0)
    t.color("white")
    t.hideturtle()
    s.bgcolor("black")

    level = int(input("Enter recursion levels: "))

    t.penup()
    t.goto(0, 0)
    t.dot()

    draw(0, 0, 200, level + 1, 4)

    print("Click turtle screen to exit...")
    s.exitonclick()

main()