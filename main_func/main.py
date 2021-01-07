"""
author: A Skrzypek
"""

from image_reader import ImageReader
from make_plots import ImagePlot
import numpy as np

if __name__ == "__main__":

    # read images from path
    path_to_test_sample = r"C:\Users\user\Documents\IMAGE_PROJECT\sample_database\jpg_samples"
    sample_image_obj = ImageReader(path_to_test_sample)
    sample_image_obj.main()

    sample_plot_obj = ImagePlot(sample_image_obj.images_storage)
    sample_plot_obj.main()




    pass

