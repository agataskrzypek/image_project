import os
import nibabel as nib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import mahotas

class ImageReader:
    def __init__(self, path_to_images):
        self.path_to_images = path_to_images
        self.__image_format = 'jpg'

    @property
    def image_format(self):
        """
        Decorator enables to obtain image_format value outside the class body
        """
        print("Retrieving image format...")
        return self.__image_format

    @image_format.setter
    def image_format(self, value):
        """
        Decorator enables to change image_format values outside the class body
        """
        if type(value) is not str:
            raise TypeError("Format must be a string")
        print("Setting image format as {}...".format(value))
        self.__image_format = value

    def list_dir(self):
        """
        Function return all paths of files with self.__image_format extension
        :return: list of paths saved in self.image_dirs
        """
        self.image_dirs = []
        for file in os.listdir(self.path_to_images):
            if file.endswith(self.__image_format):
                self.image_dirs.append(os.path.join(self.path_to_images, file))


    def read_images(self):
        "Function reads images taken from list of paths and append to dictionary"
        self.images_dict = {}
        self.images_storage = []
        for image_id, image_path in enumerate(self.image_dirs):
            # img_temp = nib.load(image_path)
            img_temp = mahotas.imread(image_path, as_grey=True)
            # self.images_dict[image_id] = img_temp
            self.images_storage.append(img_temp)

    def main(self):
        """
        Function performs all steps needed to obtain dictionary with images
        """
        self.list_dir()
        self.read_images()



