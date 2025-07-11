from flask import Flask, request, jsonify
from gestion.gestion_operations import effectuer_action

app = Flask(__name__)

@app.route('/action', methods=['POST'])
def action_ferme():
    data = request.json
    champ_id = data.get("champ_id")
    action = data.get("action")
    result = effectuer_action(champ_id, action)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)