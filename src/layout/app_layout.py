from dash import dcc, html
import dash_bootstrap_components as dbc

from .star_map import draw_star_map

tab_menu_style = {}
tab_style_unselected = {}
tab_style_selected = {}

def app_layout() -> html.Div:
    """
    Returns full app layout
    """

    layout = html.Div([
        dcc.Tabs(
            children=[
                dcc.Tab(
                    children=[
                        draw_star_map()
                    ],
                    label="Star Map",
                    style=tab_style_unselected,
                    selected_style=tab_style_selected
                )
            ],
            style=tab_menu_style
        )
    ])

    return layout
