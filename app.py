import plotly.graph_objects as go
import pandas as pd

# Datos comparativos avanzados
df = pd.DataFrame({
    "Treatment": ["ABA Therapy", "Risperidone", "NeuroConnect"],
    "Lifetime Cost (USD)": [1200000, 250000, 2500],
    "Effectiveness (%)": [40, 30, 89],
    "Side Effects": [
        "Emotional stress\n(Burnout, frustration)",
        "Obesity, sedation\n(Metabolic impact)",
        "None documented\n(Biocompatible nanotech)"
    ],
    "Duration": [
        "Continuous sessions\n(20+ years)",
        "Short-term relief\n(1–2 years)",
        "Long-term effect\n(10 years, one-time)"
    ]
})

# Crear tabla visual avanzada
fig = go.Figure(data=[go.Table(
    header=dict(
        values=[
            "<b>Treatment</b>",
            "<b>Lifetime Cost (USD)</b>",
            "<b>Effectiveness (%)</b>",
            "<b>Side Effects</b>",
            "<b>Duration of Results</b>"
        ],
        fill_color='rgb(10,10,40)',
        line_color='white',
        align='center',
        font=dict(color='white', size=14),
        height=40
    ),
    cells=dict(
        values=[
            df["Treatment"],
            ["$ {:,}".format(x) for x in df["Lifetime Cost (USD)"]],
            ["{}%".format(x) for x in df["Effectiveness (%)"]],
            df["Side Effects"],
            df["Duration"]
        ],
        fill_color=[
            ['rgba(240,100,100,0.2)', 'rgba(255,195,0,0.2)', 'rgba(100,255,100,0.2)'],  # Cost
            ['rgba(240,100,100,0.1)', 'rgba(255,195,0,0.1)', 'rgba(100,255,100,0.1)'],  # Efficacy
            ['rgba(240,100,100,0.05)', 'rgba(255,195,0,0.05)', 'rgba(100,255,100,0.05)'],  # Side effects
            ['rgba(240,100,100,0.05)', 'rgba(255,195,0,0.05)', 'rgba(100,255,100,0.05)']   # Duration
        ],
        line_color='white',
        align='center',
        font=dict(color='white', size=13),
        height=80
    )
)])

# Diseño
fig.update_layout(
    title={
        'text': "🚀 Comparative Neurotech Matrix: Why NeuroConnect Outperforms Traditional Autism Treatments",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    paper_bgcolor="rgb(5,5,20)",
    margin=dict(l=10, r=10, t=80, b=10),
    height=500
)

fig.show()
