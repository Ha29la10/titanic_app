
from pathlib import Path
import pandas as pd
import plotly.express as px
import streamlit as st
from utils.data import load_data
from pathlib import Path
from utils.config import ORDERS,COLORS
from utils.figures import plot_family_size,plot_outcome


BASE_DIR = Path(__file__).resolve().parent
df=load_data()
# Page configuration
st.set_page_config(layout="wide", page_title="Titanic Survival App")

# App title
st.title("Titanic Survival App")

# Display image
image_path = BASE_DIR / "utils" / "image.webp"
st.image(str(image_path))


# Show dataset
show_data = st.checkbox("Show data")

if show_data:
    st.dataframe(df, hide_index=True)

# Filters
classes = st.multiselect(
    "Select class",
    options=["First", "Second", "Third"],
    default=["First", "Second", "Third"]
)

gender = st.radio(
    "Select gender",
    ["male", "female"],
    horizontal=True
)

# Apply filters
data = df[
    (df["class"].isin(classes)) &
    (df["sex"] == gender)
]

# Charts
c1, c2 = st.columns(2)

with c1:
     st.plotly_chart(plot_family_size(data))

with c2:
    # Use filtered data instead of the original dataframe

    st.plotly_chart(plot_outcome(data))
