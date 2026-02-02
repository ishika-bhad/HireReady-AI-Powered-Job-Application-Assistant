# HireReady – AI-Powered Job Application Assistant
HireReady is a full-stack AI application designed to automate and optimize the job application process. It leverages large language models (LLMs) to semantically analyze job descriptions and candidate resumes, identify skill gaps, compute match scores, and generate professional application documents in real time.

The system transforms unstructured documents into structured intelligence, enabling data-driven resume optimization and personalized cover letter generation.

## Key Features

### Resume Parsing
- Supports PDF and DOCX formats
- Extracts and normalizes raw resume text

### Job Description Analysis
- Identifies required technical skills, soft skills, experience level, and technologies
- Extracts industry and role-level metadata

### Semantic Matching Engine

- Computes resume-to-job alignment
- Detects missing skills and optimization opportunities
- Generates ATS-focused recommendations

### Automated Resume Generator
- Produces ATS-optimized PDF resumes
- Adds structured formatting and keyword enhancements

### AI Cover Letter Generator
- Generates role-specific cover letters
- Supports multiple tones (professional, confident, enthusiastic)

### Interactive Dashboard
- Skill gap visualization
- Match metrics and recommendations
- Real-time document downloads
## Technical Architechture
Document Ingestion → LLM Analysis → Semantic Matching → Optimization Engine → PDF / Text Generation → Streamlit UI

## Installation
### 1. Clone repository
```bash
git clone https://github.com/your-username/HireReady.git
cd HireReady
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```
## Running the Application
```bash
streamlit run app.py
```

## Usage

### 1.Enter your OpenAI API key
### 2.Paste the job description
### 3.Upload your resume
### 4.View:
  - Match analysis
  - Recommendations
  - Skill gap chart
### 5.Generate:
   - Cover letter
   - Updated resume PDF
