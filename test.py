import unittest
import os.path
import imghdr
from PIL import Image
import imageManipulation


class TestMethods(unittest.TestCase):                            
        
    def test_test_file_exists(self):
        self.assertTrue(os.path.isfile("C:\\test.png"))

    def test_test_file_is_image(self):
        self.assertNotEqual(imghdr.what("C:\\test.png"), None)

    def test_diallow_non_images(self):
        fpath = "C:\\test.txt"
        #Check from main.py
        if imghdr.what(fpath) is not None:
            im = Image.open(fpath)
            width = 500
            height = 500
            imageManipulation.resizeImage(im, width, height, True)

    def test_create(self):        
        im = Image.open("C:\\test.png")
        filtr = "Nearest Neighbour"
        self.width = 500
        self.height = 500
        self.im2path = imageManipulation.resizeImage(im, filtr, self.width, self.height, True)
        self.assertIsNotNone(self.im2path)

    def test_created_file_exists(self):
        self.assertTrue(os.path.isfile("Nearest Neighbour.png"))

    def test_created_file_is_image(self):
        self.assertNotEqual(imghdr.what("Nearest Neighbour.png"), None)

    def test_resized_dimensions_correct(self):
        im2 = Image.open("Nearest Neighbour.png")
        self.width = 500
        self.height = 500
        newWidth, newHeight = im2.size
        self.assertEqual(self.height, newHeight)
        self.assertEqual(self.width, newWidth)


if __name__ == '__main__':
    unittest.main()
