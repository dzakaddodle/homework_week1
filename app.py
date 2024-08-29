#pip install flask
#pip install google-generativeai

from flask import Flask, render_template, request
import google.generativeai as palm
import os

api="AIzaSyC2EAOvZv6N_fD2T-Z_79LykQ7_lX618do"
palm.configure(api_key=api)
#model = palm.GenerativeModel('gemini-1.5-flash')
model = "models/text-bison-001"

app=Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/financial_qn", methods=["GET", "POST"])
def financial_qn():
    return render_template("financial_qn.html")


@app.route("/prediction", methods=["GET", "POST"])
def prediction():
    return render_template("prediction.html")


@app.route("/makersuite", methods=["POST"])
def makersuite():
    q = request.form.get("q")
    if q:
        r = palm.generate_text(prompt=q, model=model)
        return render_template("makersuite.html", r=r.result)
    else:
        return "No prompt provided", 400


@app.route('/joke', methods=["GET", "POST"])
def joke():
    r = palm.generate_text(prompt='singapore joke', model=model)
    return render_template("joke.html", r=r.result)


if __name__ == "__main__":
    app.run()

