# streamlit_app.py

import streamlit as st
import requests

st.set_page_config(page_title="Theme Feature Generator", page_icon="🎯")

st.title("🎯 Theme Feature Generator")

# Theme input
theme = st.text_input("Enter a theme")

st.markdown("---")

# Option 1: Fetch features from backend
st.subheader("🔍 Option 1: Fetch Features Automatically")

if st.button("Fetch Features from Theme"):
    if theme:
        try:
            response = requests.post("http://localhost:8000/get_features", json={"theme": theme})
            response.raise_for_status()
            data = response.json()
            st.session_state["features"] = data["features"]
            st.success("✅ Features fetched successfully!")
            st.write("Features:", data["features"])
        except Exception as e:
            st.error(f"❌ Failed to fetch features: {e}")
    else:
        st.warning("⚠️ Please enter a theme before fetching features.")

# Feature selection from fetched options
selected_feature = None
if "features" in st.session_state and st.session_state["features"]:
    selected_feature = st.selectbox("Select a feature from fetched list", st.session_state["features"])

    if st.button("Generate Content from Selected Feature"):
        if theme and selected_feature:
            response = requests.post("http://localhost:8000/generate_content", json={
                "theme": theme,
                "feature": selected_feature
            })
            data = response.json()
            st.text_area("📝 Generated Content", data["content"], height=300)
        else:
            st.warning("⚠️ Theme and feature must be set.")

st.markdown("---")

# Option 2: Manual feature input
st.subheader("✍️ Option 2: Enter Feature Manually")

manual_feature = st.text_input("Enter a feature manually")

if st.button("Generate Content from Manual Feature"):
    if theme and manual_feature:
        response = requests.post("http://localhost:8000/generate_content", json={
            "theme": theme,
            "feature": manual_feature
        })
        data = response.json()
        st.text_area("📝 Generated Content", data["content"], height=300)
    else:
        st.warning("⚠️ Both theme and feature are required.")
