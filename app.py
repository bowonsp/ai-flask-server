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
        # Misalnya: Pair: EURUSD, Timeframe: H1, Arah: BUY, Harga: 1.12000
        # Maka AI seharusnya balas: TP: 1.12500 SL: 1.11500
        response_text = "TP: 1.12500 SL: 1.11500"

        # Pastikan format benar
        if "TP:" in response_text and "SL:" in response_text:
            return response_text, 200
        else:
            return jsonify({"error": "Invalid response fo
