import requests
import os
import time


def getManyPages(keyword, pages):
    params=[]
    for i in range(30, 30*pages+30, 30):
        params.append({
                      'tn': 'resultjson_com',
                      'ipn': 'rj',
                      'ct': 201326592,
                      'is': '',
                      'fp': 'result',
                      'queryWord': keyword,
                      'cl': 2,
                      'lm': -1,
                      'ie': 'utf-8',
                      'oe': 'utf-8',
                      'adpicid': '',
                      'st': -1,
                      'z': '',
                      'ic': 0,
                      'word': keyword,
                      's': '',
                      'se': '',
                      'tab': '',
                      'width': '',
                      'height': '',
                      'face': 0,
                      'istype': 2,
                      'qc': '',
                      'nc': 1,
                      'fr': '',
                      'pn': i,
                      'rn': 30,
                      'gsm': '1e',
                      '1488942260214': ''
                  })
    url = 'https://image.baidu.com/search/acjson'
    urls = []
    for i in params:
        urls.append(requests.get(url, params=i).json().get('data'))
        time.sleep(1)
        print("当前图片库连接数：", len(urls))
    return urls


def getImg(dataList, localPath):

    if not os.path.exists(localPath):  # 新建文件夹
        os.mkdir(localPath)

    x = 0
    for list in dataList:
        for i in list:
            if None != i.get('thumbURL'):
                print('正在下载：%s' % i.get('thumbURL'))
                ir = requests.get(i.get('thumbURL'))
                open(localPath + '%d.jpg' % x, 'wb').write(ir.content)
                x += 1
            else:
                print('图片链接不存在')
            time.sleep(1)


if __name__ == '__main__':
    dataList = getManyPages('qq头像', 50)  # 参数1:关键字，参数2:要下载的页数
    getImg(dataList, r'D:\1\zhnegchang\\')  # 参数2:指定保存的路径
