import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Dr. Hossam Ali | Clinical Assistant", layout="centered")
st.title("🩺 Clinical AI Assistant")

api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    try:
        # إعداد الاتصال بنسخة مستقرة
        genai.configure(api_key=api_key)
        
        # نستخدم 'gemini-1.5-flash' بدون أي إضافات
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        complaint = st.text_area("Patient Scenario:", height=150)
        
        if st.button("Analyze"):
            if complaint:
                with st.spinner('Clinical analysis in progress...'):
                    # نستخدم طريقة توليد مباشرة تضمن تجاوز أخطاء v1beta
                    response = model.generate_content(complaint)
                    st.markdown("### 📋 Recommendations:")
                    st.write(response.text)
            else:
                st.warning("Please enter a case description.")
                
    except Exception as e:
        # إذا ظهر الخطأ، سنعرض رسالة توضح لك كيف تفعل "الفواتير" لو لزم الأمر
        st.error(f"Technical Note: {str(e)}")
        if "404" in str(e):
            st.info("Tip: Try to create a NEW key from Google AI Studio and ensure it's on a 'New Project'.")
