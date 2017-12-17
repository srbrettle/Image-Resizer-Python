from PIL import Image
from tkinter import filedialog


def resizeImage(im, filtr, width, height, skipdialog=False):
    if filtr == "Nearest Neighbour":
        image = im.resize((width, height), Image.NEAREST)      # nearest neighbour
    elif filtr == "Bilinear":
        image = im.resize((width, height), Image.BILINEAR)     # bilinear interpolation
    elif filtr == "Bicubic":
        image = im.resize((width, height), Image.BICUBIC)      # bicubic interpolation
    elif filtr == "Anti-Alias":
        image = im.resize((width, height), Image.ANTIALIAS)    # antialiasing

    if skipdialog:
        file = (filtr + ".png")
    else:
        myFormats = [('Portable Network Graphics (.png)', '*.png'),
                     ('JPEG / JFIF (.jpg)', '*.jpg'),
                     ('Windows Bitmap (.bmp)', '*.bmp'),
                     ('CompuServer GIF (.gif)', '*.gif')]
        file = filedialog.asksaveasfilename(defaultextension=".png", filetypes=myFormats)

    if file:
        image.save(file)
        return file
