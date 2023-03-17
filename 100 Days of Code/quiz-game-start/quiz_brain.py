class QuizBrain:

  def __init__(self, q_list,):
    self.q_number = 0
    self.score = 0
    self.q_list = q_list

  def next_q(self):
    question = self.q_list[self.q_number]
    self.q_number += 1
    ans = input(f"Q.{self.q_number}: {question.text} (True/False): ").title()
    self.check_answer(ans, question.answer)

  def still_has_qs(self):
    return self.q_number < len(self.q_list)

  def check_answer(self, ans, correct_ans):
    if ans == correct_ans:
      print("You got it right!")
      self.score += 1
    else:
      print("That's wrong.")
    print(f"The correct answer was: {correct_ans}.")
    print(f"Your current score is: {self.score}/{self.q_number}")
    print("\n")