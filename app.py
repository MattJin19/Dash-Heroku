import dash
import numpy as np
import pandas as pd
import plotly.graph_objs as go
from dash import dcc, html


def figure_1():
    layout=go.Layout(title='Title',)
    fig=go.Figure(data=[go.Bar(go.Bar(y=[2, 1, 3]))],layout=layout)
    return fig

app = dash.Dash(__name__)
server = app.server
app.layout = html.Div(children=[
    html.H1(children='Demo',
            style={'textAlign': 'center'}
    ),

    html.Div(children='''
        Demo testing cloud app
    '''),

    dcc.Graph(
        id='total-indus',
        figure=figure_1()
    ),
])