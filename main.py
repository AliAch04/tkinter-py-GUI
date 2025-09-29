from tkinter import *
from PIL import Image, ImageTk

#--------Window--------#
window = Tk() #instantiate
window.geometry("580x580")
window.title('1st tkinter GUI')
window.resizable(False, False)

# convert image to PhotoImage to use it as icon for the window
img = Image.open('zoz_logo.jpg')
# img.show()
icon = ImageTk.PhotoImage(img)
window.iconphoto(True, icon)

#changing the window
window.config(background="#2a3cc6")


#-------Container-------#
container = Frame(window,
                  background='#2255ff',
                  borderwidth=2,
                  relief="solid")
container.pack(fill=BOTH, expand=True, padx=10, pady=5)

#--------Label--------#
#create and config the label
img_label = Image.open('placeholder.png')
img_label = img_label.resize((150, 150), Image.LANCZOS)  # Resize image to fit label
label_photo = ImageTk.PhotoImage(img_label)
label = Label(container, 
              text="hello from widget", 
              font=('Arial',40,'bold'), 
              fg="#2a3cc6", 
              background="#55ccff",
              padx=30,
              pady=5,
              image=label_photo,
              compound='bottom',
              relief='solid',
              borderwidth=2)
label.pack() #activate the label
#label.place(x=0, y=50)

#--------Button--------#
#create and config the button
click_cnt = 0
def click():
    global click_cnt
    print(f'you clicked : {click_cnt}')
    click_cnt +=1

button = Button(container,
                text='Click',
                command=click,
                font=('Comic Sans', 10)) 
button.pack(fill=X, padx=30, pady=10) # Added padding to separate from label


#--------Entry--------#
container_entry = Frame(container,
                        borderwidth=2,
                        relief="solid")
container_entry.pack(fill=X, padx=15)

entry = Entry(container_entry,
              width=40,
              font=('Arial', 12),
              fg="#a9a9a9",  # gray color for placeholder
              state='normal')

placeholder_text = 'Write Some Text Here'
entry.insert(0, placeholder_text)

def on_focus_in(event):
    if entry.get() == placeholder_text:
        entry.delete(0, END)
        entry.config(fg="#363636")  # normal text color

def on_focus_out(event):
    if entry.get() == '':
        entry.insert(0, placeholder_text)
        entry.config(fg="#a9a9a9")  # placeholder color

entry.bind("<FocusIn>", on_focus_in)
entry.bind("<FocusOut>", on_focus_out)
entry.pack(side=LEFT, padx=5, pady=15)

def submit():
    content = entry.get()
    if content != placeholder_text:
        print(f'You typed : {content}')
        entry.config(show='*')
    else:
        print("No input provided.")

submit_entry = Button(container_entry,
                      text='Submit',
                      font=('Comic Sans', 10),
                      background="#7dda6a",
                      activebackground="#bbffad",
                      command=submit)
submit_entry.pack(side=LEFT, expand=True)

def delete():
    entry.delete(0, END)
    entry.insert(0, placeholder_text)
    entry.config(fg="#a9a9a9", show='')
    window.focus_set() # set focus to window


clear_entry = Button(container_entry,
                     text='Clear',
                     font=('Comic Sans', 10),
                     background="#da806a",
                     activebackground="#ffb3a0",
                     command=delete)
clear_entry.pack(side=RIGHT, expand=True)


window.mainloop() #activate the window and listen for events!