# -*- coding: UTF-8 -*-

# Filename : server.py
# author by : WeiQi

from util import sql_util
from spider import price_spider
from api import api
from data import mock_data

from flask import Flask, jsonify, g

app = Flask(__name__)

@app.route(api.add_price, methods=['GET'])
def add_price():
    try:
        bean= mock_data.Bean().mock_bean()
        sql_util.price_insert_sql('price', bean)
    except:
        return "error"
    price=get_latest_price('price')
    return mock_data.make_up(price);

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

@app.route(api.load_more_price, methods=['GET'])
def load_more_prices(type,page):
     if(type=='price') :
         load_price = sql_util.select_price_by_page_sql(page)
     return str(load_price)

@app.before_request
def before_request():
    sql_util.connect()
    global pricedata
    pricedata= price_spider.Price()

@app.errorhandler(404)
def not_found(error):
    return 'nodata'

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'): g.db.close()

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=8080)