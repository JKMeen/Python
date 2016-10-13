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
    def __init__(self, canvas):
        self.canvas = canvas
        self.id = canvas.create_polygon(10, 10, 10, 30, 25, 18.5, fill='blue')
        self.canvas.move(self.id, 10, 10)
        self.x = 0
        self.y = 0
        self.canvas_height = self.canvas.winfo_height()

    def PlayMove(event):
        if event.keysym == 'Return':
            canvas.move(1, 10, 10)
            
        elif event.keysym == 'Up':
            canvas.move(1, 0, -7)
                
        elif event.keysym == 'Down':
            canvas.move(1, 0, 7)
                
        elif event.keysym == 'Left':
            canvas.move(1, -7, 0)
            
        else:
            canvas.move(1, 7, 0)

    canvas.bind_all('<KeyPress-Return>', PlayMove)            
    canvas.bind_all('<KeyPress-Up>', PlayMove)
    canvas.bind_all('<KeyPress-Down>', PlayMove)
    canvas.bind_all('<KeyPress-Left>', PlayMove)
    canvas.bind_all('<KeyPress-Right>', PlayMove)

class Ballwidth:
    def __init__(self, canvas):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill='red')
        self.canvas.move(self.id, 299, random.randint(30,250))
        self.x = -3
        self.y = 0
        self.canvas_width = self.canvas.winfo_width()
        
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[2] <= 1:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

    def movetriangle(event):
        canvas.move(1, 5, 0)

class Ballheight:
    def __init__(self, canvas):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill='red')
        self.canvas.move(self.id, random.randint(30,250), 299)
        self.x = 0
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.y = -3

    def movetriangle(event):
        canvas.move(1, 0, 5)

player = Player(canvas)
ballw1 = Ballwidth(canvas)
ballw2 = Ballwidth(canvas)
ballw3 = Ballwidth(canvas)
ballw4 = Ballwidth(canvas)
ballw5 = Ballwidth(canvas)
ballw6 = Ballwidth(canvas)
ballw7 = Ballwidth(canvas)

ballh1 = Ballheight(canvas)
ballh2 = Ballheight(canvas)
ballh3 = Ballheight(canvas)
ballh4 = Ballheight(canvas)
ballh5 = Ballheight(canvas)
ballh6 = Ballheight(canvas)
ballh7 = Ballheight(canvas)

while 1:
    ballw1.draw()
    ballw2.draw()
    ballw3.draw()
    ballw4.draw()
    ballw5.draw()
    ballw6.draw()
    ballw7.draw()
    ballh1.draw()
    ballh2.draw()
    ballh3.draw()
    ballh4.draw()
    ballh5.draw()
    ballh6.draw()
    ballh7.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
    
