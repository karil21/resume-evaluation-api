from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "✅ API is running!"

@app.route("/evaluate", methods=["POST"])
def evaluate():
    data = request.json
    resume = data.get("resume", "")
    job_description = data.get("job_description", "")
    
    if not resume or not job_description:
        return jsonify({"error": "Missing resume or job_description"}), 400

    return jsonify({
        "message": "✅ API received your data!",
        "resume_preview": resume[:50],
        "job_description_preview": job_description[:50]
    })

# 🔥 ESTA PARTE es lo que hace que funcione en Railway
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
