
import streamlit as st
import time
import pandas as pd
import os
from WindPy import w
data = pd.read_csv('BTC_traderecords.csv')

st.write(os.getcwd())
st.write(data.head(5))
