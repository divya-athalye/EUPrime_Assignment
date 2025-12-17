import streamlit as st
import pandas as pd

st.set_page_config(page_title="EUPrime Lead Ranking", layout="wide")

st.title("3D in-vitro Lead Qualification Dashboard")

# data loading
df = pd.read_csv("data.csv")

# filters
title_filter = st.text_input("Filter by Title:")
location_filter = st.text_input("Filter by Location:")

filtered_df = df.copy()

if title_filter:
    filtered_df = filtered_df[df["title"].str.contains(title_filter, case=False)]

if location_filter:
    filtered_df = filtered_df[df["person_location"].str.contains(location_filter, case=False)]

# showing the data
st.dataframe(
    filtered_df.sort_values("rank").reset_index(drop=True),
    height=500
)

csv = filtered_df.to_csv(index=False)
st.download_button("Download CSV", csv, "filtered_results.csv")
