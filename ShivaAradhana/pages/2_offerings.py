import streamlit as st

st.title("🌿 Sacred Offerings")

col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.image("images/shivalinga.png", width=500)

st.subheader("Om Namah Shivaya")
st.info("After completing the sacred Abhishekam, offer the divine items beloved to Lord Shiva.")

if "belpatra_offered" not in st.session_state:
    st.session_state.belpatra_offered = False

if "dhatura_offered" not in st.session_state:
    st.session_state.dhatura_offered = False

if "vibhuti_offered" not in st.session_state:
    st.session_state.vibhuti_offered = False

if "chandan_offered" not in st.session_state:
    st.session_state.chandan_offered = False

if "shami_leaves_offered" not in st.session_state:
    st.session_state.shami_leaves_offered = False


if st.button("🍃 Offer Belpatra"):
    st.session_state.belpatra_offered = True

if st.session_state.belpatra_offered:
    st.success("Belpatra offered to Lord Shiva")
    st.image("images/offerings/belpatra.png", width=500)
    st.info("Bel Patra symbolizes: Shiva's three eyes, The Holy Trinity, Purity and devotion")
    st.write("🙏 Proceed to Dhatura offering")

    if st.button("🌸 Offer Dhatura"):
        st.session_state.dhatura_offered = True

if st.session_state.dhatura_offered:
    st.success("Dhatura offered to Lord Shiva")
    st.image("images/offerings/dhatura.png", width=500)
    st.info("Dhatura symbolizes surrendering ego, anger, jealousy, and negative thoughts to Lord Shiva.")
    st.write("🙏 Proceed to Vibhuti offering")

    if st.button("🔥 Offer Vibhuti"):
        st.session_state.vibhuti_offered = True

if st.session_state.vibhuti_offered:
    st.success("Vibhuti offered to Lord Shiva")
    st.image("images/offerings/vibhuti.png", width=500)
    st.info("Vibhuti symbolizes: Detachment from worldly desires, The impermanence of life, and Spiritual purity and wisdom")
    st.write("🙏 Proceed to Chandan offering")

    if st.button("🌿 Offer Chandan"):
        st.session_state.chandan_offered = True

if st.session_state.chandan_offered:
    st.success("Chandan offered to Lord Shiva")
    st.image("images/offerings/chandan.png", width=500)
    st.info("Chandan symbolizes: Calmness, Purity of mind, Spiritual focus and devotion")
    st.write("🙏 Proceed to Shami Leaves offering")
    
    if st.button("🍂 Offer Shami Leaves"):
        st.session_state.shami_leaves_offered = True

if st.session_state.shami_leaves_offered:
    st.success("Shami Leaves offered to Lord Shiva")
    st.image("images/offerings/shami_leaves.png", width=500)
    st.info("Shami Leaves symbolize: Peace, Removal of negative karma, Humility and devotion")

    st.success("Om Namah Shivaya! You have completed the sacred offerings to Lord Shiva.")

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

    if st.button("🪔 Proceed to Arati"):
        st.switch_page("pages/3_arati.py")
