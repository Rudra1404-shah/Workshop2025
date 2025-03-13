import streamlit as st
import pandas as pd
import numpy as np
st.markdown("**My First Cloud App**")
st.markdown("---")
st.write("A Simple Dataframe Example")
df=pd.DataFrame(np.random.randn(10,2),columns=['cols1','cols2'])
st.dataframe(df)