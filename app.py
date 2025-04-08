import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="NeuroConnect vs Traditional Treatments", layout="wide")
st.title("🔬 Advanced Comparative Analysis: NeuroConnect vs Traditional Autism Treatments")

treatments = ["ABA Therapy", "Risperidone", "NeuroConnect"]
costs = [1200000, 250000, 2500]
efficacy = [40, 30, 89]
duration = [0.5, 1, 10]  # años
side_effects_score = [8, 7, 0]  # escala cualitativa 0-10
colors = ["#FF5733", "#FFC300", "#33FF57"]

fig = go.Figure()

# Costo de vida
fig.add_trace(go.Bar(
    x=treatments,
    y=costs,
    name='💰 Cost (USD, Lifetime)',
    marker_color=colors,
    text=[f"${c:,.0f}" for c in costs],
    textposition='inside'
))

# Eficacia
fig.add_trace(go.Bar(
    x=treatments,
    y=efficacy,
    name='🎯 Effectiveness (%)',
    marker_color=colors,
    text=[f"{e}%" for e in efficacy],
    textposition='inside'
))

# Duración
fig.add_trace(go.Bar(
    x=treatments,
    y=duration,
    name='⏳ Duration (Years)',
    marker_color=colors,
    text=[f"{d} yrs" for d in duration],
    textposition='inside'
))

# Efectos secundarios
fig.add_trace(go.Bar(
    x=treatments,
    y=side_effects_score,
    name='⚠️ Side Effects (Score)',
    marker_color=colors,
    text=["Severe stress", "Obesity, sedation", "None"],
    textposition='inside'
))

# Layout avanzado
fig.update_layout(
    barmode='group',
    title='📊 NeuroConnect vs Traditional Treatments: Scientific Comparative Matrix',
    xaxis_title='Treatment Type',
    yaxis_title='Metric Scale (Mixed Units)',
    legend_title='Comparison Dimensions',
    template='plotly_dark',
    font=dict(size=12, color='white'),
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(10,10,10,1)',
    height=720
)

st.plotly_chart(fig, use_container_width=True)
