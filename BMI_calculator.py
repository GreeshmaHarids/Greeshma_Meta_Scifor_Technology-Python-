
import streamlit as st


def calculate_bmi():
    weight = st.session_state.weight
    height = st.session_state.height

    weight = float(weight)  
    height = float(height)
    
    if height> 0:
        bmi = weight/ (height** 2)
        st.write(f"Your BMI is: {bmi:.2f}")
        
        if bmi < 18.5:
            st.write("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.write("You are in the normal weight range.")
        elif 25 <= bmi < 29.9:
            st.write("You are overweight.")
        else:
            st.write("You are obese.")

st.title("Hello....Find Out Your BMI \nAre You in the Healthy Range?")

st.text_input("Enter your weight (kg):", key="weight")
st.text_input("Enter your height (m):", key="height")


st.button("Calculate BMI", on_click=calculate_bmi)
st.write('**Keep tracking your BMI and stay healthy!**')



