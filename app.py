from flask import Flask, jsonify
import os
import pandas as pd
import json

app = Flask(__name__) 

with open('temp_dates_dict.json', 'r') as fp:
    precipitation_data = json.load(fp)

with open('stations_info_dict.json', 'r') as st:
    stations_data = json.load(st)


@app.route("/")

def welcome():
    return (

        f"Welcome to the Climate Analysis and Exploration of Hawaii! <br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation <br/>"
        f"/api/v1.0/stations <br/>"
        f"/api/v1.0/tobs <br/>"
        f"/api/v1.0/<start> <br/>"
        f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")

def precipitation():
    return jsonify(precipitation_data)

@app.route("/api/v1.0/stations")

def stations():
    return jsonify(stations_data)

if __name__=="__main__":
    app.run(debug=True)


