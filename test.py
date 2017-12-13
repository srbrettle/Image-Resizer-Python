import unittest
import os.path
import imghdr
from PIL import Image
import imageManipulation


class TestMethods(unittest.TestCase):

    def setUp(self):
        global filepath
        filepath = "C:\\test.png"

    def test_file_exists(self):
        self.assertTrue(os.path.isfile(filepath))

    def test_file_is_image(self):
        self.assertNotEqual(imghdr.what(filepath), None)

    def test_resized_dimensions_correct(self):
        im = Image.open(filepath)
        width = 500
        height = 500
        im2path = imageManipulation.resizeImage(im, width, height, True)
        im2 = Image.open(im2path)
        newWidth, newHeight = im2.size
        self.assertEqual(height, newHeight)
        self.assertEqual(width, newWidth)


if __name__ == '__main__':
    unittest.main()
