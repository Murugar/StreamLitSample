import pandas as pd
import numpy as np
import altair as alt
import streamlit as st

df = pd.DataFrame(np.random.randn(255, 3), columns=['a', 'b', 'c'])
c = alt.Chart(df).mark_rect().encode(x='a', y='b', size='c',  
                                       color='c')
st.altair_chart(c)
