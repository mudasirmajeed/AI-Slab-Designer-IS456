
import streamlit as st
import joblib
import numpy as np

model = joblib.load('slab_designer_model.pkl')
st.title("🏗️ AI Slab Designer (IS 456)")
Lx = st.number_input("Short Span (m)", value=3.5)
Ly = st.number_input("Long Span (m)", value=4.5)
LL = st.selectbox("Live Load (kN/m2)", [2.0, 3.0, 4.0, 5.0])
fck = st.radio("Concrete Grade", [20, 25])

if st.button("Design"):
    pred = model.predict([[Lx, Ly, LL, fck]])[0]
    st.success(f"Thickness: {int(pred[0])} mm")
    st.info(f"Steel: 10mm bars @ {int(min(300, (78.5/pred[1])*1000))}mm c/c")
