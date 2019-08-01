# from neural_network import NeuralNetwork
import tensorflow as tf
from tensorflow import keras

from tkinter import *
import random
import string
import numpy as np

import csv


FILE_NAME = "ColorGuessData.csv"


def randColor():
    hexStr = "#"
    for i in range(6):
        hexStr += random.choice(string.ascii_letters[:6] + "123456789")
    return hexStr

def loadCSV():
    with open(FILE_NAME) as file:
        reader = csv.reader(file, delimiter=',')

        rowNum = 0
        inputs = np.array([[]])
        labels = np.array([])

        for row in reader:
            if rowNum == 0:
                rowNum += 1
            elif rowNum == 1:
                rowNum += 1
                inputs = np.array([[int(row[0]), int(row[1]), int(row[2])]])
                labels = np.array([int(row[3])])
            else:
                inputs = np.append(inputs, [[int(row[0]), int(row[1]), int(row[2])]], axis=0)
                labels = np.append(labels, [int(row[3])])
        
        return inputs, labels
    
def updateCSV(colors, labels):
    # The part after "labels" transposes it
    csvArray = np.append(colors, labels[ : , np.newaxis], axis=1)
    csvArray = np.append([['R', 'G', 'B', "Label"]], csvArray, axis=0)
    np.savetxt(FILE_NAME, csvArray, delimiter=',', fmt='%s')
        

if __name__ == "__main__":
    # nn = NeuralNetwork(3, 2, 2) # Input 1 is r, 2 is g, 3 is b. Output 1 is black, 2 is white
    model = keras.Sequential([
        keras.layers.Dense(4, activation=tf.nn.sigmoid, input_dim=3),
        keras.layers.Dense(4, activation=tf.nn.sigmoid),
        keras.layers.Dense(2, activation=tf.nn.softmax)
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    bgColor = randColor()
    inputs, labels = loadCSV()
    print(inputs, labels)

    window = Tk()
    window.title("neural_network.py")
    window.geometry("800x400")

    lbl = Label(window, text="Which text looks better?", font=("Arial Bold", 30))
    lbl.grid(column=1, row=0)

    def getCurrInputs():
        global bgColor
        r = int(bgColor[1:3], 16) / 255.
        g = int(bgColor[3:5], 16) / 255.
        b = int(bgColor[5:], 16) / 255.
        return np.array([[r, g, b]])

    def updateConfidence():
        output = model.predict(getCurrInputs()) # nn.feedForward(getCurrInputs())
        print(output)
        guess_w.configure(text=output[0][1])
        guess_b.configure(text=output[0][0])

    guess_b = Label(window, text="50", font=("Arial Bold", 10))
    guess_b.grid(column=0, row=2)
    guess_w = Label(window, text="50", font=("Arial Bold", 10))
    guess_w.grid(column=2, row=2)
    updateConfidence()

    def clicked(textColor):
        global bgColor
        global inputs
        global labels
        if inputs.size == 0:
            inputs = getCurrInputs()
        else:
            inputs = np.append(inputs, getCurrInputs(), axis=0) # getCurrInputs()

        if textColor == "#ffffff":
            # nn.train(inputs, [1, 0]) # Again, output 1 is white, 2 is black
            labels = np.append(labels, 1)
        else:
            # nn.train(inputs, [0, 1])
            labels = np.append(labels, 0)
        model.fit(inputs, labels, epochs=10)
        
        bgColor = randColor()
        btn_b.configure(bg=bgColor)
        btn_w.configure(bg=bgColor)
        updateConfidence()
        updateCSV(inputs, labels)
        
    def clicked_w():
        clicked("#ffffff")
    def clicked_b():
        clicked("#000000")

    btn_b = Button(window, padx=15, text="This BLACK text?...", bg=bgColor, fg="#000000", command=clicked_b)
    btn_b.grid(column=0, row=1)
    btn_w = Button(window, padx=15, text="Or this WHITE text?...", bg=bgColor, fg="#ffffff", command=clicked_w)
    btn_w.grid(column=2, row=1)
    
    window.mainloop()