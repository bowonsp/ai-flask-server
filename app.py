from flask import Flask, request, jsonify
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask():
    if not request.is_json:
        return jsonify({"error": "Content-Type harus application/json"}), 415

    data = request.get_json()
    prompt = data.get("prompt", "")
    if not prompt:
        return jsonify({"error": "Prompt kosong"}), 400

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Kamu adalah analis trading forex."},
            {"role": "user", "content": prompt}
        ]
    )

    return jsonify({"reply": response.choices[0].message.content})
