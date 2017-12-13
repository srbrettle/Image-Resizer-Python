from tkinter import Tk, Label, Entry, Button, StringVar, W, E, filedialog
import imageManipulation
from PIL import Image


class Gui:

    def __init__(self, master):
        self.master = master
        master.title("Image Resizer")

        self.filename = "..."
        self.xOrig = "X"
        self.yOrig = "Y"

        self.filename_label_text = StringVar()
        self.filename_label_text.set(self.filename)
        self.filename_label = Label(master, textvariable=self.filename_label_text)

        self.title_filename_label = Label(master, text="Filename:")
        self.title_original = Label(master, text="Original:")
        self.title_resize = Label(master, text="Resize:")
        self.label_x = Label(master, text="Width:")
        self.label_y = Label(master, text="Height:")

        self.label_x_orig_text = StringVar()
        self.label_x_orig_text.set(self.xOrig)
        self.label_x_orig = Label(master, textvariable=self.label_x_orig_text)
        self.label_y_orig_text = StringVar()
        self.label_y_orig_text.set(self.yOrig)
        self.label_y_orig = Label(master, textvariable=self.label_y_orig_text)

        vc = (master.register(self.validate),
              '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.contentX = StringVar()
        self.entryX = Entry(master, text="Width: ", validate='key', validatecommand=vc,  textvariable=self.contentX)
        self.contentY = StringVar()
        self.entryY = Entry(master, text="Height: ", validate='key', validatecommand=vc, textvariable=self.contentY)

        self.browse_button = Button(master, text="Browse...", command=lambda: self.update("browse"))
        self.generate_button = Button(master, text="Generate", command=lambda: self.update("generate"))
        self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))

        # Layout
        self.title_filename_label.grid(row=0, column=0, sticky=W)
        self.browse_button.grid(row=0, column=4, sticky=W+E)
        self.filename_label.grid(row=0, column=1, columnspan=3, sticky=W)
        self.title_original.grid(row=1, column=1, sticky=W+E)
        self.title_resize.grid(row=1, column=4, sticky=W+E)
        self.label_x.grid(row=2, column=0, sticky=W)
        self.label_y.grid(row=3, column=0, sticky=W)
        self.label_x_orig.grid(row=2, column=1, sticky=W+E)
        self.label_y_orig.grid(row=3, column=1, sticky=W+E)
        self.entryX.grid(row=2, column=4, sticky=W+E)
        self.entryY.grid(row=3, column=4, sticky=W+E)
        self.generate_button.grid(row=4, column=0, columnspan=4, sticky=W+E)
        self.reset_button.grid(row=4, column=4, sticky=W+E)

        self.im = Image

    def update(self, method):
        if method == "browse":
            self.clear()
            root = Tk()
            file = filedialog.askopenfile(parent=root, mode='rb', title='Choose a file')
            if file is not None:
                self.filename = file.name
                self.filename_label_text.set(self.filename)

                # Populate original width and height fields
                self.im = Image.open(self.filename)
                origWidth, origHeight = self.im.size
                self.xOrig = origWidth
                self.label_x_orig_text.set(self.xOrig)
                self.yOrig = origHeight
                self.label_y_orig_text.set(self.yOrig)
                self.contentX.set(origWidth)
                self.contentY.set(origHeight)
            root.withdraw()
        elif method == "generate":
            if not (self.contentX.get() == "") or (self.contentY.get() == ""):
                imageManipulation.resizeImage(self.im, int(self.contentX.get()), int(self.contentY.get()))
        else:  # reset
            self.clear()

    def clear(self):
        self.filename = "..."
        self.filename_label_text.set(self.filename)
        self.xOrig = "X"
        self.label_x_orig_text.set(self.xOrig)
        self.yOrig = "Y"
        self.label_y_orig_text.set(self.yOrig)
        self.contentX.set("")
        self.contentY.set("")

    def validate(self, action, index, value_if_allowed,
                 prior_value, text, validation_type, trigger_type, widget_name):
        if text in '0123456789':
            if len(value_if_allowed) != 0:
                try:
                    int(value_if_allowed)
                    return True
                except ValueError:
                    return False
        else:
            return False


root = Tk()
my_gui = Gui(root)
root.mainloop()
