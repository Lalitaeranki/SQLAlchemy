from flask import Flask,jsonify
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine,func
import pandas as pd
from datetime import datetime
import datetime as dt
############################################
# Database Setup
############################################
engine=create_engine("sqlite:///Resources/hawaii.sqlite")
Base=automap_base()
Base.prepare(engine,reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)
############################################
# Flask Setup
############################################
app=Flask(__name__)
############################################
#Flask Routes
############################################
@app.route("/")
def welcome():
   """List all available routes"""
   return(
       f"Available Routes:<br/>"
       f"/api/v1.0/precipitation</br/>"
       f"/api/v1.0/stations<br/>"
       f"/api/v1.0/tobs<br/>"
       f"/api/v1.0/<start><br/>"
       f"/api/v1.0/<start>/<end>"
   )
   @api.route("/api/v1.0/precipitation")
   def precipitation():
       """Return the JSON representation of Precipitation"""
       most_recent = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
       year_ago=dt.date(2017, 8, 23)-dt.timedelta(days=365)

        # Perform a query to retrieve the data and precipitation scores # Sort the dataframe by date

       data_precipitation=session.query(Measurement.date,Measurement.prcp).\
       filter(Measurement.date>=year_ago).\
       order_by(Measurement.date).all()
       precipitation_result=list(np.ravel(data_precipitation))
       return jsonify(precipitation_result)

if __name__ == '__main__':
    app.run(debug=True)
