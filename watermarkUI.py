from tkinter import *
from tkinter import filedialog
from PIL import Image
import os


class WaterMarkUI:
    def __init__(self):
        self.main = Tk()
        self.main.geometry("400x200")
        # self.main.config(background="Light Blue")
        self.main.title("WaterMark App")

        self.title_label = Label(text="Add WaterMark to your Image")
        self.title_label.grid(column=1, row=0, pady=25, padx=50)

        self.upload_label = Label(text="Photo:")
        self.upload_label.grid(column=0, row=1)

        self.file_path = Entry(width=40, insertborderwidth=1)
        self.file_path.grid(column=1, row=1)

        self.browse_btn = Button(text="Browse Image", command=self.browse)
        self.browse_btn.grid(column=2, row=1)

        self.upload_btn = Button(text="Add WaterMark", command=self.add_water_mark)
        self.upload_btn.grid(column=1, row=2)

        self.main.mainloop()

    def browse(self):
        filename = filedialog.askopenfilename(initialdir="/",
                                              title="Select a File",
                                              filetypes=(("Text files",
                                                          "*.jpg*"),
                                                         ("all files",
                                                          "*.*")))
        if filename:
            self.file_path.insert(0, str(filename))

    def add_water_mark(self):
        im = Image.open(str(self.file_path.get()))
        wm = Image.open("C:/Users/Berkay/Desktop/PYTHON/resizedlogo.png")
        im.paste(wm, (100, 50))
        im.save(str(self.file_path.get()), quality=95)
        self.file_path.delete(0, END)


demo = WaterMarkUI()





# wm = Image.open("C:/Users/Berkay/Desktop/PYTHON/mcdonaldlogo.png")
#
# # Resize the image
# resized_wm = wm.resize((50, 50), Image.Resampling.LANCZOS)
#
# # Save the resized image
# resized_wm.save("C:/Users/Berkay/Desktop/PYTHON/resizedlogo.png", quality=100)
