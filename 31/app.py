from flask import Flask, render_template
import logging
# 从handler中导入user, microblog, quiz, game模块
from handler import user, microblog, quiz, game

# 创建Flask应用
app = Flask(__name__)
app.debug = True
app.secret_key = '123456'

# 配置logging日志
# logging.basicConfig(level=logging.DEBUG,
#                     # 日志写入文件
#                     filename="./app.log")

# 注册user、microblog、quiz、game蓝图
app.register_blueprint(user.bp)
app.register_blueprint(microblog.bp)
app.register_blueprint(quiz.bp)
app.register_blueprint(game.bp)


# 设置404错误处理器
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


# 设置500错误处理器
@app.errorhandler(500)
def server_error(e):
    return render_template('500.html')


# 启动服务器程序
app.run(host='127.0.0.1', port=8000)
