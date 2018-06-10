from flask import Flask, request, render_template, jsonify
import numpy as np
import matplotlib.pyplot as plt
import requests
from bokeh.embed import components
import pandas as pd
import holoviews as hv

app = Flask(__name__)

@app.route('/map')
def map():
    # Read in the pickles 
    mid_unit = np.load('data/mid_unit.npy')
    all_surfaces = np.load('data/realisation_1_10.npy')
    
    # Pick one scenario
    nb = 3
    scenario = all_surfaces[:,:,:,nb]

    # Inject the surfaces into the mid_unit
    combined = mid_unit
    mid_unit[scenario==1] = np.nan
    
    # Make the Holoviews DataSpaces
    ds1 = hv.Dataset((np.arange(0,100,1), np.linspace(0., 162., 162), np.linspace(0., 250., 250),
                combined),
                kdims=['depth', 'y', 'x'],
                vdims=['z'])
       
    renderer = hv.renderer('bokeh')

    # Plot
    plot1 = ds1.to(hv.Image, ['x', 'depth']).redim(z=dict(range=(0,1))).options(height=400, width=700, colorbar=True, invert_yaxis=True, cmap='viridis')
    
    html1 = renderer.html(plot1)
    
    
    plot2 = ds1.to(hv.Image, ['x', 'y']).redim(z=dict(range=(0,1))).options(height=400, width=700, colorbar=True, invert_yaxis=True, cmap='viridis')
    
    html2 = renderer.html(plot2)
     
    return render_template("inter.html", html1=html1, html2=html2)


if __name__ == '__main__':
    app.run()