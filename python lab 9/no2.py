from tkinter import *
from tkinter import messagebox

class Convertor: 
    def __init__ (self):
        window = Tk()
        window.title("Currency Converter")

        frame = Frame(window)
        frame.pack()

        Label(frame, text= "Enter: ")
        self.input = DoubleVar()
        self.entry = Entry(frame, textvariable = self.input)
        self.entry.pack()
        uttBtn = Button(frame, text="USD to THB", command=self.utot)
        uttBtn.pack()
        ttuBtn = Button(frame, text="THB to USD", command=self.ttou)
        ttuBtn.pack()
        mainloop()

    def utot(self):
        result = float(self.entry.get()) * 30
        messagebox.showinfo("THB -> USD", f"{result} THB")
    def ttou(self):
        result = float(self.entry.get()) / 30
        messagebox.showinfo("USD --> THB", f"{result:.2f} USD")



Convertor()