
from tkinter import *

from PIL import ImageTk, Image

root = Tk()

root.title("Image Viewer")
root.attributes('-fullscreen',True)

root.geometry("700x700")

image_no_1 = ImageTk.PhotoImage(Image.open("image5.png").resize((10200,3000)))

List_images = [image_no_1]
label = Label(image=image_no_1, anchor= CENTER).place(relx=.5, rely=.5, anchor=CENTER)

button_exit = Button(root, text="Exit", command=root.quit)
button_exit.grid(row=5, column=1)

root.mainloop()