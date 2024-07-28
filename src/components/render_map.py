import pandas as pd
import numpy as np
import plotly.express as px
import json
import geopandas as gpd
from dash import Dash, dcc, html


def prepare_data_for_map(result):
    result['COEF'] = pd.Series(np.random.normal(2,0.5,result.shape[0]))
    result['PREDICCION'] = result['PRICE'] * result['COEF']

    result['OPORTUNIDAD']  = np.where(result['PRICE'] * 0.9 > result['PREDICCION']  ,'SI','NO')
    result.dropna(subset=['LATITUDE','LONGITUDE'],inplace=True)
    result.dropna(subset=['LATITUDE','LONGITUDE'],inplace=True)
    result['LONGITUDE'] = result['LONGITUDE'].str.replace(',','.')
    result['LONGITUDE'] = result['LONGITUDE'].astype('float')  
    result = result[(result['LONGITUDE']<-56)&(result['LONGITUDE']>-60)] 
    result['LATITUDE'] = result['LATITUDE'].str.replace(',','.')
    result['LATITUDE'] = result['LATITUDE'].astype('float')
    result = result[(result['LATITUDE']<-34)&(result['LATITUDE']>-35)]
    return result
    

def render(app,data):
    geo_data = prepare_data_for_map(data)


    barrios = ['Punta Carretas','La Blanqueada','Carrasco','Tres Cruces']
    mt = gpd.read_file("ine_barrios_mvd_nbi85.shp")
    mt = mt.to_crs("EPSG:4326")
    mt = mt[mt['nombbarr'].isin(barrios)]


    fig = px.scatter_mapbox(geo_data,lon='LONGITUDE',lat='LATITUDE',color='OPORTUNIDAD',hover_data='PRICE')
    
    fig.update_layout(
        mapbox={
            "style": "open-street-map",
            "zoom": 5,
            "layers": [
                {
                    "source": json.loads(mt.geometry.to_json()),
                    "below": "traces",
                    "type": "line",
                    "color": "purple",
                   "line": {"width": 8},
                }
            ],
        },
        margin={"l": 0, "r": 0, "t": 0, "b": 0},
    )

    return  html.Div(dcc.Graph(figure=fig)
                     )
