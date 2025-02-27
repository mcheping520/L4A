from flask import Flask, render_template
from data_init import db

app = Flask(__name__)
app.debug = True


@app.route('/data', methods=['GET'])
def show_data():
    # 在下方写你的代码：跳过video集合中的前3条文档
    data = db.video.find().skip(3).limit(3)
    # 跳过video集合中前0条和前113条文档
    data = db.video.find().skip(0).skip(113)
    return render_template('table.html', data=data)
   
 
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8001)
