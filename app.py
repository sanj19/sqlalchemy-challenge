from flask import Flask, jsonify

# use Flask to create an app
app = Flask(__name__)

hello_dict = {"Hello": "World!"}


@app.route("/")
def welcome():
    return (
        f"Welcome to the Temperature Observation API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<end>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    query_results = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= start_date).\
    order_by(Measurement.date).all()

    return jsonify(query_results)


@app.route("/api/v1.0/stations")
def stations():
    station_list = session.query(Station.name, Station.station).all()

    return jsonify(station_list)

@app.route("/api/v1.0/tobs")
def tobs():
    


if __name__ == "__main__":
    app.run(debug=True)