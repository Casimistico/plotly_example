import plotly.express as px
import plotly.graph_objects as go
import geopandas as gpd
import numpy as np

from dash import Dash, html,  callback, dcc, Input, Output
from . import neighbourhood_check, price_evolution, type_building_dropdown,render_map
import pandas as pd


def create_layout(app:Dash, data:pd.DataFrame) -> html.Div:
    app.layout = html.Div([
        html.Hr(), ### Espacios
        html.H1(app.title), ### Tìtulo
        html.Hr(), 
    dcc.Tabs([
        dcc.Tab(label='Evolución de precios', children=[ html.Hr(),
           create_layout_evolution(app,data)
        ],
        className='custom-tabs',
        selected_className='custom-tab--selected',
        ),
        dcc.Tab(label='Oportunidades', children=[render_map.render(app,data)
       ], 
       className='custom-tabs',
       selected_className='custom-tab--selected'),
])
])

    return app.layout


def create_layout_evolution(app:Dash, data:pd.DataFrame) -> html.Div:
    return html.Div(
        className='app-div',
        children = [
            html.Div(children=[
            html.Div(
                className="dropdown-container",
                children = neighbourhood_check.render(app,data),
                style={"margin-left": "15px",
                       "margin-right": "20px",
                       "margin-top": "50px"}
            ),
            html.Div(
                className="type_building",
                children = type_building_dropdown.render(app,data),
                style={"margin-left": "15px",
                       "margin-top": "15px"}
            )
            ]),
            html.Div(
                    className='price-evolution-graph',
                    children = price_evolution.render(app,data),
                    style={
                        "margin-left": "40px",
                           "flex": "1"
                                  }
                    
            )
        ], style={'display':'flex'}
    )