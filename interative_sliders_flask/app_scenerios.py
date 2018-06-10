from flask import Flask, request, render_template, jsonify
import numpy as np
import matplotlib.pyplot as plt
import requests
from bokeh.embed import components
import pandas as pd
import holoviews as hv

app = Flask(__name__)

@app.route('/map1')
def map1():
    # Read in the pickles 
    mid_unit = np.load('data/mid_unit.npy')
    all_surfaces = np.load('data/realisation_all.npy')
    

    
    slider_value=1
    
    # Make the Holoviews DataSpaces
    ds1 = hv.Dataset((np.arange(0,100,1), np.linspace(0., 162., 162), np.linspace(0., 250., 250), 
            (np.where((all_surfaces[:,:,:,slider_value]==1), np.nan, mid_unit))),
            kdims=['depth', 'y', 'x'],
            vdims=['z'])
       
    renderer = hv.renderer('bokeh')

    # Plot
    plot1 = ds1.to(hv.Image, ['x', 'depth']).redim(z=dict(range=(0,1))).options(height=400, width=700, colorbar=True, invert_yaxis=True, cmap='viridis')
    
    html1 = renderer.html(plot1)
    
    
    plot2 = ds1.to(hv.Image, ['x', 'y']).redim(z=dict(range=(0,1))).options(height=400, width=700, colorbar=True, invert_yaxis=True, cmap='viridis')
    
    html2 = renderer.html(plot2)
     
    return render_template("inter.html", html1=html1, html2=html2)

@app.route('/map2')    
def map2():
                      
    # Read in the pickles 
    mid_unit = np.load('data/mid_unit.npy')
    all_surfaces = np.load('data/realisation_all.npy')
    
    slider_value=2
    
    # Make the Holoviews DataSpaces
    ds1 = hv.Dataset((np.arange(0,100,1), np.linspace(0., 162., 162), np.linspace(0., 250., 250), 
            (np.where((all_surfaces[:,:,:,slider_value]==1), np.nan, mid_unit))),
            kdims=['depth', 'y', 'x'],
            vdims=['z'])
       
    renderer = hv.renderer('bokeh')

    # Plot
    plot1 = ds1.to(hv.Image, ['x', 'depth']).redim(z=dict(range=(0,1))).options(height=400, width=700, colorbar=True, invert_yaxis=True, cmap='viridis')
    
    html1 = renderer.html(plot1)
    
    
    plot2 = ds1.to(hv.Image, ['x', 'y']).redim(z=dict(range=(0,1))).options(height=400, width=700, colorbar=True, invert_yaxis=True, cmap='viridis')
    
    html2 = renderer.html(plot2)
     
    return render_template("inter.html", html1=html1, html2=html2)
    
@app.route('/map3')    
def map3():
                      
    # Read in the pickles 
    mid_unit = np.load('data/entropy_final.npy')
    all_surfaces = np.load('data/realisation_all.npy')
    
    slider_value=2
    
    # Make the Holoviews DataSpaces
    ds1 = hv.Dataset((np.arange(0,100,1), np.linspace(0., 162., 162), np.linspace(0., 250., 250), 
            (np.where((all_surfaces[:,:,:,slider_value]==1), np.nan, mid_unit))),
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