from PIL import Image
from tkinter import filedialog


def resizeImage(im, width, height, skipdialog=False):
    imNN = im.resize((width, height), Image.NEAREST)        # use nearest neighbour
    # imBL = im.resize((width, height), Image.BILINEAR)     # linear interpolation in a 2x2 environment
    # imBC = im.resize((width, height), Image.BICUBIC)      # cubic spline interpolation in a 4x4 environment
    # imAA = im.resize((width, height), Image.ANTIALIAS)    # best down-sizing filter

    if skipdialog:
        file = "Test.png"
    else:
        myFormats = [('Portable Network Graphics (.png)', '*.png'),
                     ('JPEG / JFIF (.jpg)', '*.jpg'),
                     ('Windows Bitmap (.bmp)', '*.bmp'),
                     ('CompuServer GIF (.gif)', '*.gif')]
        file = filedialog.asksaveasfilename(defaultextension=".png", filetypes=myFormats)

    if file:
        imNN.save(file)
        return file
