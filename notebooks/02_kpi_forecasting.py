import streamlit as st
import pandas as pd
st.title("NUHM Urban Health Dashboard")
st.metric("ANC Coverage", "82%", "-3%")
st.metric("Immunization", "76%", "-5%")
st.write("Flagged PHCs needing intervention: PHC03, PHC07")
