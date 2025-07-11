from flask import Flask, request, jsonify
from pricing_logic import PricingLogic
from pricing_dao import PricingDao
from db import create_lift_pass_db_connection

app = Flask("lift-pass-api")

# Connexion à la base de données
connection_options = {
    "host": 'localhost',
    "user": 'root',
    "database": 'lift_pass',
    "password": 'mysql'}

db_connection = create_lift_pass_db_connection(connection_options)

# Injection des dépendances
dao = PricingDao(db_connection)
logic = PricingLogic(dao)

@app.route("/pass/price", methods=["POST"])
def get_price():
    data = request.get_json()
    if isinstance(data, dict):
        passes = [data]
    #else:
       # passes = data

    try:
        result = logic.calculate_multiple_prices(passes)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/pass/confirm", methods=["POST"])
def confirm_booking():
    data = request.get_json()
    if isinstance(data, dict):
        passes = [data]
    #else:
        #passes = data

    try:
        logic.confirm_booking(passes)
        return jsonify({"status": "confirmed"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(port=3005)