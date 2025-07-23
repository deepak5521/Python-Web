import streamlit as st


name = st.text_input(" Enter Your Name : ")
fname = st.text_input(" Enter Your Father name :")
adr = st.text_input("Enter Your Text :")
classdata = st.selectbox(" Enter Your Class :",(1,2,3,4,5,6,7,8,9))

Button = st.button("Done")
if Button :
    st.markdown(f""""
    Name : {name}
    Father name:{fname}
    address : {adr}
    class : {classdata}""""")