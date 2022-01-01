import dash
import numpy as np
import pandas as pd
import plotly.graph_objs as go
from dash import dcc, html
from flask import Flask

def figure_1():
    layout=go.Layout(title='Title',)
    fig=go.Figure(data=[go.Bar(go.Bar(y=[2, 1, 3]))],layout=layout)
    return fig

server = Flask(__name__)

app = dash.Dash(name =__name__, server=server)
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