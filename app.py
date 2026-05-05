import streamlit as st
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

from src.load_data import load_dataset
from src.build_graph import create_graph
from src.analysis import compute_single_table

st.title("📊 Tourist Network Analysis - Thanjavur")

# Load data
df = load_dataset("data/tourist_spots.csv")
G = create_graph(df)
table = compute_single_table(G)

# Interactive Table
st.subheader("📋 SNA Table")
st.dataframe(table, use_container_width=True)

# Dropdown filter (animation-like)
spot = st.selectbox("Select Tourist Spot", table["Tourist Spot"])
filtered = table[table["Tourist Spot"] == spot]

st.subheader("🔍 Selected Spot Details")
st.dataframe(filtered)

# Graph
st.subheader("🌐 Network Graph")

plt.figure(figsize=(8,6))
pos = nx.spring_layout(G, seed=42)

nx.draw(G, pos, with_labels=True, node_size=3000)

st.pyplot(plt)