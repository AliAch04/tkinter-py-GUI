from tkinter import *
from PIL import Image, ImageTk

#--------Window--------#
window = Tk() #instantiate
window.geometry("580x580")
window.title('1st tkinter GUI')

# convert image to PhotoImage to use it as icon for the window
img = Image.open('zoz_logo.jpg')
# img.show()
icon = ImageTk.PhotoImage(img)
window.iconphoto(True, icon)

#changing the window
window.config(background="#2a3cc6")

#--------Label--------#
#create and config the label
img_label = Image.open('placeholder.png')
img_label = img_label.resize((150, 150), Image.LANCZOS)  # Resize image to fit label
label_photo = ImageTk.PhotoImage(img_label)
label = Label(window, 
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

button = Button(window,
                text='Click',
                command=click,
                font=('Comic Sans', 30)) 
button.pack(pady=10) # Added padding to separate from label


window.mainloop() #activate the window and listen for events!