import dash
from dash import html


dash.register_page(__name__,
                   title='動畫觀看數統計',
                   path='/')

layout = html.Div(
        [html.Div([
            html.Div([
                html.H1('動畫觀看數統計'),
                html.H2('以巴哈姆特動畫瘋為例'),
                html.H3('組員:蕭翊廷 周華相'),
            ],className='textbox',
            ),
            html.Div([html.Video(src='./assets/video/oshinoko.mp4',
                                width='700',
                                height='100%',
                                autoPlay=True,
                                loop=True,
                                muted=False,
                                controls=True,
                                className='video',
                                ),
                      html.Div(className='shadow_box'),
            ])
        ],
        style={
            'position':'relative',
            'display':'flex',
            'height':'800',
        },className="container-lg")
    ],
    style={
        'padding': '200px 0',
    },className="container-lg bgbox")