import os
import openai
import re
from flask import Flask, request, jsonify

# Ambil API key dari environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Inisialisasi Flask
app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask():
    try:
        # Ambil JSON dari request
        data = request.get_json(force=True)
        prompt = data.get("prompt", "")

        if not prompt:
            return jsonify({"error": "Prompt kosong"}), 400

        # Panggil OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Bisa diganti dengan model lain jika perlu
            messages=[
                {"role": "system", "content": "Kamu adalah analis forex. Jawab HANYA dalam format: TP: x.xxxxx SL: x.xxxxx tanpa penjelasan lain."},
                {"role": "user", "content": prompt}
            ]
        )

        # Ambil hasil jawaban AI
        reply = response["choices"][0]["message"]["content"]

        # 🔧 BERSIHKAN JAWABAN agar tidak mengandung newline/tab/spasi berlebihan
        clean_reply = re.sub(r"\s+", " ", reply).strip()

        # Kirim balik ke EA dalam bentuk JSON
        return jsonify({"reply": clean_reply})

    except Exception as e:
    import traceback
    print("❌ ERROR SAAT MEMPROSES /ask")
    traceback.print_exc()
    return jsonify({"error": str(e)}), 500

# Jalankan server
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Default port 5000
    app.run(host="0.0.0.0", port=port)
