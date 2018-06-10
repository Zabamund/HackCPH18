"""
Fortuna

Python project to visualize uncertatinty.

Created on 09/06/2018

@authors: Natalia Shchukina, Graham Brew, Marco van Veen, Behrooz Bashokooh, Tobias Stål, Robert Leckenby
"""

# Import libraries

import numpy as np
import glob
from matplotlib import pyplot as plt
import pandas as pd
import xarray as xr
import pyproj as proj
from scipy.stats import norm



class Fortuna(object):
    """
    Class to load the fortuna dataset and call different methods for visualization in a web frontend.

    Args:
        There are no required arguments at the moment. Input files could be defined.
    """



    def __init__(self, **kwargs):
        """
        Method that is called when a object of the class Fortuna is initiated, it imports the data and directly creates some important variables.
        """

        self.size_raster = (250,162)
        self.base_cube = None
        self.top_cube = None
        self.base_n = None
        self.top_n = None
        self.vol = None





        ds = xr.Dataset()

        self.X_corner = 390885
        self.Y_corner = 7156947
        self.dx, self.dy self.dz= 25, 25, 100
        self.top_model = 950
        self.bottom_model = 1050

        xx = np.linspace(X_corner, X_corner + size_raster[0] * dx, size_raster[0])
        yy = np.linspace(Y_corner, Y_corner + size_raster[1] * dy, size_raster[1])
        zz = np.linspace(top_model, bottom_model, dz)

        model = np.linspace(0, top_model, base_n)

        ds.coords['X'] = xx
        ds.coords['Y'] = yy
        ds.coords['Z'] = zz
        ds.coords['MODEL'] = model

        ds['BASE'] = (('X', 'Y', 'MODEL'), base_cube)
        ds['TOP'] = (('X', 'Y', 'MODEL'), top_cube)









        # Initial methods to load
        self.import_data()


    def folder2cube(self, files):
        """
        Method to read a file.
        """
        base_set = glob.glob(files)
        cube = np.zeros(self.size_raster + (len(base_set),))
        for i, model in enumerate(base_set):
            cube[:, :, i] = np.loadtxt(model, skiprows=1).reshape(self.size_raster)
        return cube, len(base_set)


    def import_data(self):
        """
        Method to load different data objects from files.
        """
        self.base_cube, self.base_n = self.folder2cube('data/Hackaton/BaseSet/MapSimu__*.data')
        self.top_cube, self.top_n = self.folder2cube('data/Hackaton/TopSet/MapSimu__*.data')

        self.vol = pd.read_csv('data/Hackaton/VolumeDistribution/Volumes', delim_whitespace=True)


    def load_pickle(self, path):
        return np.load(path)

    def plot_entropy(self, cube, slice=10):
        plt.imshow(cube[slice, :, :].T, origin='upperleft', cmap='viridis')
        plt.show()


    def calc_lithology(self, iterations = 2):
        """
        Sample from both distributions and fill each z-stack accordingly
        """
        # create empty array
        cube = np.zeros((iter, self.size_raster[0], self.size_raster[1], zz.size), dtype='int8')"

        for i in range(iter):
            for j in range(size_raster[0]):  # size_raster[0]
                for k in range(size_raster[1]):

                    # sample from top and base distributions for specific x,y position
                    top = np.random.normal(top_mean[j, k], top_std[j, k])
                    base = np.random.normal(base_mean[j, k], base_std[j, k])

                    # iterate over vertical z-stack
                    for l in range(zz.size):

                        if zz[l] <= top:
                            lith_block[i, j, k, l] = 1
                        elif zz[l] > base:
                            lith_block[i, j, k, l] = 3
                        elif ((zz[l] > top) and (l <= base)):
                            lith_block[i, j, k, l] = 2
