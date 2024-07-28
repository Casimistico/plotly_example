from dash import Dash, html, dcc
from dash.dependencies import Input, Output
from . import ids
import pandas as pd
from ..data.loader import DataSchema

def render(app: Dash,Data:pd.DataFrame) -> html.Div:
    neighbourhoods = sorted(Data.query(f'{DataSchema.ZONE}=="Montevideo"')[DataSchema.NEIGHBORHOOD].unique())    

    return   html.Div(
                    children = [
                    html.H6("Negocio"),
                    dcc.Dropdown(options=[{'label':'Casa', 'value':'Casa'},
                                          {'label':'Apartamento', 'value':'Apartamento'}
                                        ], 
                                id=ids.TYPE_BUILDING_DROPDOWN,
                                multi=False,
                                value='Casa',
                                placeholder='Selecciona si Casa o Apartamento',
                                style={'horizontal-align': ' middle',"height": "500%",
                                       "width": "100%","margin-top": "15px","textAlign": "left"}),
                    ])