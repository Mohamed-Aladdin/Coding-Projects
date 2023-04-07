from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# -------------------------- PASSWORD GENERATOR ----------------------------- #
def generate_password():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  nr_letters = random.randint(8, 10)
  nr_numbers = random.randint(2, 4)
  nr_symbols = random.randint(2, 4)

  password_letters = [random.choice(letters) for _ in range(nr_letters)]
  password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
  password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

  password_list = password_letters + password_numbers + password_symbols
  random.shuffle(password_list)

  passphrase = "".join(password_list)
  password_entry.insert(0, passphrase)

  pyperclip.copy(passphrase)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_creds():
  website = website_entry.get().title()
  email = email_entry.get()
  password = password_entry.get()

  if len(website) == 0 or len(password) == 0:
    messagebox.showinfo(title="Ooops!", message="Please make sure you haven't left any fields empty!")
  else:

    save = messagebox.askokcancel(title=website, message=f"These're the info entered: \nEmail: {email}\nPassword: {password}\nWould you like to save them?")

    if save:
      with open("data.txt", "a") as file:
        file.write(f"{website} | {email} | {password}\n")

      website_entry.delete(0, END)
      password_entry.delete(0, END)
      website_entry.focus()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(column=2, row=3)
add_btn = Button(text="Add", width=44, command=save_creds)
add_btn.grid(column=1, row=4, columnspan=2)

website_entry = Entry(width=52)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=52)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "mohamed.aladdin10@gmail.com")
password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)

window.mainloop()