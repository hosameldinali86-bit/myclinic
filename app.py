import streamlit as st
import google.generativeai as genai

# Page Configuration
st.set_page_config(page_title="Dr. Hossam Ali | Clinical AI Assistant", layout="wide")

st.title("🩺 Hepatology & GI Clinical Assistant")
st.markdown("---")

# Sidebar for Configuration
st.sidebar.header("Configuration")
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    # Main Clinical Interface
    st.header("Patient Presentation")
    complaint = st.text_area("Chief Complaint / Clinical Scenario:", placeholder="e.g., 45yo male with jaundice, dark urine, and RUQ pain...")

    if st.button("Generate Clinical Guidance"):
        if complaint:
            with st.spinner('Analyzing based on AASLD/EASL Guidelines...'):
                # Professional Medical Prompt
                prompt = f"""
                You are a Senior Consultant Hepatologist. Analyze the following clinical presentation: '{complaint}'
                
                Provide a structured clinical guidance including:
                1. Differential Diagnosis (DDx).
                2. Red Flags to rule out.
                3. Focused History & Physical Examination points.
                4. Initial Diagnostic Workup (Labs, Imaging).
                5. Preliminary Management Plan based on the latest 2024/2025 guidelines.
                
                Use professional medical terminology only.
                """
                response = model.generate_content(prompt)
                
                st.markdown("### Clinical Decision Support:")
                st.write(response.text)
        else:
            st.warning("Please enter the patient's complaint.")
else:
    st.info("Please enter your API Key in the sidebar to activate the clinical engine.")

st.sidebar.markdown("---")
st.sidebar.write("Developed for Academic & Clinical Use")
