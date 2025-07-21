from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '✅ Flask AI Trading API is Running', 200

@app.route('/ask', methods=['POST'])
def ask():
    try:
        data = request.get_json(force=True)
        prompt = data.get("prompt", "")

        if not prompt:
            return jsonify({"error": "Missing prompt"}), 400

        # Simulasi AI Response (ganti bagian ini dengan API OpenAI bila siap)
        response_text = "TP: 1.12500 SL: 1.11500"

        # Validasi format: harus ada "TP:" dan "SL:"
        if "TP:" in response_text and "SL:" in response_text:
            return response_text, 200
        else:
            return jsonify({"error": "Invalid response format"}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
