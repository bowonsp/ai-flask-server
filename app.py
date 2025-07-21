from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask server is running!"

@app.route('/ask', methods=['POST'])
def ask():
    try:
        data = request.get_json()
        if not data or 'prompt' not in data:
            return jsonify({"error": "Prompt tidak ditemukan"}), 400

        prompt = data['prompt']

        # Dummy response (ganti nanti dengan OpenAI call atau logic lainnya)
        response_text = "TP: 1.12345 SL: 1.11111"

        return jsonify({"response": response_text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=10000)
