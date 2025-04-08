import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="3D Scientific Matrix – NeuroConnect", layout="wide")
st.title("🧠 Multivariable 3D Matrix: NeuroConnect vs Traditional Treatments")

# Datos principales
treatments = ["ABA", "Risperidone", "NeuroConnect"]
costs = [1200000, 250000, 2500]
efficacy = [40, 30, 89]
duration = [0.5, 1, 10]
side_effects = [8, 7, 0]

# Crear gráfico 3D tipo holograma
fig = go.Figure(data=[go.Scatter3d(
    x=costs,
    y=efficacy,
    z=duration,
    text=[
        f"<b>{treatments[i]}</b><br>"
        f"💰 Cost: ${costs[i]:,}<br>"
        f"🎯 Efficacy: {efficacy[i]}%<br>"
        f"⏳ Duration: {duration[i]} years<br>"
        f"⚠️ Side Effects: {side_effects[i]}/10"
        for i in range(3)
    ],
    mode='markers+text',
    marker=dict(
        size=[20, 20, 30],
        color=[costs[i]/1000000 for i in range(3)],
        colorscale='Viridis',
        opacity=0.9,
        line=dict(width=2, color='white')
    ),
    textposition="top center"
)])

# Estética de fondo holográfica
fig.update_layout(
    title='<b>3D Scientific Matrix</b><br>Cost vs Efficacy vs Duration (with Side Effects)',
    scene=dict(
        xaxis_title='💰 Cost (USD)',
        yaxis_title='🎯 Efficacy (%)',
        zaxis_title='⏳ Duration (Years)',
        bgcolor="rgb(0,10,10)",
        xaxis=dict(color='white', gridcolor='gray'),
        yaxis=dict(color='white', gridcolor='gray'),
        zaxis=dict(color='white', gridcolor='gray')
    ),
    paper_bgcolor="rgb(0,10,10)",
    font=dict(color="white", size=14),
    height=750,
    margin=dict(l=0, r=0, b=0, t=80)
)

st.plotly_chart(fig, use_container_width=True)
