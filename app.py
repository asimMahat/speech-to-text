from flask import Flask,render_template,request,redirect
import speech_recognition as sr
from flask import jsonify

app = Flask(__name__)

# @app.route("/", methods=["GET","POST"])
# def upload_file():
#     if request.method == "POST":
#         print("Request received")

#     return render_template('index.html')

@app.route("/", methods=["GET", "POST"])
def index():
    transcript = ""
    if request.method == "POST":
        print("Audio file received")

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)
            
        if file:
            r = sr.Recognizer()
            audio = sr.AudioFile(file)
            with audio as source:
                data = r.listen(source)
            transcript = r.recognize_google(data)
            # for nepali language 
            # transcript = r.recognize_google(data,language ='ne-NP') 
            print(transcript)

    return render_template('index.html', transcript=transcript)

if __name__ == "__main__":
    app.run(debug=True, threaded=True)



