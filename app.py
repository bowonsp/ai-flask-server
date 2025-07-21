from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.get_json(force=True)
        prompt = data.get("prompt", "")
        
        # Validasi prompt minimal
        if not prompt or "Harga" not in prompt:
            return jsonify(error="Invalid prompt format"), 400
        
        # Sinyal dummy response (bisa diganti dengan OpenAI API atau model lokal)
        return jsonify(response="TP: 119999.00000 SL: 118000.00000")
    
    except Exception as e:
        return jsonify(error=str(e)), 400
