import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title("Aplicación web")

data = np.random.normal(0, 1, size=(50, 4))

df = pd.DataFrame(data=data,
                  columns=['col1', 'col2', 'col3', 'col4'])

fig, ax = plt.subplots(1, 3)

ax[0].hist(df['col1'])
ax[1].scatter(df['col1'], df['col2'])
ax[2].hist(df['col3'])

fig.tight_layout()

st.pyplot(fig)

