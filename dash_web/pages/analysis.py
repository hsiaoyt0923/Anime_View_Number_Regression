import dash
from dash import html, dash_table, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

dash.register_page(__name__,  title='動畫觀看數統計')

df1 = pd.read_csv('./web_csv/Genre.csv')
df2 = pd.read_csv('./web_csv/Genre_Only.csv')
df3 = pd.read_csv('./web_csv/Tags.csv')
df4 = pd.read_csv('./web_csv/Anime_Company.csv')

layout = html.Div([
    html.H1(children='關鍵因子', style={
                                    'textAlign': 'center',
                                    'margin-bottom': '1rem'
                                    }),
    dcc.Dropdown(['作品分類(全部)', '作品分類(代表性)', '原創改編、新續作', '動畫公司'],
                 '作品分類(全部)',
                 id='dropdown-selection',
                 ),
    dash_table.DataTable(style_table={
                            'width': '100%',     
                            'height': '350px',
                            'overflowY': 'auto'
                        },
                        style_cell={
                            'whiteSpace': 'normal',  # 允許表格內容變多行
                            'textAlign': 'center'
                        },
                        style_header={
                            'whiteSpace': 'normal',  # 允許表頭內容變多行
                        },
                        style_cell_conditional=[
                            {'if': {'column_id': '動畫公司'}, 'width': '120px'}
                            ],
                        sort_action='native',
                        page_size=10,
                        id='main_table'),
    dcc.Graph(style={'height': '800px'},
              id='graph1'),
    dcc.Graph(style={'height': '800px'},
              id='graph2'),
    html.Div([
        dcc.Graph(id='graph3'),
        ],
        id='pie'),
    ],
    className='container-lg pt-2')


@callback(
    [Output('main_table', 'data'), Output('main_table', 'columns'),
     Output('graph1', 'figure'), Output('graph2', 'figure'), Output('pie', 'style'), Output('graph3', 'figure')],
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    global df1, df2, df3, df4
    if value == '作品分類(全部)':
        data = df1.to_dict('records')
        column = [{'id': column, 'name': column} for column in df1.columns]
        fig1 = px.bar(df1, x=['全部作品數','前25%作品數'], y='標籤', orientation='h', barmode='overlay')
        fig1.update_layout(xaxis={'title': '作品數'})
        fig2 = px.bar(df1, x=['最高(萬)','中位數(萬)'], y='標籤', orientation='h', barmode='overlay')
        fig2.update_layout(xaxis={'title': '平均觀看數(萬)'})
        style = {'display':'None'}
        return data, column, fig1, fig2, style, None
    if value == '作品分類(代表性)':
        data = df2.to_dict('records')
        column = [{'id': column, 'name': column} for column in df2.columns]
        fig1 = px.bar(df2, x=['全部作品數','前25%作品數'], y='標籤', orientation='h', barmode='overlay')
        fig1.update_layout(xaxis={'title': '作品數'})
        fig2 = px.bar(df2, x=['最高(萬)','中位數(萬)'], y='標籤', orientation='h', barmode='overlay')
        fig2.update_layout(xaxis={'title': '平均觀看數(萬)'})
        style = {'display':'block'}
        fig3 = px.pie(df2, values='占全部作品比例(%)', names='標籤', title='各標籤作品占比')
        print(fig3)
        return data, column, fig1, fig2, style, fig3
    if value == '原創改編、新續作':
        data = df3.to_dict('records')
        column = [{'id': column, 'name': column} for column in df3.columns]
        fig1 = px.bar(df3, x=['全部作品數','前25%作品數'], y='標籤', orientation='h', barmode='overlay')
        fig1.update_layout(xaxis={'title': '作品數'})
        fig2 = px.bar(df3, x=['最高(萬)','中位數(萬)'], y='標籤', orientation='h', barmode='overlay')
        fig2.update_layout(xaxis={'title': '平均觀看數(萬)'})
        style = {'display':'block'}
        return data, column, fig1, fig2, style, None
    if value == '動畫公司':
        data = df4.to_dict('records')
        column = [{'id': column, 'name': column} for column in df4.columns]
        fig1 = px.bar(df4[(df4.全部作品數 >= 3) & (df4['前25%作品數'] > 0)], x=['全部作品數', '前25%作品數'], y='動畫公司', orientation='h', barmode='overlay')
        fig1.update_layout(xaxis={'title': '作品數'})
        fig2 = px.bar(df4[(df4.全部作品數 >= 3) & (df4['前25%作品數'] > 0)], x=['最高(萬)', '中位數(萬)'], y='動畫公司', orientation='h', barmode='overlay')
        fig2.update_layout(xaxis={'title': '平均觀看數(萬)'})
        style = {'display':'None'}
        return data, column, fig1, fig2, style, None
    