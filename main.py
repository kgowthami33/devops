from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def main():
    model = {"title":  "Hello Build Trigger2."}
    return render_template("index.html", model=model)