import tkinter as tk
from PIL import Image, ImageTk
import random
from itertools import count
class ImageLabel(tk.Label):
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []
        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100
        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()
    def unload(self):
        self.config(image="")
        self.frames = None
    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)
def move_image():
    x = random.randint(0, root.winfo_width() - lbl.winfo_width())
    y = random.randint(0, root.winfo_height() - lbl.winfo_height())
    lbl.place(x=x, y=y)
root = tk.Tk()
lbl = ImageLabel(root)
lbl.pack()
lbl.load('cat-meme-funny.gif')
move_button = tk.Button(root, text="Move Image", command=move_image)
move_button.pack()
root.mainloop()
