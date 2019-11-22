from tkinter import Tk, Label, Button

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Basic Calculator")


        self.num1 = Button(self.master, text='1', command = self.getOne)
        self.num1.grid(row=2, column=0)
        self.num2 = Button(self.master, text='2', command = self.getTwo)
        self.num2.grid(row=2, column=1)
        self.num3 = Button(self.master, text='3', command = self.getThree)
        self.num3.grid(row=2, column=2)
        self.num4 = Button(self.master, text='4', command = self.getFour)
        self.num4.grid(row=3, column=0)
        self.num5 = Button(self.master, text='5', command = self.getFive)
        self.num5.grid(row=3, column=1)
        self.num6 = Button(self.master, text='6', command = self.getSix)
        self.num6.grid(row=3, column=2)
        self.num7 = Button(self.master, text='7', command = self.getSeven)
        self.num7.grid(row=4, column=0)
        self.num8 = Button(self.master, text='8', command = self.getEight)
        self.num8.grid(row=4, column=1)
        self.num9 = Button(self.master, text='9', command = self.getNine)
        self.num9.grid(row=4, column=2)
        self.equal = Button(self.master, text='=', command= self.evaluate)
        self.equal.grid(row=5, column=2)
        self.zero = Button(self.master, text = '0', command= self.getZero)
        self.zero.grid(row=5, column=1)

        self.add = Button(self.master, text = '+', command= self.addition)
        self.add.grid(row=2, column=3)
        self.multiply = Button(self.master, text = '*', command= self.multiplication)
        self.multiply.grid(row=3, column=3)
        self.divide = Button(self.master, text = '/', command= self.division)
        self.divide.grid(row=4, column=3)
        self.minus = Button(self.master, text = '-', command= self.substract)
        self.minus.grid(row=5, column=3)

        self.delete = Button(self.master, text='AC', command=self.clear)
        self.delete.grid(row=5, column=0)

        self.s = ''
        self.display = Label(self.master, text = self.s)
        self.display.grid(row=0)

        self.quit = Button(self.master, text='OFF', command=self.close)
        self.quit.grid(row= 8)
    def clear(self):
        self.s= ''
        self.display = Label(self.master, text = self.s)
        self.display.grid(row=0)
    def getOne(self):
        self.s += self.num1.cget('text')
        self.display = Label(self.master, text = self.s)
        self.display.grid(row=0)
    def getTwo(self):
        self.s += self.num2.cget('text')
        self.display = Label(self.master, text = self.s)
        self.display.grid(row=0)
    def getThree(self):
        self.s += self.num3.cget('text')
        self.display = Label(self.master, text = self.s)
        self.display.grid(row=0)
    def getFour(self):
        self.s += self.num4.cget('text')
        self.display = Label(self.master, text = self.s)
        self.display.grid(row=0)

    def getFive(self):
        self.s += self.num5.cget('text')
        self.display = Label(self.master, text = self.s)
        self.display.grid(row=0)

    def getSix(self):
        self.s += self.num6.cget('text')
        self.display = Label(self.master, text = self.s)
        self.display.grid(row=0)
    def getSeven(self):
        self.s += self.num7.cget('text')
        self.display = Label(self.master, text = self.s)
        self.display.grid(row=0)
    def getEight(self):
        self.s += self.num8.cget('text')
        self.display = Label(self.master, text = self.s)
        self.display.grid(row=0)
    def getNine(self):
        self.s += self.num9.cget('text')
        self.display = Label(self.master, text = self.s)
        self.display.grid(row=0)
    def multiplication(self):
         self.s += self.multiply.cget('text')
         self.display = Label(self.master, text = self.s)
         self.display.grid(row=0)
    def getZero(self):
        self.s+= self.zero.cget('text')
        self.display = Label(self.master, text = self.s)
        self.display.grid(row=0)

    def addition(self):
         self.s += self.add.cget('text')
         self.display = Label(self.master, text = self.s)
         self.display.grid(row=0)
    def substract(self):
         self.s += self.minus.cget('text')
         self.display = Label(self.master, text = self.s)
         self.display.grid(row=0)
    def division(self):
         self.s += self.divide.cget('text')
         self.display = Label(self.master, text = self.s)
         self.display.grid(row=0)
    def evaluate(self):
        self.s = eval(self.s)
        print(self.s)
        self.display = Label(self.master, text = '')
        self.display.grid(row=0)
        self.display = Label(self.master, text = self.s)
        self.display.grid(row=0)
        self.s = ''
    
    def close(self):
        self.master.destroy()


root = Tk()
my_gui = MyFirstGUI(root)
print(my_gui.s)
root.mainloop()