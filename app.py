import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Dr. Hossam Ali | Clinical AI", layout="wide")
st.title("🩺 Clinical Assistant")

api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        # استخدمنا الموديل المستقر جداً لتفادي تحديثات جوجل الحالية
        model = genai.GenerativeModel('gemini-1.0-pro') 
        
        complaint = st.text_area("Patient Scenario:", placeholder="e.g., 40 year old male with jaundice")
        
        if st.button("Analyze"):
            if complaint:
                with st.spinner('Accessing Clinical Knowledge...'):
                    response = model.generate_content(f"Act as an expert Hepatologist. Analyze this case: {complaint}")
                    st.markdown("### Clinical Guidance:")
                    st.write(response.text)
            else:
                st.warning("Please enter a scenario.")
    except Exception as e:
        st.error(f"System Message: {e}")
else:
    st.info("Waiting for API Key...")
