'''
author : anwen
email : anwen758@foxmail.com
description : I want a stable seat
date : 2021-3-11
'''


import config
import requests
from bs4 import BeautifulSoup
import time


def scan_room():
    list_room = {}
    requests.packages.urllib3.disable_warnings()
    r = requests.get(config.sum_url['room_url'], cookies=config.my_cookies,
                     headers=config.headers, verify=False, timeout=5)
    r.encoding = 'utf-8'
    html = r.text
    # print(html)
    soup = BeautifulSoup(html, 'lxml')
    a_s = soup.find_all('a', attrs={"class": "list-group-item"})
    for a in a_s:
        com = {}
        spc = a.get('data-url').split('=')[1]
        spc = spc.split('.')[0]
        num = a.find('span').text
        room = a.find('h4').text.replace(
            ' ', '').replace(num, '').replace('\t', '')
        com[spc] = num
        list_room[room] = com
    return list_room, html


def scan_seat():
    list_seat = {}
    into_url = config.sum_url['into_room']
    into_url = into_url+config.seat_room+'&'+str(int(time.time()))
    requests.packages.urllib3.disable_warnings()
    r = requests.get(into_url, cookies=config.my_cookies,
                     headers=config.headers, verify=False, timeout=5)
    r.encoding = 'utf-8'
    html = r.text
    # print(html)
    soup = BeautifulSoup(html, 'lxml')
    divs = soup.find_all('div', attrs={"class": "grid_cell"})
    for div in divs:
        list_active = {}
        t = div.text.replace('\n', '').replace(' ', '')
        if t.isdigit():
            if 'grid_active' not in div.get('class'):
                list_active['1'] = div.get('data-key')
                list_seat[t] = list_active
            else:
                list_active['0'] = div.get('data-key')
                list_seat[t] = list_active
    return list_seat, html


def scan_script(html):
    soup = BeautifulSoup(html, 'lxml')
    scripts = soup.find_all('script')
    for script in scripts:
        try:
            if 'layout' in script.get('src') and 'cache' in script.get('src'):
                config.sum_url['js_url'] = script.get('src')
                print('本次加密算法地址', script.get('src'))
                break
        except:
            pass


def scan_person():
    url = config.sum_url['person_url']
    r = requests.get(url, headers=config.headers,
                     cookies=config.my_cookies, verify=False, timeout=5)
    r.encoding = 'utf-8'
    html = r.text
    soup = BeautifulSoup(html, 'lxml')
    name = soup.find('div', class_='nick')
    print('个人信息', name.string)
    return name.text
