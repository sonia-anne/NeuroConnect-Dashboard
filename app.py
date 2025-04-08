import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title="NeuroConnect: 3D Cost Comparison", layout="wide")

st.title("🧠 NeuroConnect - Comparativa Tridimensional de Tratamientos para TEA")

# Datos comparativos reales y proyectados
tratamientos = ["ABA", "Risperidona", "NeuroConnect"]
costo_total = [1200000, 250000, 2500]  # USD
eficacia = [40, 30, 89]  # Porcentaje
efectos_sec = [7, 8, 1]  # Escala 1 (mínimo) a 10 (máximo)

# Tabla 3D: Eficacia vs Costo vs Efectos Secundarios
fig = go.Figure(data=[go.Scatter3d(
    x=costo_total,
    y=eficacia,
    z=efectos_sec,
    mode='markers+text',
    marker=dict(
        size=12,
        color=eficacia,
        colorscale='Viridis',
        opacity=0.95,
        line=dict(width=2, color='DarkSlateGrey')
    ),
    text=tratamientos,
    hoverinfo='text'
)])

# Estética del gráfico 3D
fig.update_layout(
    scene=dict(
        xaxis_title='Costo Total (USD)',
        yaxis_title='Eficacia (%)',
        zaxis_title='Efectos Secundarios (1=Mínimo, 10=Máximo)',
        xaxis=dict(backgroundcolor="black", color="white", gridcolor="gray"),
        yaxis=dict(backgroundcolor="black", color="white", gridcolor="gray"),
        zaxis=dict(backgroundcolor="black", color="white", gridcolor="gray"),
    ),
    template="plotly_dark",
    margin=dict(l=0, r=0, b=0, t=50),
    height=800,
    hoverlabel=dict(bgcolor="white", font_size=16, font_family="Courier New"),
    title={
        'text': "🧬 Comparativa Tridimensional de NeuroConnect vs Tratamientos Actuales",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)

st.plotly_chart(fig, use_container_width=True)
