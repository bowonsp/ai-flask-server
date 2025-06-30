import os
import openai
from flask import Flask, request, jsonify

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.get_json(force=True)
        prompt = data.get("prompt", "").strip()
        if not prompt:
            return jsonify({"error": "Prompt kosong"}), 400

        system_message = (
            "Kamu adalah analis forex. Jawabanmu hanya boleh dalam format:\n"
            "TP: x.xxxxx SL: x.xxxxx\n"
            "Gunakan 5 digit desimal (misal: 1.10500), sesuai format harga forex standar seperti EURUSD.\n"
            "Jangan sertakan penjelasan tambahan atau kalimat lainnya."
        )

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ]
        )

        reply = response["choices"][0]["message"]["content"]
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
