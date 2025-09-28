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



window.mainloop() #activate the window and listen for events!