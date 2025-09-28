from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.geometry("580x580")
window.title('1st tkinter GUI')
window.config(background="#2a3cc6")

# Frame with grid layout
container = Frame(window, 
                 background="#55ccff",
                 borderwidth=3,
                 relief="solid")
container.pack(pady=20, padx=20)

# Using grid for more control over positioning
title_label = Label(container, text="User Profile", font=('Arial', 20, 'bold'), fg="#2a3cc6", bg="#55ccff")
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Left column - labels
name_label = Label(container, text="Name:", font=('Arial', 12, 'bold'), fg="#2a3cc6", bg="#55ccff", anchor='e')
name_label.grid(row=1, column=0, padx=5, pady=5, sticky='e')

email_label = Label(container, text="Email:", font=('Arial', 12, 'bold'), fg="#2a3cc6", bg="#55ccff", anchor='e')
email_label.grid(row=2, column=0, padx=5, pady=5, sticky='e')

phone_label = Label(container, text="Phone:", font=('Arial', 12, 'bold'), fg="#2a3cc6", bg="#55ccff", anchor='e')
phone_label.grid(row=3, column=0, padx=5, pady=5, sticky='e')

# Right column - values
name_value = Label(container, text="John Doe", font=('Arial', 12), fg="#2a3cc6", bg="#55ccff", anchor='w')
name_value.grid(row=1, column=1, padx=5, pady=5, sticky='w')

email_value = Label(container, text="john@example.com", font=('Arial', 12), fg="#2a3cc6", bg="#55ccff", anchor='w')
email_value.grid(row=2, column=1, padx=5, pady=5, sticky='w')

phone_value = Label(container, text="+1-234-567-8900", font=('Arial', 12), fg="#2a3cc6", bg="#55ccff", anchor='w')
phone_value.grid(row=3, column=1, padx=5, pady=5, sticky='w')

# Button spanning both columns
click_cnt = 0
def click():
    global click_cnt
    click_cnt += 1
    status_label.config(text=f"Updated {click_cnt} times!")

button = Button(container, text='Update Info', command=click, font=('Arial', 14), bg="#2a3cc6", fg="white")
button.grid(row=4, column=0, columnspan=2, pady=15)

status_label = Label(container, text="Ready for updates", font=('Arial', 10), fg="#2a3cc6", bg="#55ccff")
status_label.grid(row=5, column=0, columnspan=2)

window.mainloop()