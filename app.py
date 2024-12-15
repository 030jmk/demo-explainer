import os  
from flask import Flask, render_template, send_from_directory, url_for  
  
app = Flask(__name__)  
  
ALLOWED_EXTENSIONS = {'mp4', 'mov'}  
  
def allowed_file(filename):  
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS  
  
@app.route('/')  
def index():  
    videos = []  
    for filename in os.listdir('video'):  
        if allowed_file(filename):  
            video_name = filename.rsplit('.', 1)[0]  
            videos.append((filename, video_name))  
    videos.sort(key=lambda x: x[1])  
    return render_template('index.html', videos=videos)  
  
# Changed route to '/play/<filename>'  
@app.route('/play/<filename>')    
def play_video(filename):  
    return render_template('player.html', filename=filename)  
  
# This route can stay the same  
@app.route('/video/<filename>')  
def serve_video(filename):  
    return send_from_directory('video', filename)  
  
if __name__ == "__main__":  
    app.run(debug=True)  
