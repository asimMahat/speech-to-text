from flask import Flask,render_template,request,redirect
import speech_recognition as sr

app = Flask(__name__)
from flask import jsonify


@app.route("/", methods=["GET", "POST"])

def upload_file():
    if request.method == "POST":
        print("Request received")
        return render_template('index.html')
    else :
        return jsonify({"message":"Error password or user not match"})

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
