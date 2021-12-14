from flask import Flask, render_template, request, redirect
import speech_recognition as sr

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
	return "Hello World"

if __name__ == "__main__":
    app.run(debug=True, threaded=True)

