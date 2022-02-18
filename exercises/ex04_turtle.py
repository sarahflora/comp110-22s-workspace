"""This program will use Turtle objects to create two pine trees and two *magical* apple trees, and a funky patch of grass, creating a most delightful arboretum.
for #7, the apple function calls the color_pick function, the pine_tree function calls pine and tree_trunk, the apple_tree function call apple and tree_trunk. For #8, I used some
new functions I didn't know from the tutorial including .dot, .backward, and replacements for some that I learned like .up for .pen up, etc...
I used a nested while loop to create stacked triangles for my pine tree. I also included randomness by using randint in the color_pick function to pick from a list of colors.
"""

__author__ = "730456646"

from turtle import Turtle, colormode, done
from random import randint
colormode(255)


def main() -> None:
    """The entrypoint of my drawing."""
    artist: Turtle = Turtle()
    pine_tree(artist, -200, 0)
    apple_tree(artist, -50, 0)
    pine_tree(artist, 100, 0)
    apple_tree(artist, 250, 0)
    grass(artist, -325, -100, 45)
    done()


def tree_trunk(art: Turtle, x: float, y: float) -> None:
    """Drawing the tree trunk using a brown rectangle."""
    i: int = 0
    art.penup()
    art.goto(x, y)
    art.pendown()
    art.color(135, 62, 35)
    art.begin_fill()
    while i < 2:
        art.right(90)
        art.forward(100)
        art.right(90)
        art.forward(50)
        i += 1
    art.end_fill()


def pine(art: Turtle, x: float, y: float) -> None:
    """Drawing three stacked triangle, of three different greens creating some pine tree greenery."""
    counter: int = 0
    art.penup()
    art.goto(x, y)
    art.pendown()
    art.color(52, 135, 27)
    while (counter < 3):
        i: int = 0
        art.begin_fill()
        while (i < 3):
            art.forward(100)
            art.left(120)
            i += 1
        art.end_fill()
        counter += 1
        if counter == 1:
            art.color(75, 152, 51)
        if counter == 2:
            art.color(119, 191, 96)
        art.up()
        art.setpos(x, y + (30 * counter))
        art.down()   


def color_pick() -> str:
    """Randomly choose color from list, will be used for magical apple colors."""
    list_color: list = ["red", "pink", "orange", "yellow", "brown", "black", "white", "blue", "purple"]
    pick: int = randint(1, 8)
    return str(list_color[pick])


def apple(art: Turtle, x: float, y: float) -> None:
    """This function will create a round, green, filled-in circle representing the greenery and three randomly colored circles for each *magical* apple."""
    art.penup()
    art.goto(x, y)
    art.pendown()
    art.dot(130, "green")
    art.left(50)
    art.penup()
    art.backward(30)
    art.pendown()
    art.right(50)
    i: int = 0
    while i < 3:
        art.dot(30, color_pick())
        art.penup()
        art.forward(50)
        art.pendown()
        art.left(120)
        i += 1


def pine_tree(art: Turtle, x: float, y: float) -> None:
    """This function will take tree_trunk and pine to create a whole pine tree."""
    tree_trunk(art, x, y)
    pine(art, x - 75, y)


def apple_tree(art: Turtle, x: float, y: float) -> None:
    """This function will take tree_trunk and apple to create a whole magical apple tree."""
    tree_trunk(art, x, y)
    apple(art, x - 25, y + 50)


def grass(art: Turtle, x: float, y: float, count: int) -> None:
    """Will draw a funky zig zag patch of green grass count zig zags long."""
    art.speed(50)
    art.penup()
    art.goto(x, y)
    art.pendown()
    art.pensize(10)
    art.color(52, 135, 27)
    art.left(45)
    i: int = 0
    while i < count:
        art.forward(10)
        art.right(90)
        art.forward(10)
        art.left(90)
        i += 1


if __name__ == "__main__":
    main()