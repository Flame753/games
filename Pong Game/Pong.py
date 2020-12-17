# Simple Pong in Python 3

import turtle


class Obj:

    def __init__(self, shape=None, color="white", location=(0, 0), stretch=(1, 1), hide=False, write=None):
        self.Obj = turtle.Turtle()
        self.Obj.speed(0)
        self.Obj.shape(shape)
        self.Obj.color(color)
        self.Obj.shapesize(stretch_wid=stretch[0], stretch_len=stretch[1])
        self.Obj.penup()
        self.Obj.goto(location[0], location[1])

        if hide:
            self.Obj.hideturtle()
        if write:
            self.Obj.write(write, align="center", font=("Courier", 24, "normal"))

        # Ball's Movement
        self.dx = .3
        self.dy = -.3

    def get_cor(self):
        return self.Obj.xcor(), self.Obj.ycor()

    def paddle_up(self):
        y = self.Obj.ycor()
        y += 20
        self.Obj.sety(y)

    def paddle_down(self):
        y = self.Obj.ycor()
        y -= 20
        self.Obj.sety(y)

    def move(self):  # Moving Ball
        ball = self.Obj
        ball.setx(ball.xcor() + self.dx)
        ball.sety(ball.ycor() + self.dy)

    def border_check(self, paddle_a, paddle_b):
        ball = self.Obj

        if ball.ycor() > 290:
            ball.sety(290)
            self.dy *= -1

        if ball.ycor() < -290:
            ball.sety(-290)
            self.dy *= -1

        if ball.xcor() > 390:
            ball.goto(0, 0)
            self.dx *= -1

        if ball.xcor() < -390:
            ball.goto(0, 0)
            self.dx *= -1

        # Paddle and ball collisions
        if (340 < ball.xcor() < 350) and (paddle_b[1] - 50 < ball.ycor() < paddle_b[1] + 50):
            ball.setx(340)
            self.dx *= -1
        if (-340 > ball.xcor() > -350) and (paddle_a[1] - 50 < ball.ycor() < paddle_a[1] + 50):
            ball.setx(-340)
            self.dx *= -1


class Game:
    def __init__(self):
        # Screen of Board
        self.wn = turtle.Screen()
        self.wn.title("Pong")
        self.wn.bgcolor("black")
        self.wn.setup(width=800, height=600)
        self.wn.tracer(0)

        # Paddle A
        self.paddle_a = Obj("square", "white", (-350, 0), (5, 1))

        # Paddle B
        self.paddle_b = Obj("square", "white", (350, 0), (5, 1))

        # Ball
        self.ball = Obj("square", "white", (0, 0))

        # Pen
        self.pen = Obj(color="white", location=(0, 260), hide=True, write="Player A: 0 Player B: 0")

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
            self.ball.border_check(self.paddle_a.get_cor(), self.paddle_b.get_cor())



# Score
score_a = 0
score_b = 0

if __name__ == "__main__":
    Game().main()







