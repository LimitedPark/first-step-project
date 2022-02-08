from PIL import Image, ImageTk, ImageFilter

import tkinter as tk
window= tk.Tk()
canvas = tk.Canvas(window, width= 500, height=500)
canvas.pack()

window.title("레너 이미지")
img = Image.open("lenna.png")
#out = img.rotate(45)
out = img.filter(ImageFilter.BLUR)
tk_img =ImageTk.PhotoImage(out)
canvas.create_image(250,250, image= tk_img)

window.mainloop()
#fisrt

