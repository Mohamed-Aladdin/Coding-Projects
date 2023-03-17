from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for q in question_data:
  new_q = Question(q["question"], q["correct_answer"])
  question_bank.append(new_q)

quiz = QuizBrain(question_bank)
while quiz.still_has_qs():
  quiz.next_q()
print("You've completed the quiz!")
print(f"Your final score is: {quiz.score}/{quiz.q_number}")