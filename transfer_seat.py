'''
author : anwen
email : anwen758@foxmail.com
description : I want a stable seat
date : 2021-3-11
'''

import config
import scan
import requests
import json
import time


def change_room(seat_room_old):
    flag = 0
    list_room, html = scan.scan_room()
    # print(list_room)
    for i in list_room:  # config.room_num:
        if str(seat_room_old) in i:
            for x in list_room[i]:
                seat_room = x
            print(seat_room_old, '-->', seat_room)
            flag = 1
            break
        else:
            if str(seat_room_old) in list_room[i]:
                seat_room = seat_room_old
                flag = 1
                break
    # print(flag)
    if flag == 0:
        print('自习室选择错误,或者已经选了座位。')
        exit(-1)

    return seat_room, html, list_room


def change_seat(seat_where_old):
    list_seat, html = scan.scan_seat()
    if ',' not in seat_where_old:
        seat_where = list_seat[config.seat_where]
        try:
            seat_where = seat_where['0']
        except:
            seat_where = seat_where['1']
        print(seat_where_old, '-->', seat_where)
    else:
        seat_where = seat_where_old

    return seat_where, html, list_seat


def submit(a):

    requests.packages.urllib3.disable_warnings()
    # now=int(time.time())
    # SERVERID=config.my_cookies['SERVERID'].split('|')
    # config.my_cookies['SERVERID']=SERVERID[0]+'|'+str(now)+'|'+SERVERID[2]
    # config.headers['Accept']='application/json, text/javascript, */*; q=0.01'
    # config.headers['X-Requested-With']='XMLHttpRequest'
    # config.headers['Sec-Fetch-Mode']='cors'
    # config.headers['Sec-Fetch-Site']='same-origin'
    # config.headers['Referer']='http://wechat.v2.traceint.com/index.php/reserve/layout/libid={}.html'.format(config.seat_room)
    # config.headers['Accept-Encoding']='gzip, deflate,br'
    # config.headers['Accept-Language']='zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'

    # print(a)
    # print(config.my_cookies)
    # print(config.headers)
    time.sleep(1)
    r = requests.get(a, headers=config.headers,
                     cookies=config.my_cookies, verify=False, timeout=5)
    r.encoding = 'utf-8'
    r = json.loads(r.text)
    print(r['msg'])
    return r['msg']
