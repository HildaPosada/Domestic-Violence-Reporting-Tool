import streamlit as st

# Title
st.title("Emergency App")

# Tabs
tab1, tab2, tab3 = st.tabs(["Report Now", "Resources", "Safety Tips"])

# Tab 1: Report Now
with tab1:
    st.subheader("Report Now")
    st.text_area("What happened?", placeholder="Describe the incident")
    st.date_input("Date of Incident")
    st.time_input("Time of Incident")
    st.button("Submit Report")

# Tab 2: Resources
with tab2:
    st.subheader("Resources")
    st.markdown("""
    - [National Domestic Violence Hotline](https://www.thehotline.org/)
    - [RAINN](https://www.rainn.org/)
    - [SAMHSA](https://www.samhsa.gov/)
    """)

# Tab 3: Safety Tips
with tab3:
    st.subheader("Safety Tips")
    st.markdown("""
    - Have a safety plan ready.
    - Keep emergency contacts accessible.
    - Identify safe places nearby.
    - Act quickly if you sense danger.
    """)
