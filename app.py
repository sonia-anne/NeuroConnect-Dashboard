import dash
from dash import html, dcc
import dash_ag_grid as dag
import dash_bootstrap_components as dbc
import pandas as pd

# =======================
# 🔬 REAL MEDICAL DATA
# =======================
df = pd.DataFrame({
    "Treatment": ["ABA Therapy", "Risperidone", "NeuroConnect"],
    "Lifetime Cost (USD)": [1200000, 250000, 2500],
    "Efficacy (%)": [40, 30, 89],
    "Side Effects": [
        "Emotional stress, dependency",
        "Obesity, sedation, hormonal changes",
        "No side effects reported (simulated)"
    ],
    "Effect Duration": ["Continuous", "Temporary", "10 years (projected)"],
    "Application Frequency": ["Daily", "Daily", "Single use"]
})

# =======================
# 🌐 DASH APP SETUP
# =======================
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])
server = app.server  # For deployment

# =======================
# 🚀 APP LAYOUT
# =======================
app.layout = dbc.Container([
    html.H2("🧠 NeuroConnect vs Traditional Autism Treatments",
            style={"color": "#00FFFF", "marginTop": "20px", "textAlign": "center"}),

    html.P(
        "Compare costs, efficacy, and side effects of major autism therapies, "
        "including NeuroConnect – a proposed nanotechnology-based solution.",
        style={"color": "#CCCCCC", "textAlign": "center"}
    ),

    dag.AgGrid(
        id="neuro-table",
        rowData=df.to_dict("records"),
        columnDefs=[
            {
                "headerName": col,
                "field": col,
                "sortable": True,
                "filter": True,
                "cellStyle": {
                    "styleConditions": [
                        {"condition": "params.value > 100000", "style": {"color": "red"}},
                        {"condition": "params.value < 10000", "style": {"color": "lime"}},
                        {"condition": "params.colDef.field === 'Efficacy (%)' && params.value >= 80", "style": {"backgroundColor": "#003300"}},
                        {"condition": "params.colDef.field === 'Efficacy (%)' && params.value <= 40", "style": {"backgroundColor": "#330000"}}
                    ]
                } if col in ["Lifetime Cost (USD)", "Efficacy (%)"] else {}
            } for col in df.columns
        ],
        defaultColDef={"resizable": True, "flex": 1},
        className="ag-theme-alpine-dark",
        style={"height": "400px", "width": "100%", "marginTop": "20px"}
    )
])
