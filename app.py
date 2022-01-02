import dash
import numpy as np
import pandas as pd
from dash import dcc, html
import plotly.express as px

df = px.data.iris()
# Create the chart:
fig = px.parallel_coordinates(
    df, 
    color="species_id", 
    labels={"species_id": "Species","sepal_width": "Sepal Width", "sepal_length": "Sepal Length", "petal_width": "Petal Width", "petal_length": "Petal Length", },
    color_continuous_scale=px.colors.diverging.Tealrose,
    color_continuous_midpoint=2)

# Hide the color scale that is useless in this case

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div(children=[
    html.H1(children='Demo of Iris Dataset',
            style={'textAlign': 'center'}
    ),

    html.Div(children='''
        This is a dash + plotly + python on Heroku cloud platform demo.
    '''),
    dcc.Graph(figure = fig, id = 'scatter')
])


if __name__ == '__main__':
    app.run_server(debug=True)