import dash
from dash import html, dash_table, dcc, callback, Output, Input

import plotly.express as px
import pandas as pd

dash.register_page(__name__)

df1 = pd.read_csv('./web_csv/genre_table.csv')
df2 = pd.read_csv('./web_csv/Tags_View_Number.csv')
df3 = pd.read_csv('./web_csv/Anime_Company.csv')
df4 = pd.read_csv('./web_csv/genre2_table.csv')



layout = html.Div([
    html.H1(children='影響觀看數因子', style={'textAlign':'center'}),
    dcc.Dropdown(['作品分類(全部)','作品分類(代表性)','動畫公司','原創改編、新續作'], '作品分類(全部)', id='dropdown-selection'),
    dash_table.DataTable(data=df1.to_dict('records'), page_size=10, id='main_table'),
    dcc.Graph(id='graph-content'),
    
],className='container-lg')

@callback(
    [Output('main_table', 'data')],
    Input('dropdown-selection', 'value')
)
def csv_toggle(value):
    global df1, df2, df3
    if value == '作品分類(全部)':
        return df1.to_dict('records'), 
    if value == '作品分類(代表性)':
        return df2.to_dict('records'), 
    if value == '動畫公司':
        return df3.to_dict('records'),
    if value == '原創改編、新續作':
        return df4.to_dict('records'),