####################################### PYTHON LOVE CODE ########################################
'''Author By    : reguel_walker
   Text Editor  : Visual Studio Code
'''

import time
import turtle as tr


t = tr.Turtle()


def curve():
    t.pen(pencolor="white", pensize=3, speed=5)
    for i in range(200):
        t.right(1)
        t.forward(1)


def love_sign():
    t.pen(pencolor="white", fillcolor="hot pink", pensize=3, speed=5)
    t.shape("turtle")
    t.shapesize(1, 1, 1)
    t.begin_fill()
    t.left(50)
    t.forward(113)
    curve()
    t.left(120)
    curve()
    t.forward(112)
    t.end_fill()

    t.hideturtle()


s = tr.Screen()
s.bgcolor('black')
s.screensize(800, 700)
s.setup(width=1.0, height=1.0, startx=None, starty=None)


# Go to Play Music
# mixer.music.play()

t.penup()
t.goto(-80, 300)
time.sleep(1)
t.pendown()
t.shapesize(1, 2, 1)


# ----------------------------------------"I"----------------------------------------
t.pen(pencolor="white", fillcolor="dark violet", pensize=3, speed=8)
t.begin_fill()
t.forward(160)
t.right(90)
t.forward(25)
t.right(90)
t.forward(60)
t.left(90)

# ----------------------------------Height of the I----------------------------------
t.forward(140)
t.left(90)
t.forward(60)
t.right(90)
t.forward(25)
t.right(90)
t.forward(160)
t.right(90)
t.forward(25)
t.right(90)
t.forward(60)
t.left(90)
t.forward(140)
t.left(90)
t.forward(60)
t.right(90)
t.forward(25)

t.end_fill()
# -----------------------------------------------------------------------------------

t.penup()
t.goto(-550,-20)
t.pendown()


# ----------------------------------Love Sign----------------------------------------
# --------------------------------------L--------------------------------------------

t.pen(pencolor="white", fillcolor="dark violet", pensize=3, speed=2)
t.begin_fill()

t.right(90)
t.forward(25)
t.right(90)
t.forward(165)
t.left(90)
t.forward(115)
t.right(90)
t.forward(25)
t.right(90)
t.forward(140)
t.right(90)
t.forward(190)
t.right(90)

t.end_fill()
# -------------------------------------------------------------------------------------

t.penup()
t.forward(140)

# Gap Between "L" and "O"
t.forward(70)

# ---------------------------------------O---------------------------------------------
t.pen(pencolor="white", fillcolor="cyan", pensize=3, speed=8)
t.begin_fill()

t.right(90)
t.forward(190)
t.left(90)
t.pendown()
t.circle(60)
t.left(90)
t.penup()
t.forward(20)
t.right(90)
t.pendown()
t.circle(40)
t.right(90)
t.penup()
t.forward(20)
t.left(90)

t.end_fill()
# --------------------------------------------------------------------------------------

# Gap Between O and V
t.forward(100)
t.pendown()

# ----------------------------------------"V"-------------------------------------------
t.pen(pencolor="white", fillcolor="dark violet", pensize=3, speed=8)
t.begin_fill()

t.left(100)
t.forward(120)
t.right(100)
t.forward(20)
t.right(80)
t.forward(100)
t.left(80)
t.forward(20)
t.left(80)
t.forward(100)
t.right(80)
t.forward(20)
t.right(100)
t.forward(120)
t.right(80)
t.forward(50)
t.left(180)

t.end_fill()
# --------------------------------------------------------------------------------------

t.penup()
t.forward(100)
t.pendown()

# -----------------------------------------"E"------------------------------------------

t.pen(pencolor="white", fillcolor="dark violet", pensize=3, speed=8)
t.begin_fill()

t.left(90)
t.forward(120)
t.right(90)
t.forward(80)
t.right(90)
t.forward(20)
t.right(90)
t.forward(60)
t.left(90)
t.forward(30)
t.left(90)
t.forward(60)
t.right(90)
t.forward(20)
t.right(90)
t.forward(60)
t.left(90)
t.forward(30)
t.left(90)
t.forward(60)
t.right(90)
t.forward(20)
t.right(90)
t.forward(80)

t.end_fill()
# --------------------------------------------------------------------------------------

t.penup()
t.right(180)

# Gap Between V and E
t.forward(200)
t.pendown()

# ---------------------------------Y for Letter-----------------------------------------

t.pen(pencolor="white", fillcolor="dark violet", pensize=3, speed=2)
t.begin_fill()

t.left(90)
t.forward(50)
t.left(30)
t.forward(80)
t.right(120)
t.forward(20)
t.right(60)
t.forward(60)
t.left(180)
t.right(60)
t.forward(60)
t.right(60)
t.forward(20)
t.right(120)
t.forward(80)
t.left(30)
t.forward(50)
t.right(90)
t.forward(20)
t.right(180)

t.end_fill()
# --------------------------------------------------------------------------------------

t.penup()
t.forward(120)
t.pendown()

# ---------------------------------O for Letter-----------------------------------------

t.pen(pencolor="white", fillcolor="cyan", pensize=3, speed=8)
t.begin_fill()

t.circle(60)
t.left(90)
t.penup()
t.forward(20)
t.pendown()
t.right(90)
t.circle(40)
t.right(90)
t.penup()
t.forward(20)
t.left(90)

t.end_fill()
# --------------------------------------------------------------------------------------

# Gap Between "O" and "U"
t.forward(100)
t.circle(60, extent=60)
t.pendown()

# ---------------------------------U for Letter-----------------------------------------

t.pen(pencolor="white", fillcolor="dark violet", pensize=3, speed=8)
t.begin_fill()

t.left(30)

# Height of "U"
t.forward(85)
t.left(90)
t.forward(20)
t.left(90)
t.forward(70)
t.circle(-20, extent=180)
t.forward(70)
t.left(90)
t.forward(20)
t.left(90)
t.forward(85)
t.circle(40, extent=180)

t.end_fill()
# --------------------------------------------------------------------------------------

t.penup()
# t.goto(300,130)
t.right(180)
t.forward(35)
t.left(90)
t.forward(140)
t.left(90)
t.pendown()

love_sign()