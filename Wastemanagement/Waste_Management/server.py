from flask import Flask, request, render_template

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route and a view function
@app.route('/')
def hello_world():
    return render_template( 'index.html' )

@app.route("/guide")
def seg_guide():
    return render_template("seg_guide.html")

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True) 
