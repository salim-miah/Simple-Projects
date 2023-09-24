from tkinter import *


class Numbers:
    row = 2
    col = 0

    def __init__(self, number):
        self.number = number
        if number != 0:
            button = Button(root, text=str(number), padx=35, pady=30, font=("Arial",15), bg="Grey", command=self.click)
            if Numbers.col < 3:
                button.grid(row=Numbers.row, column=Numbers.col)
                Numbers.col += 1
            else:
                Numbers.col = 0
                Numbers.row += 1
                button.grid(row=Numbers.row, column=Numbers.col)
                Numbers.col += 1
        else:
            button = Button(root, text=str(number), padx=132, pady=30, font=("Arial",15), bg="Grey", command=self.click)
            button.grid(row=5, column=0, columnspan=3)

    def click(self):
        global entry_index
        entry.insert(entry_index, str(self.number))
        entry_index += 1


class Calculator:
    def __init__(self):
        self.operator = None
        global first_operand
        global second_operand

    def calculate(self):
        if self.operator == "+":
            return first_operand + second_operand
        elif self.operator == "-":
            return first_operand - second_operand
        elif self.operator == "×":
            return first_operand * second_operand
        else:
            return first_operand / second_operand


class Operators:
    row = 1

    def __init__(self, operator):
        self.operator = operator
        button = Button(root, text=operator, padx=30, pady=30, font=("Arial",15), bg="Grey", command=self.click)
        button.grid(row=Operators.row, column=3)
        Operators.row += 1

    def click(self):
        global first_operand
        global second_operand
        if self.operator != "=":
            first_operand = int(entry.get())
            calculator.operator = self.operator
            clear.click()
        else:
            second_operand = int(entry.get())
            result = calculator.calculate()
            clear.click()
            entry.insert(0, result)


class Clear:
    def __init__(self):
        button = Button(root, text="Clear", padx=115, pady=30, font=("Arial",15), command=self.click, bg="Orange")
        button.grid(row=1, column=0, columnspan=3)

    def click(self):
        global entry_index
        entry.delete(0, END)
        entry_index = 0


root=Tk()
root.title("Salim's Calculator")

entry=Entry(root,width=20,borderwidth=5,font=('Arial',25))
entry.grid(row=0,column=0,columnspan=4)
entry_index=0
calculator=Calculator()
number1=Numbers(1)
number2=Numbers(2)
number3=Numbers(3)
number4=Numbers(4)
number5=Numbers(5)
number6=Numbers(6)
number7=Numbers(7)
number8=Numbers(8)
number9=Numbers(9)
number0=Numbers(0)
operator1=Operators("÷")
operator2=Operators("×")
operator3=Operators("-")
operator4=Operators("+")
operator5=Operators("=")
first_operand=None
second_operand=None
clear=Clear()

root.mainloop()


