from tkinter import *
FONT = ("Arial", 12, "bold")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=100)

##ROW 0##
Mile_label = Label(text="Label", font=FONT)
Mile_label["text"] = "Miles"
Mile_label.config(text="Miles")
Mile_label.grid(column=2, row=0)

user_input = Entry(width=10)
user_input.grid(column=1, row=0)

def miles_to_km():
    miles = int(user_input.get())
    km = miles * 1.6
    return button_clicked(km)

def button_clicked(km):
    output_label.config(text=km)

##ROW 1##
euqal_label = Label(text="Label", font=FONT)
euqal_label["text"] = "is equal to"
euqal_label.config(text="is equal to")
euqal_label.grid(column=0, row=1)

output_label = Label(text="Label", font=FONT)
output_label["text"] = "0"
output_label.config(text="0")
output_label.grid(column=1, row=1)

km_label = Label(text="Label", font=FONT)
km_label["text"] = "km"
km_label.config(text="km")
km_label.grid(column=2, row=1)

##ROW 2##
button1 = Button(text="Calculate", command=miles_to_km)
button1.grid(column=1, row=2)

window.mainloop()
