import openai
import streamlit as st

class CoverLetterGenerator:
    def __init__(self, api_key):
        self.client = openai.OpenAI(api_key=api_key)

    def generate_cover_letter(self, job, resume, match, tone):
        prompt = f"""
        Write cover letter:
        Job: {job}
        Resume: {resume}
        Match: {match}
        Tone: {tone}
        """
        try:
            res = self.client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}]
            )
            return res.choices[0].message.content
        except Exception as e:
            st.error(str(e))
            return ""
