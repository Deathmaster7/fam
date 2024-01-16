import streamlit as st
import pickle

my_list = [1, 2, 3, 4, 5]

with open("my_list.pkl", "wb") as f:
    pickle. dump(my_list, f)