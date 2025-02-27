from flask import Flask, render_template
from data_init import db

web = Flask(__name__)
web.debug = True


@web.route('/data', methods=['GET'])
def show_data():
    data = list(db.cartoon.find({}))
    # 请在下方写你代码：使用逻辑或查询作者为动漫堂或者名称为传武的漫画文档
    data = list(db.cartoon.find({'$or': [{'author': '动漫堂'}, {'name': '传武'}]}))

    return render_template('table.html', data=data)


web.run('127.0.0.1', 8002)
