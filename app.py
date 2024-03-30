import streamlit as st
import time
import pandas as pd

data = pd.read_csv('/Users/vincent/Desktop/BTC_traderecords.csv',index_col=0)

for i in range(0,5):
    time.sleep(1)
    st.write('投资组合实时净值')
    st.write(data.head(2))
