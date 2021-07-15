import time
import webbrowser
import streamlit as st

st.title("Alarm for Website")
set_alarm = st.text_input("Set the Alarm for website as HH:MM:SS")
url = st.text_input("Enter the website URL ")
actual_time = time.strftime("%I:%M:%S")
while (actual_time != set_alarm):
    st.text("The Current time is " + actual_time)
    actual_time = time.strftime("%I:%M:%S")
    time.sleep(1)

if (actual_time == set_alarm):

    st.text("Now you can see your website")
    webbrowser.open(url)
