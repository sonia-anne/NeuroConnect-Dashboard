import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Comparative Matrix – NeuroConnect", layout="wide")
st.title("🧠 Comparative Matrix: NeuroConnect vs Traditional Treatments")

# Datos
treatments = ["ABA Therapy", "Risperidone", "NeuroConnect"]
metrics = ["Lifetime Cost (USD)", "Effectiveness (%)", "Duration (Years)", "Side Effects (Score)"]
values = [
    [1200000, 40, 0.5, 8],
    [250000, 30, 1, 7],
    [2500, 89, 10, 0]
]
colors = ["#FF6361", "#FFA600", "#00C49A", "#845EC2"]

fig = go.Figure()

for i, metric in enumerate(metrics):
    fig.add_trace(go.Bar(
        x=treatments,
        y=[row[i] for row in values],
        name=metric,
        marker=dict(
            color=colors[i],
            line=dict(color='black', width=1.5)
        ),
        text=[
            f"${v:,.0f}" if i == 0 else
            f"{v}%" if i == 1 else
            f"{v} yrs" if i == 2 else
            f"{v}/10" for v in [row[i] for row in values]
        ],
        textposition="outside",
        opacity=0.95
    ))

fig.update_layout(
    barmode='group',
    title={
        'text': "<b>🧠 Comparative Matrix: Cost, Efficacy, Duration & Risks</b>",
        'y':0.93,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': dict(size=24, color='white')
    },
    template="plotly",
    paper_bgcolor="rgb(0,20,10)",  # Fondo verde oscuro
    plot_bgcolor="rgb(0,20,10)",
    font=dict(family="Segoe UI", size=14, color="white"),
    legend=dict(
        title="",
        bgcolor="rgba(0,0,0,0.3)",
        bordercolor="rgba(255,255,255,0.2)",
        borderwidth=1
    ),
    xaxis=dict(title="Treatment Type", tickangle=-15, color="white"),
    yaxis=dict(title="Value", color="white", gridcolor="rgba(255,255,255,0.1)"),
    height=680
)

st.plotly_chart(fig, use_container_width=True)
