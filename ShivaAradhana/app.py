import streamlit as st

st.set_page_config(
    page_title="Shivar Adhana",
    page_icon="🕉️",
    layout="wide"
)

st.title("🕉️ Shiva Aradhana")
st.subheader("Om Namah Shivaya")

st.write("Welcome to Shiva Aradhana")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("images/shivalinga.png",
             width = 500)


if "puja_started" not in st.session_state:
    st.session_state.puja_started = False

if "water_offered" not in st.session_state:
    st.session_state.water_offered = False

if st.button("🕉️ Start Puja"):
    st.switch_page("pages/1_puja.py")

# if st.session_state.puja_started:
#     st.success("Welcome to Shiva Pooja")
#     st.subheader("Abhishekam")

#     if st.button("💧 Offer Water"):
#         st.session_state.water_offered = True

#         if st.session_state.water_offered:
#             st.info("Water symbolizes purity and devotion.")