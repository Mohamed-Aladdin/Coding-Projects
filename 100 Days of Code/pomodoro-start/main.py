from tkinter import *
import math
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

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
  global reps
  window.after_cancel(timer)
  timer_label.config(text="Timer", fg=GREEN)
  canvas.itemconfig(timer_text, text="00:00")
  check_mark.config(text="")
  reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
  global reps
  reps += 1
  if reps % 8 == 0:
    countdown(LONG_BREAK_MIN)
    timer_label.config(text="Break", fg=PINK)
  elif reps % 2 == 0:
    countdown(SHORT_BREAK_MIN * 60)
    timer_label.config(text="Break", fg=RED)
  else:
    countdown(WORK_MIN * 60)
    timer_label.config(text="Work", fg=GREEN)
# ---------------------------COUNT DOWN MECHANISM------------------------------#
def countdown(count):
  global timer
  count_min = math.floor(count / 60)
  count_sec = count % 60

  if count_sec < 10:
    count_sec = f"0{count_sec}"

  if count_min < 10:
    count_min = f"0{count_min}"

  canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
  if count > 0:
    timer = window.after(1000, countdown, count - 1)
  else:
    start_timer()
    marks = ""
    for _ in range(math.floor(reps / 2)):
      marks += "✔"
    check_mark.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_btn = Button(text="Start", highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_btn.grid(column=2, row=2)

window.mainloop()