from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # get password characters using list comprehension
    password_letters = [choice(letters) for _ in range(5)]
    password_symbols = [choice(symbols) for _ in range(2)]
    password_numbers = [choice(numbers) for _ in range(2)]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    # insert generated password to entry box
    password_entry.insert(0, f"{password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #

# function what run after clicked add button
def save_password():
    website_data = website_entry.get()
    email_username_data = email_username_entry.get()
    password_data = password_entry.get()

    if len(website_data) == 0 or len(email_username_data) == 0 or len(password_data) == 0:
        messagebox.showinfo(title="Empty Details", message="Please fill in all the details")

    else:
        ask_ok_cancel = messagebox.askokcancel(title=f"{website_data} email & password",
                                               message=f"These are details you entered:\nEmail : {email_username_data}\n"
                                                       f"Password: {password_data}\n is it ok to save?")

        if ask_ok_cancel:
            with open("save_passwords", "a") as pass_doc:
                pass_doc.write(f"{website_data} | {email_username_data} | {password_data}\n")

            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# creating a canvas for image
canvas = Canvas(height=200, width=160)
image_hold = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image_hold)
canvas.grid(row=0, column=1)

# creating labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="e")

email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0, sticky="e")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="e")

# creating entries
website_entry = Entry(width=45)
website_entry.grid(row=1, column=1, columnspan=2, sticky="w")
website_entry.focus()

email_username_entry = Entry(width=45)
email_username_entry.grid(row=2, column=1, columnspan=2, pady=7, sticky="w")
email_username_entry.insert(0, "harshana@gmail.com")

password_entry = Entry(width=24)
password_entry.grid(row=3, column=1, sticky="w")

# creating buttons
generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(row=3, column=2, pady=(0, 7))

add = Button(text="Add", width=38, command=save_password)
add.grid(row=4, column=1, columnspan=2, sticky="w")

window.mainloop()
