# -*- coding: UTF-8 -*-

# Filename : api.py
# author by : WeiQi

# restful api
add_price='/api/v1.0/price/add'
delete_price='/api/v1.0/price/delete/<string:priceid>'
update_price='/api/v1.0/<string:type>/update/<string:priceid>'
get_price='/api/v1.0/price/get/<string:priceid>'
load_more_price='/api/v1.0/<string:type>/loadmore/<string:page>'

# download file
open_upload='/api/v1.0/open/upload/'
upload_file='/api/v1.0/upload/file'
download_file='/api/v1.0/download/file/<string:filename>'

# download file sample url
# http://192.168.0.101:8080/api/v1.0/download/file/1528648392.apk
# http://0.0.0.0:8080/api/v1.0/upload/file
# http://0.0.0.0:8080/api/v1.0/open/upload
