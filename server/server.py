from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'moiss': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    moyenne_saisonniere = float(request.form['moyenne_saisonniere'])
    mois = request.form['mois']
    heures_pleines = float(request.form['heures_pleines'])
    heures_creuses = float(request.form['heures_creuses'])
    heures_de_pointe = float(request.form['heures_de_pointe'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(mois,moyenne_saisonniere,heures_de_pointe,heures_pleines,heures_creuses)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()