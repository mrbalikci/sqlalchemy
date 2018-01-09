# Import Needy Libraries and Extentions

from flask import Flask, jsonify
import os
import pandas as pd
import json

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Call the SQLite
engine = create_engine('sqlite:///hawaii.sqlite')

# Create the base
Base = automap_base()
Base.prepare(engine, reflect = True)

# Read the tables 
Measurement = Base.classes.measurement
Station = Base.classes.station

# Connect to the engine
session = Session(engine)

# Define app
app = Flask(__name__)

# Opne alrady saved dic files NOTE: These files could be called here by session queries also. 
with open('temp_dates_dict.json', 'r') as fp:
    precipitation_data = json.load(fp)

with open('stations_info_dict.json', 'r') as st:
    stations_data = json.load(st)

with open('prev_year_dict.json', 'r') as pr:
    tobs_data = json.load(pr)

# Create the routes
@app.route("/")

# The welcome page
def welcome():
    return(

        f"Welcome to the Climate Analysis and Exploration of Hawaii! <br/>"

        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation <br/>"
        f"/api/v1.0/stations <br/>"
        f"/api/v1.0/tobs <br/>"
        f"/api/v1.0/<start> <br/>"
        f"/api/v1.0/<start>/<end> <br/>"

        
    )

@app.route("/api/v1.0/precipitation")

def precipitation():
    return jsonify(precipitation_data)

@app.route("/api/v1.0/stations")

def stations():
    return jsonify(stations_data)

@app.route("/api/v1.0/tobs")

def tobs():
    return jsonify(tobs_data)

if __name__=="__main__":
    app.run(debug=True)


