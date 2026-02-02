import openai, json
import streamlit as st

class JobAnalyzer:
    def __init__(self, api_key):
        self.client = openai.OpenAI(api_key=api_key)

    def analyze_job(self, job_description):
        prompt = f"Analyze job and return JSON:\n{job_description}"
        try:
            res = self.client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}]
            )
            return json.loads(res.choices[0].message.content)
        except Exception as e:
            st.error(str(e))
            return {}

    def analyze_resume(self, resume_text):
        prompt = f"Analyze resume and return JSON:\n{resume_text}"
        try:
            res = self.client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}]
            )
            return json.loads(res.choices[0].message.content)
        except Exception as e:
            st.error(str(e))
            return {}

    def analyze_match(self, job, resume):
        prompt = f"Compare and return JSON\nJob:{job}\nResume:{resume}"
        try:
            res = self.client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}]
            )
            return json.loads(res.choices[0].message.content)
        except Exception as e:
            st.error(str(e))
            return {}
