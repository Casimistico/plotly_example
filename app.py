import pandas as pd
import numpy as np
import sqlite3
from dash import Dash, dcc, html
from src.components.layout import create_layout
from dash_bootstrap_components.themes import BOOTSTRAP
from src.data import loader

def main():
    data =  loader.get_data()
    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = 'Análisis de datos del mercado inmobiliario montevideano'
    app.layout = create_layout(app,data)
    app.run(debug=True)


if __name__ == "__main__":
    main()