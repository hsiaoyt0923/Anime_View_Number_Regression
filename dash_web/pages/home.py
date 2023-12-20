import dash
from dash import html

dash.register_page(__name__, path='/',  title='動畫觀看數統計')

layout = html.Div([
    html.H1('This is our Home page'),
    html.Div('This is our Home page content.'),
])