

# Load Libraries----------------
import numpy as np
import pickle
import pandas as pd
import streamlit as st 

# Import the Model--------------
pickle_in = open("rk.pkl","rb")
rf = pickle.load(pickle_in)


# A function to predict Fuel efficiency------------------------------------------
def predict_Fuel_efficiency(Eng_Displ, Cyl, Gears,
       Max_Ethanol_Gasoline, Intake_Valves_Per_Cyl,
       Exhaust_Valves_Per_Cyl, Var_Valve_Lift, Fuel_Metering_Sys_Desc,
       Stop_Start_System_Description, Air_Aspiration_Method_Desc, Label_Recalc , Eng_Displ_na,
       Max_Ethanol_Gasoline_na):
    prediction=rf.predict([[Eng_Displ, Cyl, Gears,
       Max_Ethanol_Gasoline, Intake_Valves_Per_Cyl,
       Exhaust_Valves_Per_Cyl, Var_Valve_Lift, Fuel_Metering_Sys_Desc,
       Stop_Start_System_Description,
       Air_Aspiration_Method_Desc, Label_Recalc , Eng_Displ_na,
       Max_Ethanol_Gasoline_na]])
    print(prediction)
    return prediction


# User Interface--------------------------------------------------------
def main():
    st.title("Fuel Efficieny")
    Eng_Displ = st.text_input("Engine","Type Here")
    Cyl = st.text_input("# of Cylinder","Type Here")
    Gears = st.slider("Gears", min_value = 1, max_value = 10, step = 1)
    Max_Ethanol_Gasoline = st.text_input("Gasoline","Type Here")
    Intake_Valves_Per_Cyl = st.text_input("Intake of Cylinder","Type Here")
    Exhaust_Valves_Per_Cyl = st.text_input("Exhaust", "Type Here")
    Var_Valve_Lift = st.text_input("Lift Value" , "Type Here")
    Fuel_Metering_Sys_Desc = st.text_input("Fuel Meter" , "Type Here")
    Stop_Start_System_Description = st.text_input("Stop/start description" ,"Type Here")
    Air_Aspiration_Method_Desc = st.text_input("Air Desc","Type Here")
    Label_Recalc = st.text_input("Label" , "Type Here")
    Eng_Displ_na = st.text_input("Eng displ_new" , "Type Here")
    Max_Ethanol_Gasoline_na = st.text_input("Gasoline_new" , "Type Here")
    result=""
    if st.button("Predict"):
        result=predict_Fuel_efficiency(Eng_Displ, Cyl, Gears,
       Max_Ethanol_Gasoline, Intake_Valves_Per_Cyl,
       Exhaust_Valves_Per_Cyl, Var_Valve_Lift, Fuel_Metering_Sys_Desc,
       Stop_Start_System_Description,
       Air_Aspiration_Method_Desc, Label_Recalc , Eng_Displ_na,
       Max_Ethanol_Gasoline_na)
    st.success('The output is {}'.format(result))
    

if __name__=='__main__':
    main()