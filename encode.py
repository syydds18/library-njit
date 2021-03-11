'''
author : anwen
email : anwen758@foxmail.com
description : I want a stable seat
date : 2021-3-11
'''

import requests
import re
import execjs
import config
from transfer_seat import *


def encode(a, b):
    js_url = config.sum_url['js_url']
    reserve_url = config.sum_url['reserve_url']

    hexch_js_code = requests.get(
        js_url, cookies=config.my_cookies, headers=config.headers, verify=False, timeout=5)
    hexch_js_code.encoding = 'gbk'
    hexch_js_code = hexch_js_code.text
    hexch_js_code = hexch_js_code.replace('\n', '')
    pattern = re.compile(r'(?<=T\.ajax_get\().*?(?=,)')
    ajax_url = pattern.search(hexch_js_code).group(
        0).replace('AJAX_URL', reserve_url)
    hexch_js_code = re.sub(
        r'T\.ajax_get', 'return %s ; T.ajax_get' % ajax_url, hexch_js_code)
    tmp = execjs.compile(hexch_js_code)
    submint_url = tmp.call('reserve_seat', a, b)
    print('本次提交座位地址', submint_url)
    return submint_url
