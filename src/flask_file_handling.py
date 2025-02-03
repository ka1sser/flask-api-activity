import os
from flask import Flask, request, jsonify, send_file
import pandas as pd
import config as conf


app = Flask(__name__)
config = conf.import_config()
file = conf.import_file_path(config)


@app.route("/read-csv", methods=["GET"])
def read_csv():
    """
    This function reads the csv file

    Returns:
        df (pandas.dataFrame): Returns the dataframe from the CSV file
    """

    assert os.path.isfile(file)
    df = pd.read_csv(file)

    return jsonify(df.to_dict(orient="records"))


@app.route("/update-csv", methods=["POST"])
def update_csv():
    if not os.path.exists(file):
        return jsonify({"Error": "CSV file not found!"}), 404

    df = pd.read_csv(file)
    new_data = request.json

    if not isinstance(new_data, list):
        return (
            jsonify({"error": "Invalid data format! Send a list of dictionaries."}),
            404,
        )

    new_df = pd.DataFrame(new_data)
    df = pd.concat([df, new_df], ignore_index=True)

    df.to_csv(file, index=False)
    return jsonify({"message": "CSV updated successfully!", "new_data": new_data})


@app.route("/download-csv", methods=["GET"])
def download_csv():

    if not os.path.exists(file):
        return jsonify({"error": "CSV file not found!"}), 404

    return send_file(file, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
