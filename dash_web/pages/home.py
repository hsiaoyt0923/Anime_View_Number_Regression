import dash
from dash import html


dash.register_page(__name__,
                   title='動畫觀看數統計',
                   path='/')

layout = html.Div(
        [html.Div([
            html.Div([
                html.H1('動畫觀看數統計'),
                html.H2('以巴哈姆特動畫瘋為例',
                        style={
                            'margin-bottom':'150px'
                        }),
                html.H3('組員:蕭翊廷 周華相'),
            ]),
            html.Div(html.Img(src='assets/images/cat.jpg'))
        ],
        style={
            'display':'flex',
            'justify-content':'space-evenly',
            'align-items':'center',
            'height':'800px',
        },className="container-lg")
    ])