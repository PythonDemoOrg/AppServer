# -*- coding: UTF-8 -*-

# Filename : api.py
# author by : WeiQi

# restful api
add_price='/api/v1.0/price/add'
delete_price='/api/v1.0/price/delete/<string:priceid>'
update_price='/api/v1.0/<string:type>/update/<string:priceid>'
get_price='/api/v1.0/price/get/<string:priceid>'
load_more_price='/api/v1.0/<string:type>/loadmore/<string:page>'