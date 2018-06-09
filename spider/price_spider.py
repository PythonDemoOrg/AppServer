# -*- coding: UTF-8 -*-

# Filename : price_spider.py
# author by : WeiQi

import urllib
import urllib.request
import json
import datetime
from util import sql_util
from api import third_party_api


class Price(object):
    def __init__(self):
        self.price_url = third_party_api.price_api
        self.user_agent = 'Dalvik/2.1.0 (Linux; U; Android 5.0.1; MX5 Build/LRX22C'
        self.headers = { 'User-Agent' : self.user_agent}

    def getformatdate(self):
        return datetime.datetime.now().strftime("%Y%m%d")

    def getsameindex(self,lastpriceid,pricelist):
        for index in range(len(pricelist)) :
            if(str(pricelist[index]['articleId'])== lastpriceid) :
                return (index)
        return -1

    def formatdate(self,pirceitem):
        pirceitem['putdate']=datetime.datetime.fromtimestamp(pirceitem['putdate']/1000).strftime('%Y%m%d')
        return pirceitem

    def getperprice(self):
        response = urllib.request.urlopen(self.pirce_url)
        pirce = json.loads(response.read())
        pirce=pirce['articleList']
        imagepirce=[]
        for perpirce in pirce :
            detile_url=perpirce['articleUrl']
            response = urllib.request.urlopen(detile_url)
            pircedetile = json.loads(response.read())
            imagemap=pircedetile['articleMediaMap']
            if(len(imagemap)>2) :
                perpirce['imgUrlList'].append(imagemap['img_0']['url'])
                perpirce['imgUrlList'].append(imagemap['img_1']['url'])
                perpirce['imgUrlList'].append(imagemap['img_2']['url'])
            imagepirce.append(perpirce)
             
        return imagepirce

    def save_per_article_content(self,pirce):
        correctpirce=[]
        for perpirce in pirce :
            detile_url=perpirce['articleUrl']
            priceid=perpirce['articleId']
            response = urllib.request.urlopen(detile_url)
            articlecontent={}
            articlecontent['content']=json.loads(response.read())['content']
            try:
                correctpirce.append(perpirce)
                articlecontent=json.dumps(articlecontent).decode("unicode-escape")
                sql_util.newscontent_insert_sql(priceid, articlecontent)
            except:
                continue
        return correctpirce

    def getdailyprice(self):
        date=self.getformatdate()
        pricelist=[]
        pricejsonlist={}
        source=['268_price.json','270_price.json']

        for index in range(2):
            self.price_url = third_party_api.priceapi % (date, source[index]);
            pricelist.extend(self.getperprice())

        pricelist=sorted(pricelist,key=lambda priceitem:priceitem['putdate'],reverse=True)
        latestprice= sql_util.select_latest_price_sql()
        if(latestprice is None) :
            pricejsonlist["nextId"]='0'
            indexofsame=2
        else :
            lastpriceid=latestprice[1]
            pricejsonlist["nextId"]=lastpriceid
            indexofsame =self.getsameindex(lastpriceid,pricelist)
            if((indexofsame is not -1) and (indexofsame is not 0)) :
                pricelist=pricelist[0:indexofsame]
        pricejsonlist["pricelist"]=pricelist
        pricejsonlist=json.dumps(pricejsonlist).decode("unicode-escape")
        if((indexofsame is not 0) and len(pricelist)>8) :
            try:
                sql_util.price_insert_sql('price', str(pricelist[0]['articleId']), pricejsonlist, str(date))
            except:
                return "error"
        return str(pricejsonlist)


