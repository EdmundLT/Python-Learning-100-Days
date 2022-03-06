# Day 34 Exercise - Quiz Game (API)

- main.py
    
    ```python
    from question_model import Question
    from data import question_data
    from quiz_brain import QuizBrain
    from ui import QuizInterface
    question_bank = []
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)
    
    quiz = QuizBrain(question_bank)
    quiz_ui = QuizInterface(quiz)
    
    # while quiz.still_has_questions():
    #     quiz.next_question()
    
    print("You've completed the quiz")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")
    ```
    
- data.py
    
    ```python
    import requests
    response = requests.get(
        url="https://opentdb.com/api.php?amount=10&type=boolean")
    
    data = response.json()
    question_data = data["results"]
    ```
    
- question_model.py
    
    ```python
    class Question:
    
        def __init__(self, q_text, q_answer):
            self.text = q_text
            self.answer = q_answer
    ```
    
- quiz_brain.py
    
    ```python
    import html
    
    class QuizBrain:
    
        def __init__(self, q_list):
            self.question_number = 0
            self.score = 0
            self.question_list = q_list
            self.current_question = None
    
        def still_has_questions(self):
            return self.question_number < len(self.question_list)
    
        def next_question(self):
            self.current_question = self.question_list[self.question_number]
            self.question_number += 1
            q_text = html.unescape(self.current_question.text)
            return f"Q.{self.question_number}: {q_text}"
    
        def check_answer(self, user_answer):
            correct_answer = self.current_question.answer
            if user_answer == correct_answer:
                self.score += 1
                return True
            else:
                return False
    
            print(f"Your current score is: {self.score}/{self.question_number}")
            print("\n")
    ```
    
- ui.py
    
    ```python
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
    ```
    
-
