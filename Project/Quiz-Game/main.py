from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for x in question_data:
    new_q = Question(x["text"], x["answer"])
    question_bank.append(new_q)


quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()
print("You have completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
