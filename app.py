import os
import openai
from flask import Flask, request, jsonify

app = Flask(__name__)

# Gunakan API key dari environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/ask', methods=['POST'])
def ask():
    try:
        data = request.get_json(force=True)  # <--- force=True biar JSON tetap diproses meski ada kesalahan kecil
        prompt = data.get("prompt", "")

        if not prompt:
            return jsonify({"error": "Prompt kosong."}), 400

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=200,
            temperature=0.7
        )
        reply = response["choices"][0]["text"].strip()
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Untuk deploy di Render
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
