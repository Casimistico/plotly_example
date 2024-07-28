from dash import Dash, dcc, html
import plotly.express as px
from . import ids
from dash.dependencies import Input, Output
import pandas as pd
from ..data.loader import DataSchema


def render(app: Dash, data:pd.DataFrame) -> html.Div:
    @app.callback(
        Output(ids.PRICE_EVOLUTION,'children'),
        Input(ids.NEIGHBOURHOOD_CHECKLIST,'value'),
        Input(ids.TYPE_BUILDING_DROPDOWN,'value')
    )
    def update_price_evolution(neighbourhood: list[str], building_type: list[str]) -> html.Div:
        if neighbourhood:
            neighbourhood = [x.strip() for x in neighbourhood] # Le quito los espacios adelante del nombre (espacios agregados por diseño, no es la forma óptima de hacerlo)
        if not neighbourhood:
           fig = px.line()
        else:
            filtered_price_data = data.query("NEIGHBORHOOD in @neighbourhood and BUILDING_TYPE in @building_type")  ###Con arroba hago query sobre la lista
               
            filtered_price_data.DATE = pd.to_datetime(filtered_price_data.DATE,format='%d/%m/%Y')
            per = filtered_price_data.DATE.dt.to_period("M")
            
            g = filtered_price_data.groupby(by=[per,DataSchema.NEIGHBORHOOD]).agg({'PRICE':'mean'}).reset_index()
            g['DATE'] = g['DATE'].dt.to_timestamp() 
            title = f'Precios de {building_type}s'

            fig = px.line(g, x="DATE", y="PRICE",color=DataSchema.NEIGHBORHOOD,
            title=title,
            labels={"DATE": "Mes",
                    "PRICE":"Precio (U$S)",
                    DataSchema.NEIGHBORHOOD:"Barrio"}
            )

            fig.update_layout(
                title={
                    'y':0.9,
                    'x':0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'})
        
        return html.Div(dcc.Graph(figure=fig),id=ids.PRICE_EVOLUTION)
    return html.Div(id=ids.PRICE_EVOLUTION)