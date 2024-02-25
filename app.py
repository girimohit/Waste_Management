from flask import Flask, request, render_template, redirect
from models import db, VehicleData
from flask_migrate import Migrate
import os


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///waste_management.db"
db.init_app(app)
migrate = Migrate(app, db)


# --------------------------------- Home Page -------------------------------- #
@app.route("/")
def hello_world():
    return render_template("index.html")


# ----------------------------- Segregation Guide ---------------------------- #
@app.route("/guide")
def seg_guide():
    return render_template("seg_guide.html")


# ---------------------------- Dump Zone Function ---------------------------- #
@app.route("/dump-zone", methods=["GET", "POST"])
def dump_zone():
    return render_template("dump_zone.html")


# ------------------------------ Vehicle Support ----------------------------- #
@app.route("/vehicle-support", methods=["GET", "POST"])
def vehicle_support():
    if request.method == "POST":
        name = request.form.get("name")
        location = request.form.get("location")
        contact = request.form.get("contact_num")

        vehicleData = VehicleData(name=name, location=location, contact=contact)
        db.session.add(vehicleData)
        db.session.commit()
        return redirect("/vehicle-support")

    prevData = VehicleData.query.all()
    for i in prevData:
        print(i.name)
        print(i.location)
        print(i.contact)
    return render_template("vehicle_support.html", vehicle_data = prevData)


# -------------------------------- AI Chat bot ------------------------------- #
@app.route("/binify-bot")
def about():
    return render_template("bot.html")


# ---------------------------- AI Waste Classifier --------------------------- #
@app.route("/ai-waste-classifier")
def ai_waste_classifier():
    return redirect("http://localhost:8501/")


# ------------------------- Run the Flask application ------------------------ #
if __name__ == "__main__":
    app.run(debug=True)
