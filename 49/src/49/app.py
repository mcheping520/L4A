from flask import Flask, render_template, jsonify, request
from data import data_init
import pymongo

client = pymongo.MongoClient('127.0.0.1', 27017)
db = client['movies']

app = Flask(__name__)

app.debug = True

with app.app_context():
    data_init.data_local()


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


# 高分推荐总页数
@app.route('/pages', methods=['GET'])
def get_page():
    # 在下方写你的代码：获取 score 集合中的电影数量
    movie_count = db.score.count_documents({})
    # 计算总页数
    total_pages = (movie_count + 9) // 10
    # 返回响应
    return jsonify(total_pages)


# 高分推荐
@app.route('/score', methods=['GET'])
def get_score():
    # 在下方写你的代码：获取页数page
    page = int(request.args.get('page'))
    # 按豆瓣评分降序排序并分页展示10条文档
    movies = list(db.score.find().sort('rate', -1).skip((page - 1) * 10).limit(10))

    # 将ObjectId对象转成字符串
    for d in movies:
        d['_id'] = str(d['_id'])

    # 返回 JSON 格式响应
    return jsonify(movies)


app.run('127.0.0.1', 8000)
