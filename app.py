import streamlit as st
from resume_parser import extract_text_from_resume
from ai_analysis import analyze_resume

# 🛠 Set Page Config
st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

# 🌟 Custom Styling
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

        html, body, [class*="st-"] {
            font-family: 'Poppins', sans-serif;
            background-color: #eef2f3;
            color: #333;
        }

        .title { 
            font-size: 36px; 
            font-weight: 700; 
            color: #004aad; 
            text-align: center; 
            margin-bottom: 10px;
        }
        .subtext { 
            font-size: 18px; 
            text-align: center; 
            color: #666;
            margin-bottom: 20px;
        }
        .stFileUploader {
            border: 2px solid #004aad !important;
            border-radius: 10px !important;
            background-color: white !important;
            padding: 10px;
        }
        .stButton>button {
            background-color: #004aad;
            color: white;
            border-radius: 10px;
            font-size: 18px;
            padding: 12px 20px;
            transition: 0.3s;
            width: 100%;
        }
        .stButton>button:hover { 
            background-color: #002a66; 
            transform: scale(1.02);
        }
        .result-box {
            background: white;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 4px 6px 15px rgba(0,0,0,0.1);
            margin-top: 20px;
            animation: fadeIn 0.5s ease-in-out;
        }
        .score {
            font-size: 28px;
            font-weight: bold;
            text-align: center;
            color: #007bff;
        }
        .highlight {
            color: #ff4d4d;
            font-weight: bold;
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
    </style>
""", unsafe_allow_html=True)

# 🎯 Title & Intro
st.markdown("<div class='title'>📄 AI Resume Analyzer</div>", unsafe_allow_html=True)
st.markdown("<p class='subtext'>Upload your resume and compare it with a job description for AI-powered analysis.</p>", unsafe_allow_html=True)

# 🔹 Layout - File Upload & Job Description Input
col1, col2 = st.columns([1, 1])

with col1:
    uploaded_file = st.file_uploader("📂 Upload Resume (PDF/DOCX)", type=["pdf", "docx"])

with col2:
    job_description = st.text_area("📋 Paste Job Description", placeholder="Enter job details here...", height=200)

# 🚀 Analyze Button
if uploaded_file and job_description:
    if st.button("🔍 Analyze Resume"):
        with st.spinner("Analyzing... ⏳ AI is working on your resume!"):
            resume_text = extract_text_from_resume(uploaded_file) 
            analysis = analyze_resume(resume_text, job_description)

            # 🏆 Stylish Result Box
            st.markdown("<div class='result-box'>", unsafe_allow_html=True)
            st.subheader("📊 AI Resume Analysis")
            st.write(analysis)
            st.markdown("</div>", unsafe_allow_html=True)
else:
    st.warning("⚠️ Please upload a resume and provide a job description before analyzing.")
