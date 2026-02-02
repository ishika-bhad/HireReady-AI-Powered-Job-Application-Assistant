import streamlit as st
from utils.file_reader import load_resume
from utils.resume_pdf import generate_updated_resume
from services.job_analyzer import JobAnalyzer
from services.cover_letter import CoverLetterGenerator

def main():
    st.set_page_config(page_title="HireReady", layout="wide")

    api_key = st.sidebar.text_input("OpenAI API Key", type="password")
    if not api_key:
        return

    job_analyzer = JobAnalyzer(api_key)
    cover_gen = CoverLetterGenerator(api_key)

    job_desc = st.text_area("Job Description")
    resume_file = st.file_uploader("Resume", type=["pdf", "docx"])

    if job_desc and resume_file:
        resume_text = load_resume(resume_file)
        job = job_analyzer.analyze_job(job_desc)
        resume = job_analyzer.analyze_resume(resume_text)
        match = job_analyzer.analyze_match(job, resume)

        st.metric("Match", match.get("overall_match_percentage", "0%"))

        if st.button("Generate Cover Letter"):
            letter = cover_gen.generate_cover_letter(job, resume, match, "professional")
            st.text_area("Cover Letter", letter, height=300)

        pdf = generate_updated_resume(resume_text, match)
        st.download_button("Download Resume", pdf, "updated.pdf")

if __name__ == "__main__":
    main()
