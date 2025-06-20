from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/ask', methods=['POST'])
def ask():
    try:
        data = request.get_json(force=True)  # Ambil data JSON dari request
        prompt = data.get("prompt", "")

        if not prompt:
            return jsonify({"error": "Prompt kosong."}), 400

        # Buat permintaan ke OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # model aktif (ganti kalau kamu pakai GPT-4)
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=100,
            temperature=0.7
        )

        reply = response["choices"][0]["message"]["content"].strip()
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Bagian WAJIB AGAR TERDETEKSI OLEH RENDER
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # ambil port dari Render
    app.run(host="0.0.0.0", port=port)        # listen ke semua IP, agar Render bisa konek
