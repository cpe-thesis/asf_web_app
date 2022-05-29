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
    

    vis = st.sidebar.selectbox("Map Visualisation",
		["Flow of Outbreak", "Outbreak Severities"])

    if(vis == "Flow of Outbreak"):
        try:
            components.iframe("https://kristineirishhh.github.io/map_visualisation/", height=850)

        except:
             pass
    elif(vis == "Outbreak Severities"):
        try:
            components.iframe("https://kristineirishhh.github.io/outbreak_severities/", height=850)
        except:
             pass




    
    
   


    


   


    
