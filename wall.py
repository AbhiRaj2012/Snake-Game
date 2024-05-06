import turtle


class Boundary:
    def __init__(self):
        self.wall_turtle = turtle.Turtle()
        self.wall_turtle.color('green4')
        self.wall_turtle.hideturtle()
        self.wall_turtle.penup()
        self.wall_turtle.goto(-310, -310)
        self.wall_turtle.pendown()
        self.wall_turtle.pensize(10)
        self.draw_wall()


    def draw_wall(self):
        for _ in range(4):
            self.wall_turtle.forward(620)
            self.wall_turtle.left(90)
