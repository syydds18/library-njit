'''
author : anwen
email : anwen758@foxmail.com
description : I want a stable seat
date : 2021-3-11
'''


##################################################################################################
my_cookies = {
    'FROM_TYPE': 'weixin',
    'wechatSESS_ID': '',
    'SERVERID': ''

}

seat_room = ''  # 201,202,302,305,406,510,一楼学生自修室，一楼走廊，二楼走廊，三楼走廊，四楼走廊
seat_where = ''  # 座位号


#####################################如果使用邮箱就修改这三个数据，不用可以不管#######################
epassword = ''  # 如果使用邮箱就修改这三个数据，不用可以不管#######################
hostmail = 'smtp.qq.com'  # 如果使用邮箱就修改这三个数据，不用可以不管#######################
email = '@qq.com'  # 如果使用邮箱就修改这三个数据，不用可以不管#######################
#####################################如果使用邮箱就修改这三个数据，不用可以不管#######################


headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.2(0x18000233) NetType/WIFI Language/zh_CN'}
sum_url = {'reserve_url': '\"https://' + "wechat.v2.traceint.com" + '/index.php/reserve/get/\"',
           'room_url': 'https://wechat.v2.traceint.com/index.php/reserve/index.html?f=wechat',
           'into_room': 'https://wechat.v2.traceint.com/index.php/reserve/layout/libid=',
           'person_url': 'https://wechat.v2.traceint.com/index.php/center.html'}


# room_num={'402科技图书借阅Ⅲ室 (4楼)':'23',
#     '201科技图书借阅Ⅰ室 (2楼)':'29',
#     '202科技图书借阅Ⅱ室 (2楼)':'30',
#     '302社科图书借阅Ⅰ室 (3楼)':'31',
#     '305社科图书借阅Ⅱ室 (3楼)':'32',
#     '406社科图书借阅Ⅲ室 (4楼)':'34',
#     '510信息共享空间 (5楼)':'444',
#     '一楼学生自修室 (一楼)':'20099',
#     '一楼走廊 (一楼)':'20100',
#     '二楼走廊 (二楼)':'20101',
#     '三楼走廊 (三楼)':'20102',
#     '四楼走廊 (四楼)':'20103'}
