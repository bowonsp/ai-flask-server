from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Ganti dengan API Key kamu, atau ambil dari environment variable
openai.api_key = os.getenv("OPENAI_API_KEY", "YOUR_OPENAI_API_KEY")

@app.route('/ask', methods=['POST'])
def ask():
    try:
        data = request.get_json(force=True)
        prompt = data.get("prompt", "").strip()

        if not prompt:
            return jsonify({"error": "Prompt kosong"}), 400

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Kamu adalah analis teknikal forex yang akurat dan ringkas."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300,
            temperature=0.7
        )

        reply = response.choices[0].message.content.strip()
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Jalankan server di 0.0.0.0 agar Render bisa akses
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
