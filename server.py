from flask import Flask, request, render_template, redirect
import os

# Create an instance of the Flask class
app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# Define a route and a view function
# --------------------------------- Home Page -------------------------------- #
@app.route("/")
def hello_world():
    return render_template("index.html")


# ----------------------------- Segregation Guide ---------------------------- #
@app.route("/guide")
def seg_guide():
    return render_template("seg_guide.html")


# -------------------------------- AI Chat bot ------------------------------- #
@app.route("/binify-bot")
def about():
    return render_template("bot.html")


# ---------------------------- AI Waste Classifier --------------------------- #
@app.route("/ai-waste-classifier")
def ai_waste_classifier():
    return redirect("http://localhost:8501/")


# ------------------------------ Upload function ----------------------------- #
@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return "No file part"
    file = request.files["file"]
    if file.filename == "":
        return "No selected file"
    if file:
        filename = file.filename
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        return "File uploaded successfully"


# ------------------------- Run the Flask application ------------------------ #
if __name__ == "__main__":
    app.run(debug=True)
