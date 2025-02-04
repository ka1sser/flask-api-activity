from flask import Flask, jsonify, request, render_template, redirect, url_for
from file_handling import read_csv

app = Flask(__name__)


@app.route('/display-csv')
def display_csv():
    """
    This function will get the dataframe and convert it into dictionary to be displayed as a json.

    Returns:
        jsonified_db (flask.Response): Serialized data as JSON
    """
    db = read_csv()
    jsonified_db = jsonify(db.to_dict(orient="records"))

    
    return jsonified_db


@app.route('/update-csv', methods=["GET", "POST"])
def update_csv():
    if request.method == "POST":
        return redirect(url_for('download'))
        
    return render_template('update.html')

if __name__ == "__main__":
    app.run(debug=True)
