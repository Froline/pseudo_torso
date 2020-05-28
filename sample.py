import sys
import random
from tkinter import *
import tkinter.font as tkfont
from const import *

form = Tk()
form.title('Pseudo Webdriver Torso')
form.geometry('%dx%d' % (WINDOW_WIDTH, WINDOW_HEIGHT))

canvas = Canvas(form, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, \
    bg='#fff', highlightthickness=0)
canvas.place(x=0, y=0)

squares = []
for c in ['#00f','#f00']:
    squares.append(canvas.create_rectangle(0, 0 if c == '#f00' else 200, 100, 100, \
    fill=c, width=0))

nslide = 0
caption = canvas.create_text(10, WINDOW_HEIGHT-30, \
    font=tkfont.Font(family='Courier', size=CAPTION_SIZE, weight='bold'), anchor='w')
#canvas.itemconfigure(caption, text='aqua.flv - slide 0001')

def animation():
    global nslide
    nslide += 1
    canvas.itemconfigure(caption, text='aqua.flv - slide %04d' % nslide)
    for sq in squares:
        canvas.coords(sq, \
            random.randint(0, WINDOW_WIDTH), \
            random.randint(0, WINDOW_HEIGHT), \
            random.randint(0, WINDOW_WIDTH), \
            random.randint(0, WINDOW_HEIGHT), \
            )
    canvas.after(int(1000/FPS), animation)

canvas.after(0, animation)
form.mainloop()
