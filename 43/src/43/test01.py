from flask import Flask, render_template
from data_init import db

app = Flask(__name__)
app.debug = True


@app.route('/data', methods=['GET'])
def show_data():
    # 在下方写你的代码：查询apps集合中的所有文档，并要求按照"ranking"字段值大小进行升序排序
    data = list(db.apps.find().sort('ranking', 1))

    # 获取渠道"应用宝"中"阅读"类别下的5条文档
    data = list(db.apps.find({'channel': '应用宝','category': '阅读'}).limit(5))

    # 获取渠道"应用宝"中"视频"类别下的文档，按照排名"ranking" 降序排列的10条文档
    data = list(db.apps.find({'category': '视频'}).sort('ranking', -1).limit(10))

    return render_template('table.html', data=data)


app.run(host='127.0.0.1', port=8001)
