import streamlit as st
import pickle
import numpy as np

model1=pickle.load(open('ANNModel (annual).pkl','rb'))

def predict_cases(province_id,rainfall,tmax,tmin,tmean,rh,sh,surface_pressure,wind_speed,wind_direction,pig_density,susceptible):
    input=np.array([[province_id,rainfall,tmax,tmin,tmean,rh,sh,surface_pressure,wind_speed,wind_direction,pig_density,susceptible]]).astype(np.float64)
    prediction=model1.predict(input)
    
    return float(prediction)

model2=pickle.load(open('RandomForestModel (per semester).pkl','rb'))

def predictcases(province_id,rainfall,tmax,tmin,tmean,rh,sh,surface_pressure,wind_speed,wind_direction,susceptible):
    input=np.array([[province_id,rainfall,tmax,tmin,tmean,rh,sh,surface_pressure,wind_speed,wind_direction,susceptible]]).astype(np.float64)
    pred=model2.predict(input)
    
    return float(pred)

def app():


        st.write('<style>div.block-container{padding-top:2rem;}</style>', unsafe_allow_html=True)
        st.text('Input the weather and ASF data, then click submit to forecast the probability of the ASF outbreak.')
        

        

        forecast = st.sidebar.selectbox("Forecast an Outbreak",
		["Annually", "Per Semester"])

        if(forecast == "Annually"):
                display = ("Abra", "Benguet", "Ifugao", "Kalinga", "Mountain Province", "Apayao", "Ilocos Norte", 
                                "Ilocos Sur", "La Union", "Pangasinan", "Batanes", "Cagayan", "Isabela", "Nueva Vizcaya",
                                "Quirino", "Bataan", "Bulacan", "Nueva Ecija", "Pampanga", "Tarlac", "Zambales", "Aurora",
                                "NCR First District", "NCR Second District", "NCR Third District", "NCR Fourth District", 
                                "Batangas", "Cavite", "Laguna", "Quezon", "Rizal", "Marinduque", "Mindoro Occidental",
                                "Mindoro Oriental", "Palawan", "Romblon", "Albay", "Camarines Norte", "Camarines Sur",
                                "Catanduanes", "Masbate", "Sorsogon", "Aklan", "Antique", "Capiz", "Iloilo", "Negros Occidental",
                                "Guimaras", "Bohol", "Cebu", "Negros Oriental", "Siquijor", "Eastern Samar", "Leyte",
                                "Northern Samar", "Samar", "Southern Leyte", "Biliran", "Zamboanga del Norte", "Zamboanga del Sur",
                                "Zamboanga Sibugay", "Isabela City", "Bukidnon", "Camiguin", "Lanao del Norte", "Misamis Occidental",
                                "Misamis Oriental", "Davao del Norte", "Davao del Sur", "Davao Oriental", "Davao de Oro", "Davao Occidental",
                                "North Cotabato", "South Cotabato", "Sultan Kudarat", "Sarangani", "Cotabato City", "Agusan del Norte", "Agusan del Sur",
                                "Surigao del Norte", "Surigao del Sur", "Dinagat Islands", "Basilan", "Lanao del Sur", "Maguindanao", 
                                "Sulu", "Tawi-Tawi")

                options = list(range(len(display)))
        
                try:

                        province_id = st.selectbox("Province:", options, format_func=lambda x: display[x])
                        rainfall = st.text_input('Rainfall:')
                        tmax = st.text_input('Maximum Temperature:')
                        tmin = st.text_input('Minimum Temperature:')
                        tmean = st.text_input('Mean Temperature:')
                        rh = st.text_input('Relative Humidity:')
                        sh = st.text_input('Specific Humidity:')
                        surface_pressure = st.text_input('Surface Pressure:')
                        wind_speed = st.text_input('Wind Speed:')
                        wind_direction = st.text_input('Wind Direction')
                        pig_density = st.text_input('Pig Density:')
                        susceptible = st.text_input('Susceptible:')
                
                        if st.button("Submit"):
                                output1=predict_cases(province_id,rainfall,tmax,tmin,tmean,rh,sh,surface_pressure,wind_speed,wind_direction,pig_density,susceptible)
                                cases1 = int(output1)
                                st.success('The number of possible cases: {}'.format(cases1))
                
                except:
                        pass

        elif(forecast == "Per Semester"):
                display1 = ("Abra", "Benguet", "Ifugao", "Kalinga", "Mountain Province", "Apayao", "Ilocos Norte", "Ilocos Sur",
                                "La Union", "Pangasinan", "Batanes", "Cagayan", "Isabela", "Nueva Vizcaya", "Quirino", "Bataan", "Bulacan",
                                "Nueva Ecija", "Pampanga", "Tarlac", "Zambales", "Aurora", "NCR First District", "NCR Second District", 
                                "NCR Third District", "NCR Fourth District", "Batangas", "Cavite", "Laguna", "Quezon", "Rizal", "Marinduque", 
                                "Mindoro Occidental", "Mindoro Oriental", "Palawan", "Romblon", "Albay", "Camarines Norte", "Camarines Sur", 
                                "Catanduanes", "Masbate", "Sorsogon", "Aklan", "Antique", "Capiz", "Iloilo", "Negros Occidental", "Guimaras", 
                                "Bohol", "Cebu", "Negros Oriental", "Siquijor", "Eastern Samar", "Leyte", "Northern Samar", "Samar", 
                                "Southern Leyte", "Biliran", "Zamboanga del Norte", "Zamboanga del Sur", "Isabela City", "Bukidnon", "Camiguin", 
                                "Lanao del Norte", "Misamis Occidental", "Misamis Oriental", "Davao del Norte", "Davao del Sur", "Davao Oriental", 
                                "Davao de Oro", "Davao Occidental", "North Cotabato", "South Cotabato", "Sultan Kudarat", "Sarangani", 
                                "Cotabato City", "Agusan del Norte", "Agusan del Sur", "Surigao del Norte", "Surigao del Sur", "Dinagat Islands", 
                                "Basilan", "Maguindanao", "Sulu", "Tawi-Tawi", "Lanao del Sur", "Zamboanga Sibugay" )

                options1 = list(range(len(display1)))
                try:

                        province_id = st.selectbox("Province:", options1, format_func=lambda x: display1[x])
                        rainfall = st.text_input('Rainfall:')
                        tmax = st.text_input('Maximum Temperature:')
                        tmin = st.text_input('Minimum Temperature:')
                        tmean = st.text_input('Mean Temperature:')
                        rh = st.text_input('Relative Humidity:')
                        sh = st.text_input('Specific Humidity:')
                        surface_pressure = st.text_input('Surface Pressure:')
                        wind_speed = st.text_input('Wind Speed:')
                        wind_direction = st.text_input('Wind Direction')
                        susceptible = st.text_input('Susceptible:')
                
                        if st.button("Submit"):
                                output2=predictcases(province_id,rainfall,tmax,tmin,tmean,rh,sh,surface_pressure,wind_speed,wind_direction,susceptible)
                                cases2 = int(output2)
                                st.success('The number of possible cases: {}'.format(cases2))
                except:
                        pass

