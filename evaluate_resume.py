import openai
import sys
import os

# ← API KEY de OpenAI (más seguro usar variable de entorno, pero puedes pegarla aquí si prefieres)
openai.api_key = os.getenv("OPENAI_API_KEY")
# También puedes usar esta línea si prefieres no usar entorno:
# openai.api_key = "sk-...tu_clave..."

# Lee los argumentos pasados desde UiPath
resume = sys.argv[1]
job_description = sys.argv[2]

def evaluate_candidate(resume, job_description):
    prompt = f"""
    You're a recruiter assistant. Evaluate the following resume against the job description.

    Job Description:
    {job_description}

    Resume:
    {resume}

    Please provide the following:
    1. A match score (0–100).
    2. One paragraph on how well the resume aligns to the job.
    3. One interesting or unique trait about the candidate.
    4. If the match score is below 60, generate a short feedback email in Spanish for the candidate with suggestions to improve.
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Usa GPT-4 si tienes acceso
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=600
    )

    return response.choices[0].message["content"]

try:
    result = evaluate_candidate(resume, job_description)
    print(result)
except Exception as e:
    print(f"❌ Error: {e}")