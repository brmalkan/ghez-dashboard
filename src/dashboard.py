from dash import Dash, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

from data_loader import (
    find_neighbor_stars,
    load_starset_data,
    load_orbits
)
from gcwork.starset import StarSet
from layout import app_layout


class Dashboard:

    def __init__(self) -> None:
        """
        Initialize app and load layout. Dark mode css
        themes extracted from assets directory
        """

        self.app: Dash = Dash(assets_folder="../assets")
        self.app.layout = app_layout()

        self.star_data: None | StarSet = None

    def start(self) -> None:

        @self.app.callback(
            Output("star_map_2d", "figure"),
            # Output("star_map_3d", "figure"),
            Output("star_reference_list", "options"),
            Input("refresh_button", "n_clicks"),
            [State("data_filepath", "value"),
            State("orbit_filepath", "value"),
            State("map_range", "value"),
            State("map_center_x", "value"),
            State("map_center_y", "value"),
            State("map_radio_options", "value")],
        )
        def update_starmap(
            _refresh_button: int,
            data_filepath: str,
            orbit_filepath: str,
            range: float,
            center_x: float,
            center_y: float,
            radio_options: list[bool],
        ) -> None:
            if not data_filepath:
                return go.Figure() # TODO Add Error

            self.star_data = load_starset_data(data_filepath)
            show_name = True

            fig_2d = go.Figure()
            fig_2d.add_trace(
                go.Scattergl(
                    x=self.star_data["x"],
                    y=self.star_data["y"],
                    customdata=self.star_data["name"],
                    mode="markers+text" if show_name else "markers",
                    text=self.star_data["name"] if show_name else None,
                    textposition="top center",
                    textfont={
                        "size": 8,
                        "color": "white",
                        "family": "Times New Roman"
                    },
                    marker={
                        "size": 5,
                        "color": "cyan",
                        "opacity": 0.7
                    }
                )
            )
            fig_2d.update_layout(
                template="plotly_dark",
                clickmode="event",
                dragmode="pan",
                xaxis={
                    "scaleanchor": "y",
                    "scaleratio": 1,
                    "range": [center_x - range, center_x + range],
                    "color": "white",
                    "gridcolor": "rgba(0, 0, 0, 0.3)"
                },
                yaxis={
                    "range": [center_y - range, center_y + range],
                    "color": "white",
                    "gridcolor": "rgba(0, 0, 0, 0.3)"
                },
                showlegend=False,
                margin=dict(t=20, b=20, r=20, l=20),
                plot_bgcolor="rgba(0,0,0,0)",
                paper_bgcolor="rgba(0,0,0,0)",
            )

            fig_3d = go.Figure()
            fig_3d.add_trace(
                go.Scatter3d(

                )
            )

            if orbit_filepath:
                orbit_data = load_orbits(orbit_filepath)

            return fig_2d, self.star_data["name"]

        @self.app.callback(
            Output("star_reference_list", "value"),
            Input("star_map_2d", "clickData"),
            prevent_initial_call=True
        )
        def update_neighbor_reference(star_data: dict[any]) -> None:
            star_name = star_data["points"][0]["customdata"]
            return star_name

        @self.app.callback(
            Output("neighbor_table", "data"),
            Input("star_reference_list", "value"),
            prevent_initial_call=True
        )
        def update_neighbor_table(star_name: str) -> None:
            table_data = find_neighbor_stars(self.star_data, star_name)

            # table_data = [
            #     {"star": star_name, "distance": 1.2},
            #     {"star": "Beta", "distance": 3.4},
            #     {"star": "Gamma", "distance": 2.1},
            #     {"star": "Delta", "distance": 4.8},
            #     {"star": "Epsilon", "distance": 0.9},
            #     {"star": "Zeta", "distance": 5.6},
            #     {"star": "Eta", "distance": 3.2},
            #     {"star": "Theta", "distance": 6.7},
            #     {"star": "Iota", "distance": 1.8},
            #     {"star": "Kappa", "distance": 2.9},
            #     {"star": "Lambda", "distance": 7.1},
            #     {"star": "Mu", "distance": 4.2},
            #     {"star": "Nu", "distance": 5.0},
            #     {"star": "Xi", "distance": 3.7},
            #     {"star": "Omicron", "distance": 6.3},
            #     {"star": "Pi", "distance": 2.4},
            #     {"star": "Rho", "distance": 1.5},
            #     {"star": "Sigma", "distance": 4.9},
            #     {"star": "Tau", "distance": 5.8},
            #     {"star": "Upsilon", "distance": 3.0},
            #     {"star": "Phi", "distance": 6.0},
            # ]

            return table_data

        self.app.run(
            port=8050,
            dev_tools_silence_routes_logging=True,
            debug=False
        )
