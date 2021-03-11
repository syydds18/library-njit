'''
author : anwen
email : anwen758@foxmail.com
description : I want a stable seat
date : 2021-3-11
'''

import requests
import config


def main():
    requests.packages.urllib3.disable_warnings()
    r = requests.get(config.sum_url['room_url'], cookies=config.my_cookies,
                     headers=config.headers, verify=False, timeout=5)
    r.encoding = 'utf-8'
    if '305' in r.text:
        print('alive')


def main_handler(event, context):
    try:
        main()
    except Exception as e:
        raise e
    else:
        return ''


if __name__ == '__main__':
    print(main_handler({}, {}))
