from neural_network import NeuralNetwork
from tkinter import *
import random
import string
import numpy as np

def randColor():
    hexStr = "#"
    for i in range(6):
        hexStr += random.choice(string.ascii_letters[:6] + "123456789")
    return hexStr



if __name__ == "__main__":
    nn = NeuralNetwork(3, 2, 2) # Input 1 is r, 2 is g, 3 is b. Output 1 is white, 2 is black
    bgColor = randColor()

    window = Tk()
    window.title("neural_network.py")
    window.geometry("800x400")

    lbl = Label(window, text="Which text looks better?", font=("Arial Bold", 30))
    lbl.grid(column=1, row=0)

    def getInputs():
        global bgColor
        r = int(bgColor[1:3], 16)
        g = int(bgColor[3:5], 16)
        b = int(bgColor[5:], 16)
        return np.array([r, g, b])

    def updateConfidence():
        output = nn.feedForward(getInputs())
        guess_w.configure(text=output[0])
        guess_b.configure(text=output[1])

    guess_b = Label(window, text="50", font=("Arial Bold", 10))
    guess_b.grid(column=0, row=2)
    guess_w = Label(window, text="50", font=("Arial Bold", 10))
    guess_w.grid(column=2, row=2)
    updateConfidence()

    def clicked(textColor):
        global bgColor
        inputs = getInputs()

        if textColor == "#ffffff":
            nn.train(inputs, [1, 0]) # Again, output 1 is white, 2 is black
        else:
            nn.train(inputs, [0, 1])
        
        bgColor = randColor()
        btn_b.configure(bg=bgColor)
        btn_w.configure(bg=bgColor)
        updateConfidence()
        
    def clicked_w():
        clicked("#ffffff")
    def clicked_b():
        clicked("#000000")

    btn_b = Button(window, padx=15, text="Black", bg=bgColor, fg="#000000", command=clicked_b)
    btn_b.grid(column=0, row=1)
    btn_w = Button(window, padx=15, text="White", bg=bgColor, fg="#ffffff", command=clicked_w)
    btn_w.grid(column=2, row=1)
    
    window.mainloop()