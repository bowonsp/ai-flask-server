import os
from flask import Flask, request, jsonify
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json(force=True)  # <= FIX PENTING
    prompt = data.get("prompt", "")
    if not prompt:
        return jsonify({"error": "Prompt kosong"}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {{"role": "system", "content": "Kamu adalah analis trading forex. Jawaban harus mengandung angka eksplisit untuk Take Profit (TP) dan Stop Loss (SL), seperti: TP: 1.1234 dan SL: 1.1200"}},
                {"role": "user", "content": prompt}
            ]
        )
        reply = response.choices[0].message["content"]
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
