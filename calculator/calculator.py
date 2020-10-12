import tkinter as tk
from PIL import Image, ImageTk


root = tk.Tk()

canvas = tk.Canvas(root, height = 800, width = 800, bg = "white")
canvas.pack()

frame = tk.Frame(root, bg = "grey")
frame.place(relwidth= 1, relheight = 0.8, rely = 0.25)

numberOne = ""
numberTwo = ""
number = 1
intOne = 1
intTwo = 2
#1 is equal to sum

def inputOne():
    global numberOne
    numberOne = numberOne + "1"
    label = tk.Label(canvas, text = numberOne)
    label.place(relx = 0.1, relwidth = 1)

def inputTwo():
    global numberOne
    numberOne = numberOne + "2"
    label = tk.Label(canvas, text = numberOne)
    label.place(relx = 0.1, relwidth = 1)

def inputThree():
    global numberOne
    numberOne = numberOne + "3"
    label = tk.Label(canvas, text = numberOne)
    label.place(relx = 0.1, relwidth = 1)

def inputFour():
    global numberOne
    numberOne = numberOne + "4"
    label = tk.Label(canvas, text = numberOne)
    label.place(relx = 0.1, relwidth = 1)

def inputFive():
    global numberOne
    numberOne = numberOne + "5"
    label = tk.Label(canvas, text = numberOne)
    label.place(relx = 0.1, relwidth = 1)

def inputSix():
    global numberOne
    numberOne = numberOne + "6"
    label = tk.Label(canvas, text = numberOne)
    label.place(relx = 0.1, relwidth = 1)

def inputSeven():
    global numberOne
    numberOne = numberOne + "7"
    label = tk.Label(canvas, text = numberOne)
    label.place(relx = 0.1, relwidth = 1)

def inputEight():
    global numberOne
    numberOne = numberOne + "8"
    label = tk.Label(canvas, text = numberOne)
    label.place(relx = 0.1, relwidth = 1)

def inputNine():
    global numberOne
    numberOne = numberOne + "9"
    label = tk.Label(canvas, text = numberOne)
    label.place(relx = 0.1, relwidth = 1)

def inputZero():
    global numberOne
    numberOne = numberOne + "0"
    label = tk.Label(canvas, text = numberOne)
    label.place(relx = 0.1, relwidth = 1)


def inputSum():
    global numberOne
    global numberTwo
    global number
    global intOne
    global intTwo

    numberTwo = numberOne
    number = 1

    
    intTwo = int(numberTwo)

    numberOne = ""

def inputMinus():
    global numberOne
    global numberTwo
    global number
    global intOne
    global intTwo

    numberTwo = numberOne
    number = 2

    
    intTwo = int(numberTwo)

    numberOne = ""

def inputMultiply():
    global numberOne
    global numberTwo
    global number
    global intOne
    global intTwo

    numberTwo = numberOne
    number = 3

    
    intTwo = int(numberTwo)

    numberOne = ""

def inputDivide():
    global numberOne
    global numberTwo
    global number
    global intOne
    global intTwo

    numberTwo = numberOne
    number = 4

    
    intTwo = int(numberTwo)

    numberOne = ""

def equal():
    global numberOne
    global numberTwo
    global number
    global intOne
    global intTwo

    intOne = int(numberOne)

    if number == 1:
        total = intOne + intTwo
        label = tk.Label(canvas, text = total)
        label.place(relx = 0.1, relwidth = 1)
    elif number == 2:
        total = intTwo - intOne
        label = tk.Label(canvas, text = total)
        label.place(relx = 0.1, relwidth = 1)
    elif number == 3:
        total = intTwo * intOne
        label = tk.Label(canvas, text = total)
        label.place(relx = 0.1, relwidth = 1)
    else:
        total = intTwo / intOne
        label = tk.Label(canvas, text = total)
        label.place(relx = 0.1, relwidth = 1)

def clear():
    global numberOne

    numberOne = ""
    label = tk.Label(canvas, text = numberOne)
    label.place(relx = 0.1, relwidth = 1)




    






buttonOne = tk.Button(frame, text = "1", fg = "black", command = inputOne, highlightcolor= "blue")
buttonOne.place(relheight = 0.25, relwidth = 0.2)

buttonTwo = tk.Button(frame, text = "2", fg = "black", command = inputTwo)
buttonTwo.place(relheight = 0.25, relwidth = 0.2,relx = 0.2)

buttonThree = tk.Button(frame, text = "3", fg = "black", command = inputThree)
buttonThree.place(relheight = 0.25, relwidth = 0.2, relx = 0.4)

buttonFour = tk.Button(frame, text = "4", fg = "black", command = inputFour)
buttonFour.place(relheight = 0.25, relwidth = 0.2, rely = 0.25)

buttonFive = tk.Button(frame, text = "5", fg = "black", command = inputFive)
buttonFive.place(relheight = 0.25, relwidth = 0.2, rely = 0.25, relx = 0.2)

buttonSix = tk.Button(frame, text = "6", fg = "black", command = inputSix)
buttonSix.place(relheight = 0.25, relwidth = 0.2, rely = 0.25, relx = 0.4)

buttonSeven = tk.Button(frame, text = "7", fg = "black", command = inputSeven)
buttonSeven.place(relheight = 0.25, relwidth = 0.2,rely = 0.5)

buttonEight = tk.Button(frame, text = "8", fg = "black", command = inputEight)
buttonEight.place(relheight = 0.25, relwidth = 0.2, rely = 0.5, relx = 0.2)

buttonNine = tk.Button(frame, text = "9", fg = "black", command = inputNine)
buttonNine.place(relheight = 0.25, relwidth = 0.2, rely = 0.5, relx = 0.4)

buttonZero = tk.Button(frame, text = "0", fg = "black", command = inputZero)
buttonZero.place(relheight = 0.2, relwidth = 0.2, rely = 0.75)



buttonSum = tk.Button(frame, text = "+", fg = "black", command = inputSum)
buttonSum.place(relheight = 0.25, relwidth = 0.4, relx = 0.6)

buttonMinus = tk.Button(frame, text = "-", fg = "black", command = inputMinus)
buttonMinus.place(relheight = 0.25, relwidth = 0.4, relx = 0.6, rely = 0.25)

buttonMulitply = tk.Button(frame, text = "X", fg = "black", command = inputMultiply)
buttonMulitply.place(relheight = 0.25, relwidth = 0.4, relx = 0.6, rely = 0.5)

buttonDivide = tk.Button(frame, text = "/", fg = "black", command = inputDivide)
buttonDivide.place(relheight = 0.2, relwidth = 0.4, relx = 0.6, rely = 0.75)

buttonEqual = tk.Button(frame, text = "=", fg = "black", command = equal)
buttonEqual.place(relheight = 0.2, relwidth = 0.2, relx = 0.4, rely = 0.75)

buttonClear = tk.Button(frame, text = "Clear", fg = "black", command = clear)
buttonClear.place(relheight = 0.2, relwidth = 0.2, relx = 0.2, rely = 0.75)





root.mainloop()
