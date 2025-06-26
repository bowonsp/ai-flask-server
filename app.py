from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask():
    try:
        data = request.get_json(force=True)
        print("📩 Data diterima:", data)

        # Contoh respon ke MT4
        return jsonify({
            "status": "success",
            "received": data
        }), 200

    except Exception as e:
        print("❌ Error:", str(e))
        return jsonify({"error": str(e)}), 400
