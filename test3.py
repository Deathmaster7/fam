import streamlit as st
import pickle

with open("my_list.pkl", "rb") as f:
    my_list = pickle.load(f)

st.title('Counter Example')
count = 0

increment = st.button('Increment')
if increment:
    my_list[0] += 1

st.write('Count = ', my_list[0])

with open("my_list.pkl", "wb") as f:
    pickle. dump(my_list, f)