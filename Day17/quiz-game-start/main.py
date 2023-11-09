from data import question_data
from question_model import Question
from quiz_brain import QuizzBrain

question_bank = []
for item in question_data:
    question = Question (item['text'], item['answer'])
    question_bank.append(question)


ok = 0
score =0

quiz = QuizzBrain(question_bank)

while quiz.still_questions():
    quiz.nextquestion()

print (f"Your final score was:{quiz.score}/{len(question_bank)} ")