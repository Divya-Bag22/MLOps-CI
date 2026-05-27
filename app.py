import streamlit as st 

##Streamlit UI
st.title("Power Caluclator")
st.write("Enter a number to calculate its square, cube and fifth power")

##Getting a user input
n = st.number_input("Enter a integer" , value=1, step=1)

##Calculate results
square=n*n
cube=n*n*n
fifth=n**5

##Display results
st.write("Square is:",square)
st.write("Cube is:",cube)
st.write("Fifth Power is:",fifth)
