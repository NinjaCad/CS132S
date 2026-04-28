"""
    Deliverable: Homework04.py


    References:

        https://runestone.academy/runestone/books/published/pythonds3/Recursion/toctree.htmlLinks to an external site.
        (Sections 4.1-4.8)


    Sample Input/Output:

        RESTART: /Users/jeickemeyer/TMU/Courses/CS132S/_key/Homework04.py 
        Enter recursion levels: 0
        Click turtle screen to exit...
        >>> 
        HW04-L0.png
        RESTART: /Users/jeickemeyer/TMU/Courses/CS132S/_key/Homework04.py 
        Enter recursion levels: 1
        Click turtle screen to exit...
        >>> 
        HW04-L1.png
        RESTART: /Users/jeickemeyer/TMU/Courses/CS132S/_key/Homework04.py 
        Enter recursion levels: 2
        Click turtle screen to exit...
        >>> 
        HW04-L2.png
        RESTART: /Users/jeickemeyer/TMU/Courses/CS132S/_key/Homework04.py 
        Enter recursion levels: 3
        Click turtle screen to exit...
        >>> 
        HW04-L3.png
        RESTART: /Users/jeickemeyer/TMU/Courses/CS132S/_key/Homework04.py 
        Enter recursion levels: 4
        Click turtle screen to exit...
        >>> 
        HW04-L4.png


    100	CS132S Rubric HW04:
        5	Initial I/O
        5	Turtle window
        10	Draw Dots
        15	Base Case
        15	Display "I"
        15	Recursively
        10	Readability of Code
        25	Quality of Solution
"""

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

if __name__ == "__main__":
    main()