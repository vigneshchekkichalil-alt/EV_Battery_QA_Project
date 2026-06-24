import streamlit as st

st.title("🕉️ Shiva Puja")

col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.image("images/shivalinga.png", width=500)

st.subheader("Abhishekam")

if "water_offered" not in st.session_state:
    st.session_state.water_offered = False

if "milk_offered" not in st.session_state:
    st.session_state.milk_offered = False

if "curd_offered" not in st.session_state:
    st.session_state.curd_offered = False

if "honey_offered" not in st.session_state:
    st.session_state.honey_offered = False

if "ghee_offered" not in st.session_state:
    st.session_state.ghee_offered = False

if "panchamrut_offered" not in st.session_state:
    st.session_state.panchamrut_offered = False



if st.button("💧 Offer Water"):
    st.session_state.water_offered = True

if st.session_state.water_offered:
    st.success("Water offered to Lord Shiva")

    st.image("images/abhishekam/water.png", width=500)

    st.info("Water symbolizes purity and devotion.")

    st.write("🙏 Proceed to Milk Abhishekam")

    if st.button("🥛 Offer Milk"):
        st.session_state.milk_offered = True

if st.session_state.milk_offered:
    st.success("Milk offered to Lord Shiva")

    st.image("images/abhishekam/milk.png", width=500)

    st.info("Milk symbolizes purity, peace, and a long life.")

    st.write("🙏 Proceed to Curd Abhishekam")

    if st.button("🍶 Offer Curd"):
        st.session_state.curd_offered = True

if st.session_state.curd_offered:
    st.success("Curd offered to Lord Shiva")

    st.image("images/abhishekam/curd.png", width=500)

    st.info("Curd symbolizes good health, nourishment, and prosperity.")

    st.write("🙏 Proceed to Honey Abhishekam")

    if st.button("🍯 Offer Honey"):
        st.session_state.honey_offered =True

if st.session_state.honey_offered:
    st.success("Honey offered to Lord Shiva")

    st.image("images/abhishekam/honey.png", width=500)

    st.info("Honey symbolizes sweet speech, happiness, and harmony.")

    st.write("🙏 Proceed to Ghee Abhishekam")

    if st.button("🧈 Offer Ghee"):
        st.session_state.ghee_offered = True

if st.session_state.ghee_offered:
    st.success("Ghee offered to Lord Shiva")

    st.image("images/abhishekam/ghee.png", width=500)

    st.info("Ghee symbolizes strength,spiritual illumination,and removal of obstacles.")

    st.write("🙏 Proceed to Panchamrut Abhishekam")

    if st.button("🍶 Offer Panchamrut"):
        st.session_state.panchamrut_offered = True

if st.session_state.panchamrut_offered:
    st.success("Panchamrut offered to Lord Shiva")

    st.image("images/abhishekam/panchamrut.png", width=500)

    st.info("Panchamrut symbolizes purity, nourishment, prosperity, strength, and divine blessings.")

    st.success("🎉 Abhishekam Completed")

    st.markdown("# 🕉️ Har Har Mahadev 🕉️")

    st.image("images/shivalinga.png", width=500)

    st.write("""
    May Lord Shiva bless you with:
    🕉️ Peace
    💪 Strength
    📖 Wisdom
    🙏 Devotion
    🌺 Prosperity
    """)

    if st.button("🌿 Proceed to Sacred Offerings"):
        st.switch_page("pages/2_offerings.py")