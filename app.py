from flask import Flask, render_template
from crawl import map
app = Flask(__name__)


@app.route('/') #��ҳ��
def index():
    return render_template('index.html')

@app.route('/login')    #��¼ҳ��
def login():
    return render_template('login.html')

@app.route('/register')         #ע��ҳ��
def register():
    return render_template('register.html')

@app.route('/release')      #������Դ��Ϣҳ��
def do_release():
    return render_template('release_news.html')

@app.route('/find_house')       #��ѯչʾҳ��
def find_house():
    return render_template('select_information.html')
@app.route('/map')        #��ͼ�ҷ�ҳ��
def do_map():
    map()
    return render_template('map.html')

if __name__ == '__main__':
    app.run()
