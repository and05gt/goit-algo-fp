import turtle
import math

def pythagoras_tree(t, order, branch_len):
    """Recursive function for drawing a Pythagorean tree."""

    if order == 0:
        return
    
    t.forward(branch_len)

    next_len = branch_len * (math.sqrt(2) / 2)  # Length of the next branches

    t.left(45)
    pythagoras_tree(t, order - 1, next_len)
    t.right(90)
    pythagoras_tree(t, order - 1, next_len)
    t.left(45)
    t.backward(branch_len)

def draw_pythagoras_tree(order, length=150):
    """Set up the turtle and draw the Pythagorean tree."""

    window = turtle.Screen()
    window.bgcolor("white")
    window.setup(width=800, height=800)

    t = turtle.Turtle()
    t.color("brown")
    t.speed(0)
    t.hideturtle()
    t.pensize(2)
    t.left(90)
    t.penup()
    t.goto(0, -250)
    t.pendown()

    pythagoras_tree(t, order, length)

    window.mainloop()

if __name__ == "__main__":
    try:
        recursion_level = int(input("Enter the recursion level (5-12): "))
        if recursion_level >= 5 and recursion_level <= 12:
            draw_pythagoras_tree(recursion_level, length=150)
        else:
            print("Please enter a valid recursion level between 5 and 12.")
        
    except ValueError:
        print("Invalid input. Please enter an integer between 5 and 12.")
    except Exception as e:
        print(f"An error occurred: {e}")
