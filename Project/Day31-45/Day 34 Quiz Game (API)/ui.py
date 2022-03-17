from tkinter import *
import tkinter
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title = ("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(
            text="Score: 0", bg=THEME_COLOR, fg="white", padx=20, pady=20)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250,
                             highlightthickness=0, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2)

        self.question_text = self.canvas.create_text(150, 150, width=280,
                                                     text="Hello", font=FONT, fill="black")

        self.true_image = PhotoImage(file="images/true.png")
        self.false_image = PhotoImage(file="images/false.png")

        self.true_button = Button(
            image=self.true_image, highlightthickness=0, command=self.true)
        self.true_button.grid(row=2, column=0, padx=20, pady=50)
        self.false_button = Button(
            image=self.false_image, highlightthickness=0, command=self.false)
        self.false_button.grid(row=2, column=1, padx=20, pady=50)
        self.get_next_q()
        self.window.mainloop()

    def get_next_q(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true(self):
        is_right = self.quiz.check_answer("True")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.give_feedback(is_right)

    def false(self):
        is_right = self.quiz.check_answer("False")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_q)
