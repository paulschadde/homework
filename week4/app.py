import pandas as pd
import streamlit as st

# load data
df = pd.read_csv("disney_plus_shows.csv")

st.title("Disney+ Movies and Series")
st.markdown("Here you can see all titles on Disney+. You can filter by **type**.")

# filter
choice = st.multiselect("Type", ["movie", "series", "episode"], default=[
                        "movie", "series", "episode"])

df_new = df[df["type"].isin(choice)]

st.markdown("Number of titles: " + str(len(df_new)))
st.dataframe(df_new[["title", "type", "year", "genre", "imdb_rating"]])
