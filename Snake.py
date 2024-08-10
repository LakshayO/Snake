from turtle import Turtle


class Snake:
    def __init__(self):
        self.position = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []

        for po in self.position:
            new = Turtle("square")
            new.penup()
            new.turtlesize(stretch_len=1, stretch_wid=1)
            new.color('white')
            new.goto(po)
            self.segments.append(new)
        self.head = self.segments[0]

    def add_seg(self):
        imb = Turtle("square")
        imb.penup()
        imb.turtlesize(stretch_len=1, stretch_wid=1)
        imb.color("white")
        x = self.segments[-1].xcor()
        y = self.segments[-1].ycor()
        imb.goto(x, y)
        self.segments.append(imb)

    def snake_reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)

    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
            x = self.segments[i-1].xcor()
            y = self.segments[i-1].ycor()
            self.segments[i].goto(x, y)
        self.head.forward(20)

    def Up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def Down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def Left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def Right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
