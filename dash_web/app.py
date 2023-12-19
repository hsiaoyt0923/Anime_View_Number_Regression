from dash import Dash, html, dash_table, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

df1 = pd.read_csv('../csv/ratio_table.csv')
df2 = pd.read_csv('../csv/Tags_View_Number.csv')
df3 = pd.read_csv('../csv/Original_or_Adapted.csv')
df4 = pd.read_csv('../csv/New_or_Sequel.csv')

app = Dash(__name__, title='動畫觀看數統計', external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    html.H1(children='影響觀看數關鍵因子', style={'textAlign':'center'}),
    dcc.Dropdown(['人氣作品各標籤占比','各類型作品觀看數據','各原作載體觀看數據','新續作觀看數據'], '人氣作品各標籤占比', id='dropdown-selection'),
    dash_table.DataTable(data=df1.to_dict('records'), page_size=10, id='main_table'),
    dcc.Graph(id='graph-content'),
    
],className='container-lg')

@callback(
    [Output('main_table', 'data'),Output('graph-content', 'figure')],
    Input('dropdown-selection', 'value')
)
def csv_toggle(value):
    global df1, df2, df3, df4
    if value == '人氣作品各標籤占比':
        return df1.to_dict('records'), px.bar(df1, x='標籤', y=['全部', '前25%'], barmode="group")
    if value == '各類型作品觀看數據':
        return df2.to_dict('records'), px.bar(df2, x='標籤', y=['最高', '中位數'], barmode="group")
    if value == '各原作載體觀看數據':
        return df3.to_dict('records'), px.bar(df3, x='原作載體', y=['最高', '中位數'], barmode="group")
    if value == '新續作觀看數據':
        return df4.to_dict('records'), px.bar(df4, x='新續作', y=['最高', '中位數'], barmode="group")
if __name__ == '__main__':
    app.run(debug=True)