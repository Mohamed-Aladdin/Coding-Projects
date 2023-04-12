from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
  words_df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
  words_df = pandas.read_csv("data/french_words.csv")

words_dict = words_df.to_dict(orient="records")

# ---------------------------- Next Card ------------------------------- #
def next_card():
  global word, flip_timer

  window.after_cancel(flip_timer)

  word = random.choice(words_dict)
  canvas.itemconfig(card_img, image=card_front_img)
  canvas.itemconfig(card_title, text="French", fill="black")
  canvas.itemconfig(card_word, text=word["French"], fill="black")

  flip_timer = window.after(3000, flip_card)
# ---------------------------- Flip Card ------------------------------- #
def flip_card():
  canvas.itemconfig(card_img, image=card_back_img)
  canvas.itemconfig(card_title, text="English", fill="white")
  canvas.itemconfig(card_word, text=word["English"], fill="white")
# ------------------------- Remove Word From List ---------------------------- #
def remove_word():
  words_dict.remove(word)
  new_df = pandas.DataFrame(words_dict)
  new_df.to_csv("data/words_to_learn.csv", index=False)

  next_card()
# ---------------------------- UI SETUP ------------------------------- #
window  = Tk()
window.title("Flash Cards!")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", fill="black", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", fill="black", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_btn = Button(image=wrong_img, highlightthickness=0, borderwidth=0, command=next_card)
wrong_btn.grid(column=0, row=1)

right_btn = Button(image=right_img, highlightthickness=0, borderwidth=0, command=remove_word)
right_btn.grid(column=1, row=1)

next_card()

window.mainloop()