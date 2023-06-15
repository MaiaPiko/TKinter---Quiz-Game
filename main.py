from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizzUserInterface

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(q_list=question_bank)
quiz_ui = QuizzUserInterface(quiz)

# quiz_on = True
# # while quiz_on:


# print("You've completed the quiz")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")
