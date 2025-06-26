from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")  # pastikan API key sudah benar

@app.route('/ask', methods=['POST'])
def ask():
    try:
        data = request.get_json(force=True)

        # Tangkap input dari EA
        model = data.get("model", "gpt-3.5-turbo")  # default jika kosong
        prompt = data.get("prompt", "")
        max_tokens = data.get("max_tokens", 100)

        if not prompt:
            return jsonify({"error": "Prompt kosong"}), 400

        # Jalankan OpenAI Completion
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=0.7
        )

        reply = response.choices[0].text.strip()
        return jsonify({"reply": reply})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
