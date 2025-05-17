from flask import Flask
import os

app = Flask(__name__)

@app.route("/", methods=["GET"]) # NOTE: / =  http://192.168.1.42:5000
def home():
    return render_template("login.html")

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")