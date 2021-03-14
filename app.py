from flask import Flask, request,render_template
import logging
import jsonify

from api.Google import youtube

app = Flask(__name__)


@app.route('/')
def hello_world():
    #youtubeComment = youtube.GetCommentList("apIbXjVp8NU")
    return 'Hello World!'

@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/index/videoid',methods=['GET'])
def test():
    #logging.info("GET Request")
    videoId = request.args.get('id')
    youtubeComment = youtube.GetCommentList(videoId)

    print(youtubeComment.to_html())

    return render_template('index.html',  tables=[youtubeComment.to_html(classes='data')], titles=youtubeComment.columns.values)
    #return youtubeComment.to_html()


if __name__ == '__main__':
    app.run()
