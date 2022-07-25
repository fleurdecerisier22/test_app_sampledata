import requests
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import streamlit as st
from apps.__packages.EnvironmentVariables import Variables
variables = Variables()

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



def get_lottie(url=variables.lottieurl, height=300, width=300, key="signal"):

    lottie = load_lottieurl(url)

    return st_lottie_spinner(lottie, height=height, width=width, key=key)

