from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

def evaluate_candidate(resume, job_description):
    prompt = f"""
You are an expert in talent acquisition and human resources. Your task is to evaluate whether the following candidate is a good match for the job description provided.

Please:
1. Give a match score from 0 to 100.
2. Briefly explain why the candidate matches or doesn't.
3. Highlight the most interesting or unique aspects of the candidate's background.
4. If the match score is below 60, write a short, professional email response to the candidate with polite and constructive feedback, and general suggestions on how to improve their fit for future opportunities.

### JOB DESCRIPTION:
{job_description}

### CANDIDATE RESUME:
{resume}

Return your response in this format:

Match Score: XX/100
Alignment Comments: ...
Most Interesting Aspects: ...
Suggested Email to Candidate (only if score < 60): ...
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=800
    )

    return response.choices[0].message['content']

@app.route('/evaluate', methods=['POST'])
def evaluate():
    data = request.json
    resume = data.get("resume", "")
    job_description = data.get("job_description", "")

    if not resume or not job_description:
        return jsonify({"error": "Missing resume or job_description"}), 400

    try:
        result = evaluate_candidate(resume, job_description)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

