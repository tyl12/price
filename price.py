#!/usr/bin/python
import urllib
#import urllib.request
def get_price(name_code):
    #print name_code
    if name_code[0] == '-':
        print(name_code[1])
        return

    name_eng = name_code[0]
    code = name_code[1]

    url = 'http://hq.sinajs.cn/?list=%s' % code
    proxies = {'http': 'http://proxy.cd.intel.com:911'}
    urlhandle = urllib.urlopen(url, proxies=proxies)
    content = urlhandle.read()
    #print content
    #return

    #str = content.decode('gbk')
    str = content
    data = str.split('"')[1].split(',')
    full_name = "%-6s" % data[0]
    #print data

    name_net = full_name[0]
    name_eng = "%-10s" % name_eng
    price_current = "%-6s" % float(data[3])
    change_percent = ( float(data[3])-float(data[2]) )*100 / float(data[2])
    change_percent = "%-6s" % round (change_percent, 2)
    print( name_eng + ": range= "+change_percent+" , price= " + price_current);
    #print( name_net + ": range= "+change_percent+" , price= " + price_current);

def get_all_price(code_list):
    for code in code_list:
        get_price(code)


code_list = [
        ["SH",'sh000001'],
        ["ETF50",'sh510050'],
        ["ZZ500",'sz399905'],
        ['-','-'*5],
        ["JiaoTong",'sh601328'],
        ["WaiGQ",'sh600648'],
        ["FangZheng",'sh601901'],
        ["ShangYiYao",'sh601607'],
        ]
'''
        ['-','-'*5],
        ["ETF300",'sh510300'],
        ["YiHua",'sz000422'],
        ["LianTong",'sh600050'],
        ["WuGang",'sh600005'],
        ["PianZH",'sh600436'],
        ["MuYuan",'sz002714'],
        ["GuangDa",'sh601818'],
        ["YuanYang",'sh601919'],
        ["ChangHong",'sh600839'],
        ["GuoJin",'sh600109'],
        ["GuoYuan",'sz000728'],
        ["TianQi",'sz002009'],
        ["PingZhuang",'sz000780'],
        ["ZhangJiang",'sh600895'],
        ['-','-'*5],
        ["ChuanYe",'sz399006'],
        ["ZhongChe",'sh601766'],
        ]
        '''

#["ZhaoHang",'sh600036'],

get_all_price(code_list)

