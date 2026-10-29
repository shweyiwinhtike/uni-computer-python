from tkinter import *

class paint:
    def __init__ (self):
        window = Tk()
        window.title("A simple Paint Program")

        frame = Frame(window)
        frame.pack()
        self.canvas = Canvas(window, width=500, height=400, bg="white")
        self.canvas.pack()
        self.label = Label(frame, text="Drag the mouse to draw").pack()
        self.button = Button(frame, text="clear", command=self.clear).pack()
        
        
        self.canvas.bind("<Button-1>", self.click)
        self.canvas.bind("<B1-Motion>", self.draw)

        window.mainloop()

    def click(self, event):
        self.x = event.x
        self.y = event.y

    def draw(self, event):
        self.canvas.create_line(self.x, self.y, event.x, event.y, width=5)
        self.x = event.x
        self.y = event.y

    def clear(self):
        self.canvas.delete("all")


paint()