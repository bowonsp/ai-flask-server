from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# 🔑 Ganti dengan API key OpenAI kamu
openai.api_key = "OPENAI_API_KEY"

@app.route('/ask', methods=['POST'])
def ask():
    try:
        data = request.get_json(force=True)
        prompt = data.get("prompt", "").strip()

        if not prompt:
            return jsonify({"error": "Prompt kosong"}), 400

        # ✅ Kirim prompt ke OpenAI (gunakan model sesuai kebutuhan)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # atau "gpt-4" jika punya akses
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

if __name__ == '__main__':
    app.run(debug=True)
