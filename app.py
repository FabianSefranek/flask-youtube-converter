from flask import Flask, send_file, request, render_template, url_for
from functions import download_audio, download_video
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", error=False)

@app.route("/download", methods=["POST"])
def downloadAudio():
    try:
        url = request.form["url"]
        type = request.form["type"]
        if type=="mp3":
            return send_file(download_audio(url), as_attachment=True)
        elif type=="mp4":
            return send_file(download_video(url), as_attachment=True)
        else:
           return render_template("index.html", error=True)
    except Exception:
        return render_template("index.html", error=True)
    


if __name__ == "__main__":
    app.run(debug=True)