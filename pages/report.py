import streamlit as st
import streamlit.components.v1 as components




def app():


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
        
    components.iframe("https://kristineirishhh.github.io/analysis_report/", height=1100)

