# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import *

# ---------------------------- SAVE PASSWORD ------------------------------- #
with open("save_passwords", "w") as pass_doc:
    a =
    pass_doc.write()



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
generate_password = Button(text="Generate Password")
generate_password.grid(row=3, column=2, pady=(0, 7))

add = Button(text="Add", width=38)
add.grid(row=4, column=1, columnspan=2, sticky="w")

window.mainloop()
