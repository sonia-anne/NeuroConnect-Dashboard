import plotly.graph_objects as go

# Datos reales
tratamientos = ["ABA", "Risperidona", "NeuroConnect"]
costo_total = [1200000, 250000, 2500]
eficacia = [40, 30, 89]
efectos_secundarios = [70, 85, 2]

# Crear tabla visual con estilo neón
fig = go.Figure(data=[go.Table(
    header=dict(values=[
        "<b>Tratamiento</b>",
        "<b>Costo Total (USD)</b>",
        "<b>Eficacia (%)</b>",
        "<b>Efectos Secundarios (Índice)</b>"
    ],
        fill_color='black',
        font=dict(color='cyan', size=14),
        align='center'),
    cells=dict(values=[
        tratamientos,
        costo_total,
        eficacia,
        efectos_secundarios
    ],
        fill_color=[['#141e30', '#243b55', '#00c9ff']],  # Fondo tipo sci-fi
        font=dict(color='white', size=13),
        align='center'))
])

# Estilo del layout
fig.update_layout(
    title_text="🌐 Comparativa de NeuroConnect vs Terapias Tradicionales",
    title_font_color="aqua",
    title_font_size=22,
    paper_bgcolor="#0d1117",
    plot_bgcolor="#0d1117",
    margin=dict(l=20, r=20, t=60, b=20),
    height=450
)

fig.show()
