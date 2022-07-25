from apps.__packages import load_data, lottie
import streamlit as st
import numpy as np
import plotly.express as px
import pandas as pd


def plot_hist(_list, name="x"):
    
    fig = px.histogram(pd.DataFrame(_list, columns=[name]) ,marginal="violin")

    fig.update_layout(margin = dict(t=0, l=0, r=0, b=0)
                  , paper_bgcolor='rgba(0,0,0,0)'
                  , plot_bgcolor='rgba(0,0,0,0)')
    return fig



def app(): 
    
    data = load_data.load_data()

    st.write("data_num : ", len(data['norm']))
    st.write("OK DataLoad")
    plot_hist(data["norm"][:])
    st.write(data["norm"][:])

    