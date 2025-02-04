from flask import Flask, jsonify, request, render_template, redirect, url_for
import pandas as pd
from file_handling import read_csv, write_csv

app = Flask(__name__)
db = read_csv()


@app.route("/display-csv")
def display_csv():
    """
    This function will get the dataframe and convert it into dictionary to be displayed as a json.

    Returns:
        jsonified_db (flask.Response): Serialized data as JSON
    """
    jsonified_db = jsonify(db.to_dict(orient="records"))

    return jsonified_db


@app.route("/update-csv", methods=["GET", "POST"])
def update_csv():
    """
    This function updates the current csv file by:
        1. Creating a POST request using the "update.html" wherein it takes the values of different keys
        2. Getting the global variable of the csv file
        3. Concatenate the new_data (from the form) to the global variable
        4. Calling write_csv() which overwrites the existing csv file with the new dataframe
            that has the new_data
        5. Redirecting the url for '/display_csv' display_csv() function to display the new dictionary
    """
    if request.method == "POST":

        new_data = {
            "MSIDN": request.form["MSIDN"],
            "EventType": request.form["EventType"],
            "EventDateAndTime": request.form["EventDateAndTime"],
            "ServiceClass": request.form["ServiceClass"],
            "RechargeAmount": request.form["RechargeAmount"],
            "PaymentMethod": request.form["PaymentMethod"],
            "Category": request.form["Category"],
            "Location": request.form["Location"],
        }

        global db

        db = pd.concat([db, pd.DataFrame([new_data])], ignore_index=True)

        write_csv(db)

        return redirect(url_for("display_csv"))

    return render_template("update.html")


if __name__ == "__main__":
    app.run(debug=True)
