# imports
from flask import Flask, render_template, request
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import altair as alt
import sys, os

# use specified path
sys.path.append("../../")
import fortuna.fortuna as ft

app = Flask(__name__)

#routes

@app.route('/')
def home():

    ### BEHROOZ
    # read volume file and assign to vol data frame
    volume_file = ('static/Volumes')
    vol = pd.read_csv(volume_file, delim_whitespace=True)

    # GRVQHC
    # For GRV vs GRV quantiles by HC Column charts
    brush = alt.selection(type='interval')

    points = alt.Chart(vol).mark_point().encode(
        x='Oil_GRV_10_6:Q',
        y='Oil_GRV_quantile:Q', tooltip=['Num', 'Oil_GRV_quantile'],
        color=alt.condition(brush, 'Hc_column__m_:Q', alt.value('darkgray'))).add_selection(brush)


    bars = alt.Chart().mark_bar().encode(
        alt.Color('Hc_column__m_:Q', scale=alt.Scale(scheme='viridis')),
        y='Hc_column__m_:Q',
        x='Oil_GRV_10_6:Q'   
    ).transform_filter(brush)

    GRVQHC=alt.vconcat(points, bars, data=vol)
    GRVQHC = GRVQHC.to_json()

    # GRVOWC
    brush = alt.selection(type='interval')

    points = alt.Chart(vol).mark_point().encode(
        alt.X('Oil_GRV_10_6:Q'),
        alt.Y('OWC_depth:Q', scale=alt.Scale(zero=False)), tooltip=['Num', 'Oil_GRV_quantile'],
        color=alt.condition(brush, 'Oil_GRV_quantile:Q', alt.value('darkgray'))).add_selection(brush)


    bars = alt.Chart().mark_bar().encode(
        alt.Color('Oil_GRV_quantile:Q', scale=alt.Scale(scheme='viridis')),
        y='Hc_column__m_:Q',
        x='Oil_GRV_10_6:Q'   
    ).transform_filter(brush)

    GRVOWC=alt.vconcat(points, bars, data=vol)
    GRVOWC = GRVOWC.to_json()

    # GRVDNS
    # For the histogram of GRV density with Min,Mean,Max HC column indicators

    brush = alt.selection(type='interval', encodings=['x'])

    bars = alt.Chart(vol).mark_bar().encode(
        
        alt.X("GRV_density__m_:Q", bin=alt.Bin(maxbins=20)),
        alt.Y('count()', axis=alt.Axis(title='Min,Mean,Max HC')),
        opacity=alt.condition(brush, alt.OpacityValue(1), alt.OpacityValue(0.7))
    ).add_selection(
        brush).properties(width=600, height=400)

    line1 = alt.Chart(vol).mark_rule(color='firebrick').encode(
        y='max(Hc_column__m_):Q',
        size=alt.SizeValue(2)
    ).transform_filter(
        brush
    )

    line2 = alt.Chart(vol).mark_rule(color='yellow').encode(
        y='min(Hc_column__m_):Q',
        size=alt.SizeValue(2)
    ).transform_filter(
        brush
    )

    line3 = alt.Chart(vol).mark_rule(color='green').encode(
        y='mean(Hc_column__m_):Q',
        size=alt.SizeValue(2)
    ).transform_filter(
        brush
    )

    GRVDNS=alt.layer(bars, line1, line2,line3, data=vol)
    GRVDNS = GRVDNS.to_json()

    return render_template('index.html', GRVQHC = GRVQHC, GRVOWC = GRVOWC, GRVDNS = GRVDNS)

    ### MARCO


@app.route('/slider', methods = ['GET'])
def slider():
    if request.method == 'GET':
        slider_value = request.args.get('arg1')
        print('slider_value', slider_value)
        return slider_value

# run
if __name__ == '__main__':
    app.run(port=5002, debug=True)