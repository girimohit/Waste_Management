from flask import Flask, request, render_template, redirect
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


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
