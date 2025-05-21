import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from utils import load_all_data, compute_summary

# Load data
df_benin,df_sierraleone,df_togo = load_all_data()

st.title("Solar Data Dashboard 🌞")

st.subheader("Summary Statistics")
summary = compute_summary(df_benin,df_sierraleone,df_togo)
st.dataframe(summary)

# --- 1. Sidebar Filters ---
st.sidebar.header("Filters")
all_countries = ["Benin","Sierra Leone","Togo"]
selected_countries = st.sidebar.multiselect("Select countries", all_countries, default=all_countries)

available_attrs = ['GHI', 'DNI', 'DHI']
selected_attr = st.sidebar.selectbox("Select attribute", available_attrs)

df_benin['country'] = 'Benin'
df_sierraleone['country'] = 'Sierra Leone'
df_togo['country'] = 'Togo'

# Combine them
combined_df = pd.concat([df_benin, df_sierraleone, df_togo], ignore_index=True)

# Create the boxplot
st.subheader("Boxplot of GHI by Country")
fig, ax = plt.subplots(figsize=(8, 6))
sns.boxplot(x='country', y='GHI', data=combined_df, ax=ax)
ax.set_title("Boxplot of GHI by Country")
ax.set_ylabel("GHI")
ax.set_xlabel("Country")
ax.grid(True)

# Display it in Streamlit
st.pyplot(fig)




