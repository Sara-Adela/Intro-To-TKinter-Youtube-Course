from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title('Learn To Code at Codemy.com')
root.iconbitmap('c:/gui/codemy.ico')

def open():
	global my_img
	top = Toplevel() # creates a second window
	top.title('My Second Window')
	top.iconbitmap('c:/gui/codemy.ico')
	my_img = ImageTk.PhotoImage(Image.open("images/aspen.png")) # loads picture in the second window
	my_label = Label(top, image=my_img).pack()
	btn2 = Button(top, text="close window", command=top.destroy).pack()



btn = Button(root, text="Open Second Windo", command=open).pack()





mainloop()
