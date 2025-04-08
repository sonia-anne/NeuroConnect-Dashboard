import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Advanced Comparison – NeuroConnect", layout="wide")
st.title("🔬 Multivariable Comparison: NeuroConnect vs Traditional Treatments")

# Datos
treatments = ["ABA Therapy", "Risperidone", "NeuroConnect"]
metrics = ["Lifetime Cost (USD)", "Effectiveness (%)", "Duration (Years)", "Side Effects (Score)"]

values = [
    [1200000, 40, 0.5, 8],
    [250000, 30, 1, 7],
    [2500, 89, 10, 0]
]

colors = ["#EF553B", "#00CC96", "#AB63FA", "#FFA15A"]

fig = go.Figure()

for i, metric in enumerate(metrics):
    fig.add_trace(go.Bar(
        x=treatments,
        y=[row[i] for row in values],
        name=f"{metric}",
        marker=dict(color=colors[i], line=dict(color='white', width=1)),
        text=[f"${v:,}" if i == 0 else f"{v}%" if i == 1 else f"{v} yrs" if i == 2 else f"{v}/10" for v in [row[i] for row in values]],
        textposition="auto",
        opacity=0.85
    ))

fig.update_layout(
    barmode='group',
    title={
        'text': "🧠 Comparative Matrix: Cost, Efficacy, Duration & Risks",
        'y':0.92,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    template="plotly_dark",
    paper_bgcolor="rgb(5,5,15)",
    plot_bgcolor="rgb(0,0,0)",
    font=dict(family="Arial", size=15, color="white"),
    legend=dict(
        title="Metric",
        bgcolor="rgba(0,0,0,0.4)",
        bordercolor="rgba(255,255,255,0.2)",
        borderwidth=1
    ),
    xaxis=dict(title="Treatment Type", tickangle=-15),
    yaxis=dict(title="Value", gridcolor="rgba(255,255,255,0.1)"),
    height=680
)

st.plotly_chart(fig, use_container_width=True)
