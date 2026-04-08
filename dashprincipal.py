import pandas as pd
import plotly.express as px
import dash
from dash import html, Input, Output, dcc
from dash import dash_table
from database import obtenerestudiantes


def creartablero(server):

    appnotas = dash.Dash(
        __name__,
        server=server,
        url_base_pathname="/dashprincipal/",
        suppress_callback_exceptions=True
    )


    # LAYOUT DINAMICO
    def layout():

        dataf = obtenerestudiantes()

        if dataf.empty:
            carreras = []
            edad_min = 0
            edad_max = 50
        else:
            carreras = sorted(dataf["carrera"].unique())
            edad_min = int(dataf["edad_estu"].min())
            edad_max = int(dataf["edad_estu"].max())

        return html.Div([

            html.H1(
                "TABLERO AVANZADO",
                style={
                    "textAlign": "center",
                    "backgroundColor": "#1e3a8a",
                    "color": "white",
                    "padding": "20px",
                    "borderRadius": "10px"
                }
            ),

            html.Br(),

            html.Div([

                html.Label("Seleccionar carrera"),

                dcc.Dropdown(
                    id="filtro_carrera",
                    options=[{"label": c, "value": c} for c in carreras],
                    placeholder="Seleccionar carrera"
                ),

                html.Br(),

                html.Label("Rango de edad"),

                dcc.RangeSlider(
                    id="slider_edad",
                    min=edad_min,
                    max=edad_max,
                    step=1,
                    value=[edad_min, edad_max],
                    tooltip={"placement": "bottom"}
                ),

                html.Br(),

                html.Label("Rango promedio"),

                dcc.RangeSlider(
                    id="slider_promedio",
                    min=0,
                    max=5,
                    step=0.1,
                    value=[0, 5],
                    tooltip={"placement": "bottom"}
                )

            ], style={
                "width": "80%",
                "margin": "auto",
                "backgroundColor": "white",
                "padding": "20px",
                "borderRadius": "10px"
            }),

            html.Br(),

            html.Div(
                id="kpis",
                style={
                    "display": "flex",
                    "justifyContent": "space-around"
                }
            ),

            html.Br(),

            dash_table.DataTable(
                id="tabla",
                page_size=8,
                filter_action="native",
                sort_action="native",
                row_selectable="multi",
                selected_rows=[],
                style_table={"overflowX": "auto"},
                style_cell={"textAlign": "center"},
                style_header={
                    "backgroundColor": "#1e3a8a",
                    "color": "white",
                    "fontWeight": "bold"
                }
            ),

            html.Br(),

            dcc.Input(
                id="busqueda",
                type="text",
                placeholder="Buscar estudiante...",
                style={
                    "width": "50%",
                    "padding": "10px",
                    "margin": "auto",
                    "display": "block"
                }
            ),

            html.Br(),

            dcc.Interval(
                id="intervalo",
                interval=3000,
                n_intervals=0
            ),

            dcc.Graph(id="gra_detallado"),

            html.Br(),

            dcc.Tabs([

                dcc.Tab(
                    label="Histograma",
                    children=[dcc.Graph(id="histograma")]
                ),

                dcc.Tab(
                    label="Dispersion",
                    children=[dcc.Graph(id="dispersion")]
                ),

                dcc.Tab(
                    label="Desempeño",
                    children=[dcc.Graph(id="pie")]
                ),

                dcc.Tab(
                    label="Promedio por Carrera",
                    children=[dcc.Graph(id="barras")]
                )

            ])

        ], style={"backgroundColor": "#f4f6fb", "padding": "20px"})


    appnotas.layout = layout


    # CALLBACK PRINCIPAL
    @appnotas.callback(

        Output("tabla", "data"),
        Output("tabla", "columns"),
        Output("kpis", "children"),
        Output("histograma", "figure"),
        Output("dispersion", "figure"),
        Output("pie", "figure"),
        Output("barras", "figure"),

        Input("intervalo", "n_intervals"),
        Input("filtro_carrera", "value"),
        Input("slider_edad", "value"),
        Input("slider_promedio", "value"),
        Input("busqueda", "value")

    )

    def actualizar_comp(n, carrera, rangoedad, rangoprome, busqueda):

        dataf = obtenerestudiantes()

        if dataf.empty:
            return [], [], [], px.scatter(), px.scatter(), px.pie(), px.bar()

        filtro = dataf.copy()

        if carrera:
            filtro = filtro[filtro["carrera"] == carrera]

        filtro = filtro[
            (filtro["edad_estu"] >= rangoedad[0]) &
            (filtro["edad_estu"] <= rangoedad[1]) &
            (filtro["promedio"] >= rangoprome[0]) &
            (filtro["promedio"] <= rangoprome[1])
        ]

        if busqueda:
            filtro = filtro[
                filtro["nombre_estu"].str.contains(busqueda, case=False, na=False)
            ]

        promedio = round(filtro["promedio"].mean(), 2) if len(filtro) > 0 else 0
        total = len(filtro)
        maximo = round(filtro["promedio"].max(), 2) if len(filtro) > 0 else 0


        kpis = [

            html.Div(
                [html.H4("Promedio"), html.H2(promedio)],
                style={
                    "backgroundColor": "#3b82f6",
                    "color": "white",
                    "padding": "20px",
                    "borderRadius": "10px",
                    "width": "25%",
                    "textAlign": "center"
                }
            ),

            html.Div(
                [html.H4("Total estudiantes"), html.H2(total)],
                style={
                    "backgroundColor": "#10b981",
                    "color": "white",
                    "padding": "20px",
                    "borderRadius": "10px",
                    "width": "25%",
                    "textAlign": "center"
                }
            ),

            html.Div(
                [html.H4("Máximo"), html.H2(maximo)],
                style={
                    "backgroundColor": "#6366f1",
                    "color": "white",
                    "padding": "20px",
                    "borderRadius": "10px",
                    "width": "25%",
                    "textAlign": "center"
                }
            )

        ]


        histo = px.histogram(
            filtro,
            x="promedio",
            nbins=10,
            title="Distribución de Promedios"
        )


        dispersion = px.scatter(
            filtro,
            x="edad_estu",
            y="promedio",
            color="desempeno",
            trendline="ols",
            title="Edad vs Promedio"
        )


        pie = px.pie(
            filtro,
            names="desempeno",
            title="Distribución por Desempeño"
        )


        promedios = dataf.groupby("carrera")["promedio"].mean().reset_index()

        barras = px.bar(
            promedios,
            x="carrera",
            y="promedio",
            color="carrera",
            title="Promedio General por Carrera"
        )


        return (
            filtro.to_dict("records"),
            [{"name": i, "id": i} for i in filtro.columns],
            kpis,
            histo,
            dispersion,
            pie,
            barras
        )


    @appnotas.callback(

        Output("gra_detallado", "figure"),
        Input("tabla", "derived_virtual_data"),
        Input("tabla", "derived_virtual_selected_rows")

    )

    def actualizartab(rows, selected_rows):

        if rows is None or len(rows) == 0:
            return px.scatter(title="Sin datos")

        dff = pd.DataFrame(rows)

        if selected_rows:
            dff = dff.iloc[selected_rows]

        fig = px.scatter(
            dff,
            x="edad_estu",
            y="promedio",
            color="desempeno",
            size="promedio",
            title="Analisis detallado"
        )

        return fig


    return appnotas