import streamlit as st

st.title("🪔 Arati")

col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.image("images/shivalinga.png", width=500)


st.subheader("Om Namah Shivaya")

st.info(
    "The sacred worship is nearing completion. Offer light, devotion, and gratitude to Lord Shiva through Arati."
)

