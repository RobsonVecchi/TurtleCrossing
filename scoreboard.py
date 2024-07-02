from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-290,270)
        self.write(f"Level: {self.level}", align="left", font=FONT)
        
    def increment_level(self):
        self.level += 1    
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)
        
    def game_over(self):
        self.goto(0,0)
        self.clear()
        self.write("GAME OVER", align="left", font=FONT)    