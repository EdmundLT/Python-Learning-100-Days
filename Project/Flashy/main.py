import random
import pandas as pd
from tkinter import *


BACKGROUND_COLOR = "#B1DDC6"
REGULAR_FONT = ("Ariel", 40, "italic")
BOLD_FONT = ("Ariel", 60, "bold")
# ------------------Create New Flash Card --------------------#

try:
    data = pd.read_csv("data/word_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")

data_dict = data.to_dict(orient="records")
current_card = {}


def new_card():
    global current_card
    global timer
    current_card = random.choice(data_dict)
    window.after_cancel(timer)
    canvas.itemconfig(card_image, image=front_image)
    current_french = current_card["French"]
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_french, fill="black")
    timer = window.after(3000, func=flip)


def flip():
    current_english = current_card["English"]
    canvas.itemconfig(card_image, image=back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_english, fill="white")


def correct():
    data_dict.remove(current_card)
    data = pd.DataFrame(data_dict)
    data.to_csv("data/word_to_learn.csv", index=False)
    return new_card()

# ---------------------- Flip the  Card ----------------------#


# -------------------------UI Setup --------------------------#
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flashy")
timer = window.after(3000, func=flip)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526, highlightthickness=0)
card_image = canvas.create_image(400, 263, image=front_image)
card_title = canvas.create_text(400, 150, text="Title",
                                font=REGULAR_FONT, fill="black")
card_word = canvas.create_text(400, 263, text="Word",
                               font=BOLD_FONT, fill="black")

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

canvas.grid(row=0, column=0, columnspan=2)


wrong_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")
# button
wrong_button = Button(
    image=wrong_image, highlightthickness=0, command=new_card)
wrong_button.grid(row=1, column=0, padx=50, pady=50)
right_button = Button(
    image=right_image, highlightthickness=0, command=correct)
right_button.grid(row=1, column=1, padx=50, pady=50)


new_card()
window.mainloop()
