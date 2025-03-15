import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np


@st.cache_data
def load_data(file):
    return pd.read_csv(file)

file = st.file_uploader("Upload File", type=["csv"])

if file is not None:
    df = load_data(file)
    
    n_rows = st.slider("Choose number of rows to display", 
                       min_value=5, max_value=len(df), step=1)
    columns_to_show = st.multiselect("Select columns to show",
                                     df.columns.to_list(), default=df.columns.to_list())
    num_columns = df.select_dtypes(include=np.number).columns.to_list()
    
    st.write(df[:n_rows][columns_to_show])
    
    tab1, tab2 = st.tabs(["Scatter plot", "Histogram"])
     
    with tab1:    
        col1, col2, col3 = st.columns(3)
        with col1:
            x = st.selectbox("Select a colomn on x axios :", num_columns)
        with col2:
            y = st.selectbox("Select a column on y axios :", num_columns)
        with col3:
            color = st.selectbox('Select column to be color', df.columns)

        if(x and y):
            fig_scatter = px.scatter(df, x=x, y=y, color=color)
            with st.spinner("Computing ... "):
                st.plotly_chart(fig_scatter)

    with tab2:
        hist_feat = st.selectbox("Select feature to Histogram", num_columns)
        if(hist_feat):
            fig_hist = px.histogram(df, x=hist_feat)
            with st.spinner("Computing ... "):
                st.plotly_chart(fig_hist)
