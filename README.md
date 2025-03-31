# 📄 AI Resume Analyzer (Streamlit)  

**AI Resume Analyzer** is a smart tool that evaluates resumes by extracting key information and comparing it against a job description. It leverages **Google Gemini AI API** for analysis and provides insights on suitability, missing skills, and recommendations.  

## 🚀 Features  
✔ Upload resumes in **PDF/DOCX** format  
✔ Extracts text from resumes using **PDFPlumber & python-docx**  
✔ Compares resume content with a **job description**  
✔ Uses **Google Gemini AI API** for deep analysis  
✔ Provides a **match score (0-100%)** and improvement suggestions  
✔ Simple & user-friendly **Streamlit UI**  

## 📌 Tech Stack  
- **Frontend**: Streamlit  
- **Backend**: Google Gemini AI API  
- **Parsing**: PDFPlumber, python-docx  
- **Environment Management**: Python-dotenv  
- **Deployment**: Can be hosted on Streamlit Sharing or other cloud services  

---

## 📂 Project Structure  

📁 resume_analyzer  
│── 📄 app.py                # Main Streamlit app  
│── 📄 ai_analysis.py        # AI-based resume analysis  
│── 📄 resume_parser.py      # Resume text extraction  
│── 📄 .env                  # API Key for Gemini AI  
│── 📄 requirements.txt      # Dependencies  
└── 📄 README.md             # Documentation  


🎯 Usage

 - 1️.Upload your resume (PDF/DOCX)
 - 2.Paste the job description
 - 3️.Click Analyze Resume
 - 4️.View detailed insights, including match score and improvement areas

🛠️ Future Improvements

🔹 Migrate to a Full-Stack app with React & FastAPI

🔹 Improve UI/UX with better design elements

🔹 Add resume ranking for multiple candidates

🔹 Deploy as a web service

🤝 Contributing
Feel free to fork this repo, suggest improvements, or raise issues! 🚀

