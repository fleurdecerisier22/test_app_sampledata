
import h5py
import streamlit as st
from apps.__packages.EnvironmentVariables import Variables


variables = Variables()


@st.cache(allow_output_mutation=True)
def load_data():
    
    """
    load data streamlit virtual dataset h5py 
    
    original 'apps/__data/faers_data/*.h5py'
    """

    data = h5py.File(variables.sample_data, 'r')

    return data

