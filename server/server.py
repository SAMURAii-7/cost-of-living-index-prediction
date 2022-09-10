from flask import Flask, request, jsonify

app = Flask(__name__)

import util


@app.route("/")
def home():
    return "Hello, welcome to the server!"


@app.route("/cols", methods=["GET"])
def get_col_names():
    response = jsonify({"data_cols": util.get_cols()})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/predict", methods=["POST"])
def predict():
    rent_ind = float(request.form["rent_ind"])
    groceries_ind = float(request.form["groceries_ind"])
    rp_ind = float(request.form["rp_ind"])
    ppi_ind = float(request.form["ppi_ind"])

    response = jsonify(
        {"estimated_coi": util.predict_coi(rent_ind, groceries_ind, rp_ind, ppi_ind)}
    )
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == "__main__":
    print("Starting Python Flask Server for Cost of Living Index Prediction...")
    app.run()
