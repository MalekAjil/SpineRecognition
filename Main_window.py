# import tkinter as tk
#
# top = tk.Tk()
# # Code to add widgets will go here...
# top.mainloop()


"""
The example draws lines on the Canvas.
"""

from tkinter import Tk, Canvas, Frame, BOTH, NW, W
from PIL import Image, ImageTk


class Example(Frame):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.master.title("Spine Deformities Recognition")
        self.pack(fill=BOTH, expand=1)

        # canvas = Canvas(self)
        # canvas.create_line(15, 25, 200, 25)
        # canvas.create_line(300, 35, 300, 200, dash=(4, 2))
        # canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)
        #
        # canvas.pack(fill=BOTH, expand=1)

        # canvas = Canvas(self)
        # canvas.create_rectangle(30, 10, 120, 80,
        #                         outline="#fb0", fill="#fb0")
        # canvas.create_rectangle(150, 10, 240, 80,
        #                         outline="#f50", fill="#f50")
        # canvas.create_rectangle(270, 10, 370, 80,
        #                         outline="#05f", fill="#05f")
        #
        # canvas.create_text(20, 130, anchor=W, font="Purisa",
        #                    text="Who doesn't long for someone to hold")
        # canvas.pack(fill=BOTH, expand=1)
        #
        # self.img = Image.open("001.png")
        # self.tatras = ImageTk.PhotoImage(self.img)
        #
        # canvas = Canvas(self, width=self.img.size[0]+20,
        #    height=self.img.size[1]+20)
        # canvas.create_image(300, 10, anchor=NW, image=self.tatras)
        #
        # canvas.pack(fill=BOTH, expand=1)





def main():
    root = Tk()
    ex = Example()
    root.geometry("1200x650")
    root.mainloop()


if __name__ == '__main__':
    main()
