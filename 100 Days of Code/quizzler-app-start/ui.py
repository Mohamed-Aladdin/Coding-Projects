from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 16, "italic")

class QuizInterface:
  def __init__(self, quiz_brain: QuizBrain):
    self.quiz = quiz_brain

    self.window = Tk()
    self.window.title("Quizzler")
    self.window.config(padx=20, pady=20, bg=THEME_COLOR)

    self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 12, "bold"))
    self.score_label.grid(column=1, row=0)

    self.canvas = Canvas(width=300, height=250, bg="white")
    self.question_text = self.canvas.create_text(150, 125, width=280, text="Question goes here!", fill=THEME_COLOR, font=FONT)
    self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

    true_img = PhotoImage(file="images/true.png")
    false_img = PhotoImage(file="images/false.png")

    self.true_btn = Button(image=true_img, highlightthickness=0, command=self.pressed_true)
    self.true_btn.grid(column=0, row=2)

    self.false_btn = Button(image=false_img, highlightthickness=0, command=self.pressed_false)
    self.false_btn.grid(column=1, row=2)

    self.get_next_q()

    self.window.mainloop()

  def get_next_q(self):
    self.canvas.config(bg="white")
    self.score_label.config(text=f"Score: {self.quiz.score}")
    
    if self.quiz.still_has_questions():
      q_text = self.quiz.next_question()
      self.canvas.itemconfig(self.question_text, text=q_text)
    else:
      self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
      self.true_btn.config(state="disabled")
      self.false_btn.config(state="disabled")

  def pressed_true(self):
    self.give_feedback(self.quiz.check_answer("True"))
      
  def pressed_false(self):
    self.give_feedback(self.quiz.check_answer("False"))

  def give_feedback(self, is_right):
    if is_right:
      self.canvas.config(bg="green")
    else:
      self.canvas.config(bg="red")
    
    self.window.after(1000, self.get_next_q)