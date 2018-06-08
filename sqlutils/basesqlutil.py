# -*- coding: UTF-8 -*-

# Filename : basesqlutil.py
# author by : WeiQi

from imp import reload
import pymysql
from flask import g
import sys
reload(sys)

def connect():
    status=0
    try:
        g.db = pymysql.connect(
            host='localhost',
            port=3306,
            user='huangweiqi',
            passwd='123456',
            db='app_server',
            charset='utf8')
        g.db.ping(True)
        dbc=g.db.cursor()
        g.db.set_character_set('utf8')
        dbc.execute('SET NAMES utf8;')
        dbc.execute('SET CHARACTER SET utf8;')
        dbc.execute('SET character_set_connection=utf8;')
    except Exception as e:
        status=1
    return status

def price_insert_sql(table_name,id,title,thumbnail,description,done):
    c = g.db.cursor()
    sql ="insert into %s (title,thumbnail,description) VALUES (\'%s\',\'%s\',\'%s\')" % (table_name,title,thumbnail,description)
    c.execute(sql)

def price_content_insert_sql(id,content):
    c = g.db.cursor()
    sql ="insert into price (id,content) VALUES ('%s','%s')" % (id,content)
    c.execute(sql)

def select_latest_price_sql():
    c = g.db.cursor()
    sql ="select * from price order by id DESC limit 1"
    c.execute(sql)
    price=c.fetchone()
    return price

def select_price_by_page_sql(page):
    c = g.db.cursor()
    sql ="select * from price where id <%s" %(page*10)
    c.execute(sql)
    prices=c.fetchone()
    return prices

def select_lastest_id_sql():
    c = g.db.cursor()
    sql ="select * from price order by id DESC limit 1"
    c.execute(sql)
    price=c.fetchone()
    return price[0]

def select_price_by_id_sql(priceid):
    c = g.db.cursor()
    sql ="select * from price where id =%s" %(priceid)
    c.execute(sql)
    price=c.fetchone()
    return str(price[2])

def delete_sql(table_name):
    c = g.db.cursor()
    c.execute('delete from %s'%(table_name))