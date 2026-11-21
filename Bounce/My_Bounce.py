from tkinter import *
from tkinter import colorchooser
import random
import time
import sys

class Ball:
    def __init__ (self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.score = 0
        self.id = canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3,-2,-1,1,2,3]
        self.x = random.choice(starts)
        self.y = -speed
        self.canvas_height = 400
        self.canvas_width = 500
        self.hit_bottom = False
        self.DisplayScore = canvas.create_text(470,20,text= f'Score: {self.score}', fill='Black',font=('Helvectia', 10))
        

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0 or pos[2] >= self.canvas_width:
            self.x = self.x * -1
        if self.hit_paddle(pos) == True:
            self.y = self.y * -1
            self.score = self.score + 1
            canvas.itemconfig(self.DisplayScore, text=f'Score:{self.score}')
        if pos[1] <= 0 or pos[3] >= self.canvas_height:
            self.y = self.y * -1    
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True

    
    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
            return False

class Paddle:
    def __init__( self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 85, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = 500
        self.canvas.bind_all('<KeyPress-Left>', self.move_left)
        self.canvas.bind_all('<KeyPress-Right>', self.move_right)
        self.canvas.bind_all('<Button-1>', self.StartGame)
        self.StartGame = False
    
    def StartGame(self, event):
        time.sleep(1)
        self.StartGame = True

    def draw (self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0 or pos[2] >= self.canvas_width:
            self.x = self.x * -1

    def move_left(self, event):
        self.x = -2

    def move_right(self, event):
        self.x = 2



print('Which speed from 1 to 10?')
speed = int(sys.stdin.readline())

tk = Tk() 
tk.title('Bounce Game')
tk.resizable(0,0)
tk.wm_attributes('-topmost', 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update

paddle = Paddle(canvas,'Blue')

ball = Ball(canvas, paddle, 'Red')

textid = canvas.create_text(245,100,text='GAME OVER', fill='Red',font=('Helvectia', 30))
canvas.itemconfig(textid, state='hidden')
while True:

    if ball.hit_bottom == True:
        canvas.itemconfig(textid, state='normal')
        canvas.create_text(255,190,text= f'Your Score: {ball.score}', fill='Black',font=('Helvectia', 10))
    
    if ball.hit_bottom == False and paddle.StartGame == True:
        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)