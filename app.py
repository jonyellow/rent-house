from flask import Flask, render_template
from crawl import map
app = Flask(__name__)


@app.route('/') #主页面
def index():
    return render_template('index.html')

@app.route('/login')    #登录页面
def login():
    return render_template('login.html')

@app.route('/register')         #注册页面
def register():
    return render_template('register.html')

@app.route('/release')      #发布房源信息页面
def do_release():
    return render_template('release_news.html')

@app.route('/find_house')       #查询展示页面
def find_house():
    return render_template('select_information.html')
@app.route('/map')        #地图找房页面
def do_map():
    map()
    return render_template('map.html')

if __name__ == '__main__':
    app.run()
