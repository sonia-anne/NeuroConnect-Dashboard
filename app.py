import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode

# Page setup
st.set_page_config(page_title="NeuroConnect Dashboard", layout="wide")

# Title and Description
st.markdown("<h1 style='color:#00ffff;'>🧠 NeuroConnect vs Traditional Autism Treatments</h1>", unsafe_allow_html=True)
st.markdown("""
Compare costs, efficacy, and side effects of major autism therapies, including **NeuroConnect** – a proposed nanotechnology-based solution to target root causes of autism spectrum conditions with precision and ethics.
""")

# Data Table
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

# Grid Configuration
gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_default_column(editable=False, groupable=True)
gb.configure_column("Lifetime Cost (USD)", type=["numericColumn"], cellStyle=JsCode("""
    function(params) {
        if (params.value > 100000) {
            return { 'color': 'red', 'fontWeight': 'bold' };
        } else {
            return { 'color': 'lime', 'fontWeight': 'bold' };
        }
    }
"""))
gb.configure_column("Efficacy (%)", type=["numericColumn"], cellStyle=JsCode("""
    function(params) {
        if (params.value >= 80) {
            return { 'backgroundColor': '#003300', 'color': 'white' };
        } else if (params.value <= 40) {
            return { 'backgroundColor': '#330000', 'color': 'white' };
        }
    }
"""))

gridOptions = gb.build()

# Render Interactive Table
st.markdown("### 📊 Interactive Treatment Comparison Table")
AgGrid(df, gridOptions=gridOptions, enable_enterprise_modules=False, theme='material', height=350, fit_columns_on_grid_load=True)

# Key Takeaways
st.markdown("#### 💡 Key Insights")
st.markdown("""
- **NeuroConnect** projects significantly higher effectiveness and lower lifetime cost.
- Traditional therapies often require repeated interventions and carry serious side effects.
- This visualization supports transparent decision-making and ethical technological innovation.
""")
