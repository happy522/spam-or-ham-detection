from flask import Flask, redirect, url_for, render_template, request

import pickle

vector = pickle.load(open("vectorizer.pkl", 'rb'))
model = pickle.load(open("finalized_model.pkl", 'rb'))
app = Flask(__name__)
global __predict
__predict = None

@app.route("/")
def home():
    return render_template("index.html")
global usr
usr=0
@app.route("/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]

        __predict = model.predict(vector.transform([user]))[0]
        print(__predict)
        return render_template("index.html", usr=__predict,n=user)

if __name__ == "__main__":
    app.run(debug=True)