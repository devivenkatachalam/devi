from flask import Flask, render_template, send_file,request, flash
import moviepy.editor
import time,os
app = Flask(__name__)
app.secret_key='secretkey'

@app.route('/')
def form():
    list=['a','b','c','d']
    return render_template('1stpage.html', list=list)








@app.route('/audio_extract', methods=['POST','GET'])
def download_file():
    request_file=request.files['media_file']
    print(request_file)
    request_format=request.form['audio_format']
    print(request_format)
    videoclip = moviepy.editor.VideoFileClip(str(request_file))
    audioclip = videoclip.audio
    # file_name="/static" + "temp_file" + str(time.time()) +".wav"
    file_name='imaginedragon.'+request_format
    audioclip.write_audiofile(file_name)
    file_name = 'imaginedragon.wav'
    flash(file_name)
    return render_template('1stpage.html')


if __name__ == "__main__":
    app.run(debug=True)

