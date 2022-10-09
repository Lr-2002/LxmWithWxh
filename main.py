import streamlit as st
import cv2
import pandas as pd

if __name__ == '__main__':
    st.title('Lxm with Wxh')
    lxm = cv2.imread('./lxm.jpg')
    lxm = cv2.cvtColor(lxm, cv2.COLOR_BGR2RGB)
    st.image(lxm)
    st.title('To Do List')
    df=  pd.read_csv('lxmwithwxh.csv')
    st.table(df)