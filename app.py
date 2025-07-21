from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY") or "ISI_API_KEY_DISINI"

@app.route('/ask', methods=['POST'])
def ask():
    try:
        # Coba parsing JSON
        try:
            data = request.get_json(force=True)
        except Exception as e:
            print("❌ Gagal parsing JSON:", e)
            return jsonify({"error": "Bad JSON format"}), 400

        if not data or "prompt" not in data:
            print("⚠️ Tidak ada prompt")
            return jsonify({"error": "Missing 'prompt' in JSON"}), 400

        prompt = data["prompt"].strip()
        print("🧠 Prompt diterima:", prompt)

        if not prompt:
            return jsonify({"error": "Prompt kosong!"}), 400

        # Kirim ke OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=100
        )

        reply = response.choices[0].message["content"].strip()
        print("✅ Balasan GPT:", reply)

        return jsonify({"reply": reply}), 200

    except Exception as e:
        print("🔥 Exception utama:", str(e))
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET"])
def home():
    return "🟢 Server Flask aktif", 200
