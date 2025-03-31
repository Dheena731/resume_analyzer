import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API Key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API"))

def analyze_resume(resume_text, job_description):
    prompt = f"""
You are an AI resume evaluator. Your task is to analyze the following resume and compare it with the given job description.

### **📜 Resume Summary:**  
{resume_text}  

### **📝 Job Description:**  
{job_description}  

---

### **🔍 AI Analysis:**  
- **Strengths Identified** (Skills, experience, qualifications)  
- **Missing Skills or Gaps**  
- **Improvement Suggestions**  
- **Match Score (0-100%)**  
- **Final Verdict** (Highly Suitable / Suitable / Needs Improvement)  

Your response should be **detailed yet readable**, avoiding rigid templates.
"""

    response = genai.GenerativeModel("gemini-2.0-flash").generate_content(prompt)
    return response.text
