from flask import Flask, url_for
app = Flask(__name__)

@app.route("/")
def index():
    return app.send_static_file("index.html")
