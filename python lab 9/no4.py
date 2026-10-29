from tkinter import *
from tkinter import messagebox
import random

class spinner:
    def __init__ (self):
        window = Tk()
        window.title("A simple Paint Program")

        self.canvas = Canvas(window, width=500, height=400, bg="white")
        self.canvas.pack()

        self.x0 = 50
        self.y0 = 50
        self.x1 = 400
        self.y1 = 250
        self.canvas.create_rectangle(self.x0, self.y0, self.x1, self.y1, width=5)
        self.canvas.bind("<Button-1>", self.click)
        mainloop()

    def click(self, event):        
        if 50 <= event.x <= 400 and 50 <= event.y <= 250:
            colors = random.choice(["red", "yellow", "blue", "green"])
            self.canvas.create_oval(event.x-5, event.y-5, event.x, event.y, fill=colors)
        else:
            messagebox.showwarning("warning", "Mouse Pointer is not in the rectangle")


spinner()

