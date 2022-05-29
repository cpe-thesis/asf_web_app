import streamlit as st
import streamlit.components.v1 as components


def app():

    st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)

    st.markdown("""
        <style>
               .css-18e3th9 {
                    padding-top: 0rem;
                    padding-bottom: 0rem;
                    padding-left: 0rem;
                    padding-right: 0rem;
                }
               .css-1d391kg {
                    padding-top: 0rem;
                    padding-right: 0rem;
                    padding-bottom: 0rem;
                    padding-left: 0rem;
                }
        </style>
        """, unsafe_allow_html=True)

    components.iframe("https://kristineirishhh.github.io/home_about/", height=1000)

    
