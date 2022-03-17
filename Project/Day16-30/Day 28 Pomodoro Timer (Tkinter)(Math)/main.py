import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
countmark = ""
# ---------------------------- TIMER RESET ------------------------------- #


def reset():
    global reps, countmark
    window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(timer_text, text="00: 00")
    timer_label.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
    countmark = ""

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="BREAK", fg=RED,
                           bg=YELLOW, font=(FONT_NAME, 40))
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="BREAK", fg=PINK,
                           bg=YELLOW, font=(FONT_NAME, 40))
    else:
        count_down(work_sec)
        timer_label.config(text="WORK", fg=GREEN, bg=YELLOW,
                           font=(FONT_NAME, 40))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global timer, countmark

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start()
        for _ in range(math.floor(reps/2)):
            countmark += "✔"
            label_cm.config(text=countmark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(
    100, 130, text="00: 00", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(text="This is old text")
timer_label.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
timer_label.grid(row=0, column=1)

# Buttons


button_start = Button(text="Start", command=start,
                      bg=YELLOW, highlightthickness=0)
button_start.grid(row=2, column=0)
button_stop = Button(text="Stop", command=reset,
                     bg=YELLOW, highlightthickness=0)
button_stop.grid(row=2, column=2)

label_cm = Label(font=(
    FONT_NAME, 24, "bold"), bg=YELLOW, fg=GREEN)
label_cm.grid(row=3, column=1)
window.mainloop()
