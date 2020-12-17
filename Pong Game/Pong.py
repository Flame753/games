# Simple Pong in Python 3

import turtle
import os
# import winsound


def sound():
    # For Mac
    os.system("afplay Bounce.wav&")
    # For Linux
    # os.system("afplay Bounce.wav&")
    # For Windows
    # winsound.PlaySound("Bounce.wav", winsound.SND_ASYNC)


class GameObject:

    def __init__(self, shape=None, color="white", location=(0, 0)):
        self.Obj = turtle.Turtle()
        self.Obj.speed(0)
        self.Obj.shape(shape)
        self.Obj.color(color)
        self.Obj.penup()
        self.Obj.goto(location[0], location[1])

    def get_cor(self):
        return self.Obj.xcor(), self.Obj.ycor()


class Paddle(GameObject):
    def __init__(self, shape="square", color="white", location=(0, 0)):
        super().__init__()
        self.Obj.shape(shape)
        self.Obj.color(color)
        self.Obj.shapesize(stretch_wid=5, stretch_len=1)
        self.Obj.goto(location[0], location[1])
        # Score
        self.score = 0

    def paddle_up(self):
        y = self.Obj.ycor()
        y += 20
        self.Obj.sety(y)

    def paddle_down(self):
        y = self.Obj.ycor()
        y -= 20
        self.Obj.sety(y)

    def set_score(self, score):
        self.score += score


class Ball(GameObject):
    def __init__(self, shape="circle", color="white", location=(0, 0)):
        super().__init__()
        self.Obj.shape(shape)
        self.Obj.color(color)
        self.Obj.shapesize(stretch_wid=1, stretch_len=1)
        self.Obj.goto(location[0], location[1])

        # Ball's Movement
        self.dx = .3
        self.dy = -.3

    def move(self):  # Moving Ball
        self.Obj.setx(self.Obj.xcor() + self.dx)
        self.Obj.sety(self.Obj.ycor() + self.dy)

    def border_check(self, paddle_a, paddle_b):
        if self.Obj.ycor() > 290:
            self.Obj.sety(290)
            self.dy *= -1
            sound()

        elif self.Obj.ycor() < -290:
            self.Obj.sety(-290)
            self.dy *= -1
            sound()

        elif self.Obj.xcor() > 390:
            self.Obj.goto(0, 0)
            self.dx *= -1
            return 1  # "A scored a point"

        elif self.Obj.xcor() < -390:
            self.Obj.goto(0, 0)
            self.dx *= -1
            return 2  # "B scored a point"

        # Paddle and ball collisions
        elif (340 < self.Obj.xcor() < 350) and (paddle_b[1] - 50 < self.Obj.ycor() < paddle_b[1] + 50):
            self.Obj.setx(340)
            self.dx *= -1
            sound()

        elif (-340 > self.Obj.xcor() > -350) and (paddle_a[1] - 50 < self.Obj.ycor() < paddle_a[1] + 50):
            self.Obj.setx(-340)
            self.dx *= -1
            sound()

        return 0  # "No one scored a point"


class Pen(GameObject):
    def __init__(self, shape=None, color="white", location=(0, 0)):
        super().__init__()
        self.Obj.hideturtle()
        self.Obj.shape(shape)
        self.Obj.color(color)
        self.Obj.goto(location[0], location[1])
        self.Obj.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))

    def update_score(self, score_a, score_b):
        self.Obj.clear()
        self.Obj.write("Player A: {} Player B: {}".format(score_a, score_b),
                       align="center", font=("Courier", 24, "normal"))


class Game:
    def __init__(self):
        # Screen of Board
        self.wn = turtle.Screen()
        self.wn.title("Pong")
        self.wn.bgcolor("black")
        self.wn.setup(width=800, height=600)
        self.wn.tracer(0)

        # Paddle A
        self.paddle_a = Paddle(location=(-350, 0))

        # Paddle B
        self.paddle_b = Paddle(location=(350, 0))

        # Ball
        self.ball = Ball()

        # Pen
        self.pen = Pen(location=(0, 260))

    def main(self):
        # Keyboard binding
        self.wn.listen()
        self.wn.onkeypress(self.paddle_a.paddle_up, "w")
        self.wn.onkeypress(self.paddle_a.paddle_down, "s")

        self.wn.onkeypress(self.paddle_b.paddle_up, "Up")
        self.wn.onkeypress(self.paddle_b.paddle_down, "Down")

        # Main game loop
        while True:
            self.wn.update()
            # Move the ball
            self.ball.move()
            # Border checking
            point_goes_to = self.ball.border_check(self.paddle_a.get_cor(), self.paddle_b.get_cor())

            # 0: "No one scored a point"
            # 1: "A scored a point"
            # 2: "B scored a point"
            if point_goes_to == 0:
                continue
            elif point_goes_to == 1:
                self.paddle_a.set_score(1)
                self.pen.update_score(self.paddle_a.score, self.paddle_b.score)
            elif point_goes_to == 2:
                self.paddle_b.set_score(1)
                self.pen.update_score(self.paddle_a.score, self.paddle_b.score)


if __name__ == "__main__":
    Game().main()







