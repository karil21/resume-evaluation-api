import openai

def evaluate(resume, job_description, api_key):
    openai.api_key = api_key

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
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=600
    )

    return response.choices[0].message["content"]
