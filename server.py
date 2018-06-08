# -*- coding: UTF-8 -*-

# Filename : server.py
# author by : WeiQi

from sqlutils import basesqlutil
from spider import price
from util import api
from util import mock_data
from flask import Flask, jsonify, g

app = Flask(__name__)

@app.route('/api/v1.0/prices/update', methods=['GET'])
def price_update():
    price=pricedata.getdailyprice()
    return str(price)

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

@app.route(api.price_update,methods=['GET'])
def get_latest_price(type):
    if(type=='price') :
        latestprice =str(basesqlutil.select_latest_price_sql()[2])
    return latestprice

@app.route(api.price_load_more,methods=['GET'])
def load_more_prices(type,priceid):
     if(type=='priceid') :
         load_price =basesqlutil.select_price_by_id_sql(priceid)
     return str(load_price)

@app.route('/api/v1.0/prices',methods=['GET'])
def get_prices():
    # return jsonify({'prices': prices})
    return jsonify(mock_data.prices)

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=8080)