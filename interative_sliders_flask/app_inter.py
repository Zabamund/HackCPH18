from flask import Flask, request, render_template, jsonify
import numpy as np
import matplotlib.pyplot as plt
import requests
from bokeh.embed import components
import pandas as pd
import holoviews as hv

app = Flask(__name__)

@app.route('/section')
def section():
    top_cloud = np.load('data/graham.pkl.npy')

    ds = hv.Dataset((np.arange(0,100,1), np.linspace(0., 162., 162), np.linspace(0., 250., 250),
                top_cloud),
                kdims=['depth', 'y', 'x'],
                vdims=['z'])
    
    renderer = hv.renderer('bokeh')

    plot1 = (ds.to(hv.Image, ['x', 'depth']).redim(z=dict(range=(0,0.05))).options(height=400, width=700, colorbar=True, invert_yaxis=True, cmap='viridis'))
    
    html1 = renderer.html(plot1)
     
    return render_template("inter.html", html1=html1)


@app.route('/map')
def map():
    top_cloud = np.load('data/graham.pkl.npy')

    ds1 = hv.Dataset((np.arange(0,100,1), np.linspace(0., 162., 162), np.linspace(0., 250., 250),
                top_cloud),
                kdims=['depth', 'y', 'x'],
                vdims=['z'])
    
    ds2 = hv.Dataset((np.arange(0,100,1), np.linspace(0., 162., 162), np.linspace(0., 250., 250),
                top_cloud),
                kdims=['depth', 'y', 'x'],
                vdims=['z'])
    
    renderer = hv.renderer('bokeh')

    plot1 = (ds1.to(hv.Image, ['x', 'depth']).redim(z=dict(range=(0,0.05))).options(height=400, width=700, colorbar=True, invert_yaxis=True, cmap='viridis'))
    
    html1 = renderer.html(plot1)
    
    
    plot2 = ds2.to(hv.Image, ['x', 'y']).redim(z=dict(range=(0,0.05))).options(height=400, width=700, colorbar=True, invert_yaxis=True, cmap='viridis')
    
    html2 = renderer.html(plot2)
     
    return render_template("inter.html", html1=html1, html2=html2)


if __name__ == '__main__':
    app.run()