from dash import dcc, html
import dash_bootstrap_components as dbc

from .star_map import draw_star_map

tab_menu_style = {
    "height": "5vh",
    "text-align": "center",
    "vertical-align": "middle",
    "align-items": "center",
    "font-size": "15px"
}
tab_style_unselected = {
    "backgroundColor": "#32383f",
    "color": "white",
    "border-style": "solid",
    "border-color": "#acb5bd",
    "border-width": "4px"
}
tab_style_selected = {
    "backgroundColor": "#272b31",
    "color": "white",
    "border-style": "solid",
    "border-color": "#acb5bd",
    "border-width": "4px"
}

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
                ),
                dcc.Tab(
                    children=[
                        # draw_star_map()
                    ],
                    label="Empty Tab 1",
                    style=tab_style_unselected,
                    selected_style=tab_style_selected
                ),
                dcc.Tab(
                    children=[
                        # draw_star_map()
                    ],
                    label="Empty Tab 2",
                    style=tab_style_unselected,
                    selected_style=tab_style_selected
                )
            ],
            style=tab_menu_style
        )
    ])

    return layout
