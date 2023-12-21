import dash
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import dash_bootstrap_components as dbc


app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
    [
        dbc.NavbarSimple(
            children=[
                dbc.NavLink("首頁", href="/", active="exact"),
                dbc.NavLink("資料庫", href="/archive", active="exact"),
                dbc.NavLink("統計表", href="/analysis", active="exact"),
            ],
            brand="動畫觀看數統計_以巴哈姆特動畫瘋為例",
            color="success",
            dark=True,
            className='fixed-top'
        ),
        dash.page_container,
    ]
)

if __name__ == '__main__':
    app.run(debug=True)






























# import dash
# from dash import Dash, html, dash_table, dcc, callback, Output, Input
# import dash_bootstrap_components as dbc
# import plotly.express as px
# import pandas as pd

# df1 = pd.read_csv('./web_csv/Genre.csv')
# df2 = pd.read_csv('./web_csv/Genre_Only.csv')
# df3 = pd.read_csv('./web_csv/Tags.csv')
# df4 = pd.read_csv('./web_csv/Anime_Company.csv')


# app = Dash(__name__, title='動畫觀看數統計', external_stylesheets=[dbc.themes.BOOTSTRAP])

# app.layout = html.Div([
#     html.H1(children='影響觀看數因子', style={
#             'textAlign': 'center', 'margin-bottom': '1rem'}),
#     dcc.Dropdown(['作品分類(全部)', '作品分類(代表性)', '原創改編、新續作', '動畫公司'],
#                  '作品分類(全部)', id='dropdown-selection'),
#     dash_table.DataTable(style_table={
#                             'width': '100%',     # Set fixed width of the table
#                             'height': '350px',
#                             'overflowY': 'auto'
#                         },
#                         style_cell={
#                             'whiteSpace': 'normal',  # Allow text wrapping
#                             'textAlign': 'center'      # Align text to the left
#                         },
#                         style_header={
#                             'whiteSpace': 'normal',  # Allow header text wrapping
#                         },
#                          style_cell_conditional=[{'if': {'column_id': '動畫公司'}, 'width': '120px'}],
#                          sort_action='native',
#                          page_size=10,
#                          id='main_table'),
#     dcc.Graph(id='graph1'),
#     dcc.Graph(id='graph2'),
# ], className='container-lg')


# @callback(
#     [Output('main_table', 'data'), Output('main_table', 'columns'),
#     Output('graph1', 'figure'), Output('graph2', 'figure')],
#     Input('dropdown-selection', 'value')
# )
# def update_graph(value):
#     global df1, df2, df3, df4
#     if value == '作品分類(全部)':
#         data = df1.to_dict('records')
#         column = [{'id': column, 'name': column} for column in df1.columns]
#         fig1 = px.bar(df1, x='標籤', y=['全部作品數', '前25%作品數'], barmode='overlay')
#         fig1.update_layout(yaxis={'title': '作品數'})
#         fig2 = px.bar(df1, x='標籤', y=['最高(萬)', '中位數(萬)'], barmode='overlay')
#         fig2.update_layout(yaxis={'title': '平均觀看數(萬)'})
#         return data, column, fig1, fig2
#     if value == '作品分類(代表性)':
#         data = df2.to_dict('records')
#         column = [{'id': column, 'name': column} for column in df2.columns]
#         fig1 = px.bar(df2, x='標籤', y=['全部作品數', '前25%作品數'], barmode='overlay')
#         fig1.update_layout(yaxis={'title':'作品數'})
#         fig2 = px.bar(df2, x='標籤', y=['最高(萬)', '中位數(萬)'], barmode='overlay')
#         fig2.update_layout(yaxis={'title': '平均觀看數(萬)'})
#         return data, column, fig1, fig2
#     if value == '原創改編、新續作':
#         data = df3.to_dict('records')
#         column = [{'id': column, 'name': column} for column in df3.columns]
#         fig1 = px.bar(df3, x='標籤', y=['全部作品數', '前25%作品數'], barmode='overlay')
#         fig1.update_layout(yaxis={'title': '作品數'})
#         fig2 = px.bar(df3, x='標籤', y=['最高(萬)', '中位數(萬)'], barmode='overlay')
#         fig2.update_layout(yaxis={'title': '平均觀看數(萬)'})
#         return data, column, fig1, fig2
#     if value == '動畫公司':
#         data = df4.to_dict('records')
#         column = [{'id': column, 'name': column} for column in df4.columns]
#         fig1 = px.bar(df4[df4['全部作品數']>=3], x='動畫公司', y=['全部作品數', '前25%作品數'], barmode='overlay')
#         fig1.update_layout(yaxis={'title': '作品數'})
#         fig2 = px.bar(df4[df4['全部作品數'] >= 3], x='動畫公司', y=['最高(萬)', '中位數(萬)'], barmode='overlay')
#         fig2.update_layout(yaxis={'title': '平均觀看數(萬)'})
#         return data, column, fig1, fig2

# if __name__ == '__main__':
#     app.run(debug=True)
