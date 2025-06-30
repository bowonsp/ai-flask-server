import os
import openai
from flask import Flask, request, jsonify

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.get_json(force=True)  # ← penting agar Flask tetap memproses walau tidak perfect Content-Type
        prompt = data.get("prompt", "")

        if not prompt:
            return jsonify({"error": "Prompt kosong"}), 400

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Kamu adalah analis trading forex."},
                {"role": "user", "content": prompt}
            ]
        )

        reply = response['choices'][0]['message']['content']
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
