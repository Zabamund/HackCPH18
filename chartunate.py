import pandas as pd
import altair as alt
#Only required for Jupyter_notebook chart display
alt.renderers.enable('notebook')


# read volume file and assign to vol data frame
volume_file = (r'D:\GeoHack2018\gitrepo\data\Hackaton\VolumeDistribution\Volumes')
vol = pd.read_csv(volume_file, delim_whitespace=True)

# For GRV vs GRV quantiles by HC Column charts
brush = alt.selection(type='interval')

points = alt.Chart(vol).mark_point().encode(
    x='Oil_GRV_10_6:Q',
    y='Oil_GRV_quantile:Q',
    color=alt.condition(brush, 'Hc_column__m_:Q', alt.value('darkgray'))).add_selection(brush)


bars = alt.Chart().mark_bar().encode(
    alt.Color('Hc_column__m_:Q', scale=alt.Scale(scheme='viridis')),
    y='Hc_column__m_:Q',
    x='Oil_GRV_10_6:Q'   
).transform_filter(brush)

GRVQHC=alt.vconcat(points, bars, data=vol)
GRVQHC.to_json()

# For GRV vs OWC_depth by HC column charts

brush = alt.selection(type='interval')

points = alt.Chart(vol).mark_point().encode(
    alt.X('Oil_GRV_10_6:Q'),
    alt.Y('OWC_depth:Q', scale=alt.Scale(zero=False)),
    color=alt.condition(brush, 'Oil_GRV_quantile:Q', alt.value('darkgray'))).add_selection(brush)


bars = alt.Chart().mark_bar().encode(
    alt.Color('Oil_GRV_quantile:Q', scale=alt.Scale(scheme='viridis')),
    y='Hc_column__m_:Q',
    x='Oil_GRV_10_6:Q'   
).transform_filter(brush)

GRVOWC=alt.vconcat(points, bars, data=vol)
GRVOWC.to_json()


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
GRVDNS.to_json()