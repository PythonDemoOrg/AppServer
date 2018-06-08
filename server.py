# -*- coding: UTF-8 -*-

# Filename : server.py
# author by : WeiQi

from sqlutils import basesqlutil
from spider import price
from util import api
from util import mock_data
from flask import Flask, jsonify, g

app = Flask(__name__)

@app.route(api.add_price, methods=['GET'])
def add_price():
    id=basesqlutil.select_lastest_id_sql()
    print(id)
    try:
        id=id+1,
        title='normal title'
        thumbnail='http://pic4.zhimg.com/aa94e197491fb9c44d384c4747773810.jpg'
        description='description not it'
        done=0
        basesqlutil.price_insert_sql('price', id,title,thumbnail,description,done)
        print('price_insert_sql')
    except:
        print('error')
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

@app.route(api.get_price,methods=['GET'])
def get_prices():
    return jsonify(mock_data.prices)

@app.route(api.get_price,methods=['GET'])
def get_latest_price(type):
    if(type=='price') :
        latestprice =basesqlutil.select_latest_price_sql()
    return latestprice

@app.route(api.load_more_price,methods=['GET'])
def load_more_prices(type,page):
     if(type=='price') :
         load_price =basesqlutil.select_price_by_page_sql(page)
     return str(load_price)

@app.before_request
def before_request():
    basesqlutil.connect()
    global pricedata
    pricedata= price.Price()

@app.errorhandler(404)
def not_found(error):
    return 'nodata'

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'): g.db.close()

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=8080)