import streamlit as st
import requests
from streamlit_lottie import st_lottie

def page_set():
    #setting page areas (name, favicon, footer, etc.)
    
    st.set_page_config(page_title='TEST APP',
                           #page_icon = '__img/favi.png', #add a favicon to the folder
                           layout = 'wide',
                           initial_sidebar_state = 'auto')
    
    #generate title
    st.markdown('<style>' + open('apps/__data/icons.css').read() + '</style>', unsafe_allow_html=True)
    st.markdown("--------")
    title_l, title_r = st.columns([2,1])
    with title_r:
        lottie_data = load_lottieurl('https://assets3.lottiefiles.com/packages/lf20_u8jppxsl.json')
        st_lottie(lottie_data, height=250)
    #title_l.image("__img/AEST.png", width=250)
    title_l.title("TEST APP")
    title_l.caption("Ver. 0.1 ")
    st.markdown("--------")
         
    #create original footer
    footer_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        footer:after {
        content:'TEST APP';
        visibility: visible;
        display: block;
        position: relative;
        #background-color: lightgreen;
        padding: 5px;
        top: 2px;
        }
        </style>
        """
    st.markdown(footer_style, unsafe_allow_html=True)
    
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


