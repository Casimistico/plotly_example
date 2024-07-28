import pandas as pd
import sqlite3
import os
import plotly.express as px
from matplotlib import pyplot as plt

from pandas import read_csv
from sklearn.model_selection import train_test_split
#from sklearn.linear_model import LinearRegression
from sklearn.neighbors import LocalOutlierFactor
#from sklearn.metrics import mean_absolute_error



class DataSchema:
    TITLE = 'TITLE'
    BEDROOMS = 'BEDROOMS'
    FULL_BATHROOMS =  'FULL_BATHROOMS'
    NEIGHBORHOOD  = 'NEIGHBORHOOD'
    BUILDING_TYPE = 'BUILDING_TYPE'
    PRICE =  'PRICE'
    CURRENCY_ID = 'CURRENCY_ID'
    COVERED_AREA = 'COVERED_AREA'
    TOTAL_AREA = 'TOTAL_AREA'
    ITEM_CONDITION = 'ITEM_CONDITION'
    LINK = 'LINK'
    PATIO = 'PATIO' 
    GARAGES = 'GARAGES'
    SOURCE = 'SOURCE'
    DATE = 'DATE'
    MONTH = 'MONTH'
    DAY = 'DAY'
    YEAR = 'YEAR'
    ZONE = 'ZONE'
    LATITUDE = 'LATITUDE'
    LONGITUDE = 'LONGITUDE'

MT_NEIGHBORHOOD =['Punta Carretas', 'La Blanqueada', 'Carrasco', 'Tres Cruces']

def get_data():
    RESULT_DATASET_COLUMNS = [
                DataSchema.BEDROOMS,
                DataSchema.FULL_BATHROOMS,
                DataSchema.NEIGHBORHOOD,
                DataSchema.BUILDING_TYPE,
                DataSchema.PRICE,
                DataSchema.CURRENCY_ID,
                DataSchema.COVERED_AREA,
                DataSchema.TOTAL_AREA,
                DataSchema.ITEM_CONDITION,
                DataSchema.PATIO,
                DataSchema.GARAGES,
                DataSchema.SOURCE,
                DataSchema.DATE,
                DataSchema.MONTH,
                DataSchema.DAY,
                DataSchema.YEAR,
                DataSchema.ZONE,
                DataSchema.LATITUDE,
                DataSchema.LONGITUDE,

                ]
    
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'info_inmo.csv')
    result = pd.read_csv(filename,sep=";",low_memory=False)
    return result
if __name__ == '__main__':
    print("Este script se encarga de cargar los datos")
    print(get_data().columns)