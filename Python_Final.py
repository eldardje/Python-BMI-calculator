'''
Program Name: Python_Final.py
Program Purpose: Creating a BMI Calculator
Date Written: 12/3/2021
Programer: Eldar Djedovic
'''

import tkinter as tk
from PIL import Image, ImageTk
from tkinter import *

window = tk.Tk()
window.geometry("620x780")
window.title("BMI Calculator")

# Names of the data feilds
name = tk.Label(text = "Name")
name.grid(column = 0, row = 0)

weight = tk.Label(text = "Enter Your Weight in Pounds")
weight.grid(column = 0, row = 1)

height = tk.Label(text = "Enter Your Height in Inches")
height.grid(column = 0, row = 2)

#Test feilds

nameEntry = tk.Entry()
nameEntry.grid(column = 1, row = 0)

weightEntry = tk.Entry()
weightEntry.grid(column = 1, row = 1)

heightEntry = tk.Entry()
heightEntry.grid(column = 1, row = 2)
# Doing the calculation


def BMICALC():

    name = nameEntry.get()
    LBS = int(weightEntry.get())
    inch = int(heightEntry.get())

    bmi = ((LBS / (inch**2)) * 703 )
    BMI = round(bmi, 2)
    textArea = tk.Text(master = window, height = 5, width = 35)
    textArea.grid(column = 1, row = 6)


    if BMI < 18.5:
        status = 'Underweight'
    elif 18.5 <= BMI <= 24.9:
        status = "Normal Weight"
    elif 25 <= BMI <= 29.5:
        status = 'Over Weight'
    elif BMI > 29.5:
        status = 'Obese'
    else:
        status = 'This is not possible'




    answer = f'Hello {name} your BMI is {BMI}, you are {status}.'

    textArea.insert(tk.END, answer)



button = tk.Button(window, text="Calculate", command=BMICALC, bg="yellow")

button.grid(column= 1, row= 5)

window.mainloop()


























































































