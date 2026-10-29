from tkinter import *

class spinner:
    def __init__(self):
        window = Tk()
        window.title("N0. 1")
        self.count = 0

        frame = Frame(window)
        frame.pack()

        label = Label(frame, text=self.count)

        addBtn = Button(frame, text="+", command=self.count_plus)
        minusBtn = Button(frame, text="-", command=self.count_minus)
        resetBtn = Button(frame, text="Reset", command=self.count_reset)

        label.grid(row=1,column=1)
        addBtn.grid(row=1,column=2)
        minusBtn.grid(row=2,column=2)
        resetBtn.grid(row=3,column=2)
        mainloop()


    def count_plus(self):
        self.count += 1
        self.label['text'] = self.count

    def count_minus(self):
        self.count -= 1
        self.label['text'] = self.count

    def count_reset(self):
        self.count = 0
        self.label['text'] = self.count

spinner()