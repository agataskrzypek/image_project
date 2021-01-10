from __future__ import print_function
from pynput.mouse import Listener
import numpy as np
import matplotlib.pyplot as plt


class IndexTracker(object):
    def __init__(self, ax, X, hist_ind):
        self.ax = ax
        ax.set_title('use scroll wheel to navigate images')

        self.X = X
        # rows, cols, self.slices = X.shape
        self.slices = int(len(X))
        self.ind = self.slices//2
        self.hist_ind = hist_ind
        if self.hist_ind:
            # self.im = ax.hist(self.X[:, :, self.ind])
            self.im = ax.hist(self.X[self.ind][:], histtype='step')
            self.update_hist()
        else:
            self.im = ax.imshow(self.X[self.ind][:])
            self.update()

    def onscroll(self, event):
        print("%s %s" % (event.button, event.step))
        if event.button == 'up':
            self.ind = (self.ind + 1) % self.slices
        else:
            self.ind = (self.ind - 1) % self.slices
        if self.hist_ind:
            self.update_hist()
        else:
            self.update()


    def onscroll_hist(self, event, index):
        self.ind = index
        self.update()

    def update(self):
        # self.im.set_data(self.X[:, :, self.ind])
        self.im.set_data(self.X[self.ind][:])
        self.ax.set_ylabel('slice %s' % self.ind)
        self.im.axes.figure.canvas.draw()

        self.ax.imshow(self.X[self.ind][:])


    def update_hist(self):
        self.ax.hist(self.X[self.ind][:], histtype='step')

class ImagePlot:
    def __init__(self, img_obj):
        self.img = img_obj

    def plot_3d_img(self):
        """
        Function shows 3d images: 2d layers with scrolling option
        """

        # fig, ax = plt.subplots(1, 1)
        # self.img_data = self.img.get_fdata()
        # tracker = IndexTracker(ax, self.img_data)
        # fig.canvas.mpl_connect('scroll_event', tracker.onscroll)


        fig, (ax1, ax2) = plt.subplots(2, 1)
        # self.img_data = self.img.get_fdata()
        self.img_data = self.img
        tracker = IndexTracker(ax1, self.img_data, False)
        tracker_2 = IndexTracker(ax2, self.img_data, True)
        fig.canvas.mpl_connect('scroll_event', tracker.onscroll)
        fig.canvas.mpl_connect('scroll_event', tracker_2.onscroll)


        plt.show()
        pass

        # print('Type Y to analyze current layer \n To stop analysing put 0 ...')
        # img_input = input()
        #
        #
        # while img_input.lower() == 'y':
        #     plt.show()
        #     print('ffff')
        #     plt.hist(self.img_data[:,:, tracker.ind], density=True, bins='auto')
        #     plt.grid(axis='y', alpha=0.75)
        #     plt.xlabel('Pixel value')
        #     plt.ylabel('Frequency')
        #     plt.title('My Very Own Histogram')
        #     plt.show()
        #     print('Type Y to analyze current layer \n To stop analysing put 0 ...')
        #     img_input = input()




    def main(self):
        self.plot_3d_img()


