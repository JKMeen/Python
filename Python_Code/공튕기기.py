from tkinter import*
import random
import time

tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=300, height=300, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

class Player:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_polygon(10, 10, 10, 30, 25, 18.5, fill=color)
        self.canvas.move(self.id, 10, 10)
        self.x = 0
        self.y = -1
        self.canvas_height = self.canvas.winfo_height()
 
    def PlayMove(event):
        if event.keysym == 'Up':
            canvas.move(1, 0, -5)
                
        elif event.keysym == 'Down':
            canvas.move(1, 0, 5)
                
        elif event.keysym == 'Left':
            canvas.move(1, -5, 0)
            
        else:
            canvas.move(1, 5, 0)
            
    canvas.bind_all('<KeyPress-Up>', PlayMove)
    canvas.bind_all('<KeyPress-Down>', PlayMove)
    canvas.bind_all('<KeyPress-Left>', PlayMove)
    canvas.bind_all('<KeyPress-Right>', PlayMove)

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 299, random.randint(10,290))
        self.x = -5
        self.y = 0
        self.canvas_width = self.canvas.winfo_width()
        
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.x = 5
        if pos[3] >= self.canvas_width:
            self.x = -5

    def movetriangle(event):
        canvas.move(1, 5, 0)

player = Player(canvas, 'yellow')
ball = Ball(canvas, 'red')


while 1:
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
    
