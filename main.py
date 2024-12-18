
from flask import Flask, flash, redirect, render_template, request, session



# Configure application
app = Flask(__name__)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    if request.method == "GET":
        return render_template("index.html")

#app.run(host='0.0.0.0', port=3000)


