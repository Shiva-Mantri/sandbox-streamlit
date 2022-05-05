import streamlit as st
import pandas as pd
import numpy as np
import altair as alt


# Day 5
st.write('Day 5 - Streamlit')

df = pd.DataFrame(np.random.rand(200, 3), columns=['a', 'b', 'c'])
c = alt.Chart(df).mark_circle().encode(x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)
st.write(df)