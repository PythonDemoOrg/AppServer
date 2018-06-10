# -*- coding: UTF-8 -*-

# Filename : server.py
# author by : WeiQi

import os
import time
from werkzeug.utils import secure_filename
from util import sql_util
from spider import price_spider
from api import api
from data import mock_data
from data import handle_data
from flask import Flask, jsonify, g, request, send_from_directory, render_template

app = Flask(__name__)
UPLOAD_FOLDER = 'upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
basedir = os.path.abspath(os.path.dirname(__file__))
ALLOWED_EXTENSIONS = set(['txt', 'png', 'jpg', 'xls', 'JPG', 'PNG', 'gif', 'GIF', 'apk', 'APK'])

# 用于判断文件后缀
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# 用于测试上传，稍后用到
@app.route(api.open_upload)
def upload_test():
    return render_template('upload.html')

# 上传文件
@app.route(api.upload_file, methods=['POST'], strict_slashes=False)
def api_upload():
    file_dir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    f = request.files['myfile']  # 从表单的file字段获取文件，myfile为该表单的name值
    if f and allowed_file(f.filename):  # 判断是否是允许上传的文件类型
        fname = secure_filename(f.filename)
        print(fname)
        ext = fname.rsplit('.', 1)[1]  # 获取文件后缀
        unix_time = int(time.time())
        new_filename = str(unix_time) + '.' + ext  # 修改了上传的文件名
        f.save(os.path.join(file_dir, new_filename))  # 保存文件到upload目录
        # token = base64.b64encode(new_filename)
        # print(token)
        return jsonify({"errno": 0, "errmsg": "上传成功", "new_filename": new_filename})
    else:
        return jsonify({"errno": 1001, "errmsg": "上传失败"})

@app.route(api.download_file)
def download(filename):
    if request.method=="GET":
        if os.path.isfile(os.path.join('upload', filename)):
            return send_from_directory('upload',filename,as_attachment=True)
        os.abort(404)

@app.route(api.add_price, methods=['GET'])
def add_price():
    try:
        bean= mock_data.Bean().mock_bean()
        sql_util.price_insert_sql('price', bean)
    except:
        return handle_error("error")
    price=get_latest_price('price')
    return handle_data.make_up(price);

@app.route(api.delete_price, methods=['GET'])
def delete_price():
    return jsonify(mock_data.prices)

@app.route(api.update_price, methods=['GET'])
def price_update():
    price = pricedata.getdailyprice()
    return str(price)

@app.route(api.get_price, methods=['GET'])
def get_prices():
    return jsonify(mock_data.prices)

@app.route(api.get_price, methods=['GET'])
def get_latest_price(type):
    if(type=='price') :
        latestprice = sql_util.select_latest_price_sql()
        return latestprice
    return handle_error('arg')

@app.route(api.load_more_price, methods=['GET'])
def load_more_prices(type,page):
     if(type=='price') :
         load_price = sql_util.select_price_by_page_sql(page)
         return handle_data.add_header(load_price)
     return handle_error('arg')

@app.errorhandler(404)
def handle_error(error):
    if (error=='404'):
        return '404'
    if (error=='arg'):
        return 'argument error!!!'
    return 'server internal error!!!'

@app.before_request
def before_request():
    sql_util.connect()
    global pricedata
    pricedata= price_spider.Price()

@app.teardown_request
def teardown_request(exception):
    print(exception)
    if hasattr(g, 'db'):
        g.db.close()

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=8080)