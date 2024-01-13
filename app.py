import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(layout='wide')

st.title("Aplicación web")

data = np.random.normal(0, 1, size=(1000, 4))

df = pd.DataFrame(data=data,
                  columns=['col1', 'col2', 'col3', 'col4'])

fig, ax = plt.subplots(1, 3, figsize=(6, 2))

ax[0].hist(df['col1'], color='orange')
ax[1].scatter(df['col1'], df['col2'], color='red')
ax[2].hist(df['col3'], color='darkred')

fig.tight_layout()

st.pyplot(fig)

if st.button("Clic aquí"):
    fig, ax = plt.subplots(1, 2, figsize=(4, 2))
    ax[0].hist(df['col3'], bins=50)
    ax[1].scatter(df['col1'], df['col4'])
    st.pyplot(fig)

