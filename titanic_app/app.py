
from pathlib import Path
import pandas as pd
import plotly.express as px
import streamlit as st

# Get the project directory
BASE_DIR = Path(__file__).resolve().parent

# Page configuration
st.set_page_config(layout="wide", page_title="Titanic Survival App")

# Load dataset
df = pd.read_csv(BASE_DIR / "data" / "titanic - titanic (1).csv")

# Prepare data
df.columns = df.columns.str.lower()

df["class"] = df["pclass"].map({
    1: "First",
    2: "Second",
    3: "Third"
})

df["survival"] = df["survived"].map({
    0: "Died",
    1: "Survived"
})

df["port"] = df["embarked"].map({
    "C": "Cherbourg",
    "Q": "Queenstown",
    "S": "Southampton"
})

df["family_size"] = df["sibsp"] + df["parch"] + 1

df["title"] = df["name"].str.extract(
    r",\s*([^\.]+)\.",
    expand=False
)

df["age_group"] = pd.cut(
    df["age"],
    [0, 12, 18, 35, 60, 80],
    labels=["child", "teen", "young adult", "adult", "senior"]
)

# Chart colors
COLORS = {
    "Died": "#D95D4A",
    "Survived": "#0F766E"
}

# App title
st.title("Titanic Survival App")

# Display image
image_path = BASE_DIR / "utils" / "image.webp"

if image_path.exists():
    st.image(str(image_path))
else:
    st.warning("Image file not found.")

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
    fig = px.histogram(
        data,
        x="family_size",
        nbins=11,
        labels={
            "family_size": "Family size (incl. the passenger)"
        },
        title="How big were the families on board?"
    )

    fig.update_layout(
        bargap=0.1,
        yaxis_title="Passengers"
    )

    st.plotly_chart(fig, use_container_width=True)

with c2:
    # Use filtered data instead of the original dataframe
    outcome = data["survival"].value_counts().reset_index()

    fig2 = px.pie(
        outcome,
        names="survival",
        values="count",
        hole=0.5,
        color="survival",
        color_discrete_map=COLORS,
        title="Died vs Survived"
    )

    st.plotly_chart(fig2, use_container_width=True)
