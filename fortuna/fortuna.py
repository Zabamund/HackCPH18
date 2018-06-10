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

        # hardcode geometry
        self.size_raster = (250,162)
        self.X_corner = 390885
        self.Y_corner = 7156947
        self.dx, self.dy, self.dz = 25, 25, 100
        self.top_model = 950
        self.bottom_model = 1050


        self.base_cube = None
        self.top_cube = None
        self.base_n = None
        self.top_n = None
        self.vol = None

        # Create empty xarray dataset
        self.ds = xr.Dataset()

        self.xx = None
        self.yy = None
        self.zz = None
        self.model = None

        self.base_mean = None
        self.base_std = None # ds['BASE'].std(dim='MODEL')

        self.top_mean = None #ds['TOP'].mean(dim='MODEL')
        self.top_std = None # ds['TOP'].std(dim='MODEL')


        ## Initial methods to load
        self.import_data()
        self.calc_xarray()
        self.calc_stat()




    ### Methods for initiating the object

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


    def calc_xarray (self):
        self.xx = np.linspace(self.X_corner, self.X_corner + self.size_raster[0] * self.dx, self.size_raster[0])
        self.yy = np.linspace(self.Y_corner, self.Y_corner + self.size_raster[1] * self.dy, self.size_raster[1])
        self.zz = np.linspace(self.top_model, self.bottom_model, self.dz)

        self.model = np.linspace(0, self.top_model, self.base_n)

        self.ds.coords['X'] = self.xx
        self.ds.coords['Y'] = self.yy
        self.ds.coords['Z'] = self.zz
        self.ds.coords['MODEL'] = self.model

        self.ds['BASE'] = (('X', 'Y', 'MODEL'), self.base_cube)
        self.ds['TOP'] = (('X', 'Y', 'MODEL'), self.top_cube)


    def calc_stat (self):
        self.base_mean = self.ds['BASE'].mean(dim='MODEL')
        self.base_std = self.ds['BASE'].std(dim='MODEL')

        self.top_mean = self.ds['TOP'].mean(dim='MODEL')
        self.top_std = self.ds['TOP'].std(dim='MODEL')



    ## Data Management methods

    def load_pickle(self, path):
        return np.load(path)


    ## Methods tocompute different uncertatinty cubes --> cubes to be displayed in the frontend

    def calc_lithology(self, iterations = 2):
        """
        Sample from both distributions and fill each z-stack accordingly
        """
        # create empty array
        cube = np.zeros((iter, self.size_raster[0], self.size_raster[1], zz.size), dtype='int8')

        for i in range(iter):
            for j in range(self.size_raster[0]):  # size_raster[0]
                for k in range(self.size_raster[1]):

                    # sample from top and base distributions for specific x,y position
                    top = np.random.normal(self.top_mean[j, k], self.top_std[j, k])
                    base = np.random.normal(self.base_mean[j, k], self.base_std[j, k])

                    # iterate over vertical z-stack
                    for l in range(zz.size):

                        if zz[l] <= top:
                            cube[i, j, k, l] = 1
                        elif zz[l] > base:
                            cube[i, j, k, l] = 3
                        elif ((zz[l] > top) and (l <= base)):
                            cube[i, j, k, l] = 2

        return cube


    ### Modifyed from GemPy!!!
    def calculate_probability_lithology(self, lith_blocks):
        """Blocks must be just the lith blocks!"""
        lith_id = np.unique(lith_blocks)
        # lith_count = np.zeros_like(lith_blocks[0:len(lith_id)])
        lith_count = np.zeros((len(np.unique(lith_blocks)), lith_blocks.shape[1]))
        for i, l_id in enumerate(lith_id):
            lith_count[i] = np.sum(lith_blocks == l_id, axis=0)
        lith_prob = lith_count / len(lith_blocks)
        return lith_prob


    ### Modyfied from GemPy!!!
    def calculate_information_entropy(self, lith_prob):
        """Calculates information entropy for the given probability array."""
        cube = np.zeros_like(lith_prob[0])
        for l in lith_prob:
            pm = np.ma.masked_equal(l, 0)  # mask where layer prob is 0
            cube -= (pm * np.ma.log2(pm)).filled(0)
        return cube



    ## Simple plotting methods

    def plot_entropy(self, cube, slice=10):
        plt.imshow(cube[slice, :, :].T, origin='upperleft', cmap='viridis')
        plt.show()