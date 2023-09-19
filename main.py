from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(320, 350)

FONT = ("Trebuchet MS", 14, "normal")

label1 = Label(text="Enter Your Weight (kg):", font=FONT)
label1.place(x=50, y=50)

spinbox_kg = Spinbox(from_=0, to=200, font=FONT)
spinbox_kg.place(x=50, y=80)

label2 = Label(text="Enter Your Height (cm):", font=FONT)
label2.place(x=50, y=110)

spinbox_cm = Spinbox(from_=0, to=220, font=FONT)
spinbox_cm.place(x=50, y=140)

label3 = Label(text=" ", font=FONT)
label3.place(x=50, y=230)


def calculate():
    kg = float(spinbox_kg.get())
    cm = float(spinbox_cm.get()) / 100
    bmi = round((kg / (cm ** 2)), 2)

    label4 = Label(text=" ", font=FONT)
    label4.place(x=50, y=260)

    if int(spinbox_kg.get()) == 0 or int(spinbox_kg.get()) == 0:
        label3.config(text="Value must be bigger than 0")
    elif bmi > 30:
        label3.config(text="Your BMI is: {}".format(bmi))
        label4.config(text="You are obese")
    elif 25 < bmi <= 30:
        label3.config(text="Your BMI is: {}".format(bmi))
        label4.config(text="You are overweight")
    elif 18.5 < bmi <= 25:
        label3.config(text="Your BMI is: {}".format(bmi))
        label4.config(text="You are normal")
    elif bmi < 18.5:
        label3.config(text="Your BMI is: {}".format(bmi))
        label4.config(text="You are underweight")


button = Button(text="Calculate", command=calculate, font=FONT)
button.place(x=50, y=180)

window.mainloop()
