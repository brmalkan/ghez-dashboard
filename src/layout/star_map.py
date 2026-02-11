from dash import html
import dash_bootstrap_components as dbc

def draw_star_map() -> html.Div:
    return html.Div([
        dbc.Card(
            dbc.CardBody(
                children=[
                    dbc.Row(
                        children=[
                            dbc.Col(
                                children=[draw_config_box()],
                                width=2
                            ),
                            dbc.Col(
                                children=[draw_star_plot()],
                                width=7
                            ),
                            dbc.Col(
                                children=[draw_neighbor_table()],
                                width=3
                            )
                        ],
                        className="dbc"
                    )
                ]
            )
        )
    ])

def draw_config_box() -> html.Div:
    return html.Div()

def draw_star_plot() -> html.Div:
    return html.Div()

def draw_neighbor_table() -> html.Div:
    return html.Div()
