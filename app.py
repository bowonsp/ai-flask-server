from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask():
    try:
        # Baca isi JSON dari MT4
        data = request.get_json(force=True)
        print("✅ Data diterima:", data)

        prompt = data.get("prompt", "")
        if not prompt:
            return jsonify({"error": "Prompt kosong"}), 400

        # Kirim balasan dummy sebagai tes koneksi
        return jsonify({"reply": f"Sukses! Prompt yang diterima: '{prompt}'"}), 200

    except Exception as e:
        print("🔥 ERROR:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
