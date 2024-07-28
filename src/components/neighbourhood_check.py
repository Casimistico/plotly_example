from dash import Dash, html, dcc
from dash.dependencies import Input, Output
from . import ids
import pandas as pd
from ..data.loader import DataSchema

def render(app: Dash,Data:pd.DataFrame) -> html.Div:
    neighbourhoods = sorted(Data.query(f'{DataSchema.ZONE}=="Montevideo"')[DataSchema.NEIGHBORHOOD].unique())    
    return  html.Div(
                    children = [
                    html.H2("Barrio",style={'horizontal-align':'middle',"margin-left": "40px",'text-align':'middle'}),
                     dcc.Checklist(
                id=ids.NEIGHBOURHOOD_CHECKLIST,
                options=[" " * 3 + neighbourhood for neighbourhood in neighbourhoods ], #Para agregar espacio antes del primer caracter
                labelStyle={"align-items": "center",'text-align':'middle'}
                
            ),
        ] 
    )