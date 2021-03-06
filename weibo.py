import requests
from urllib.parse import urlencode
from pyquery import PyQuery as pq

base_url = 'https://m.weibo.cn/api/container/getIndex?'
headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/1958015870',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',  # 设置请求为Ajax
}
max_page = 10


# 模拟Ajax请求
def get_page(page,value):
    params = {
        'type': 'uid',
        'value': value,
        'containerid': '107603'+value,
        'page': page
    }
    url = base_url + urlencode(params)  # 合成完整的URL
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:  # 判断响应的状态码
            return response.json(), page
    except requests.ConnectionError as e:
        print('Error', e.args)


# 解析并提取信息
def parse_page(json, page: int):
    if json:
        items = json.get('data').get('cards')
        for index, item in enumerate(items):
            if page == 1 and index == 1:
                continue
            else:
                item = item.get('mblog', {})
                weibo = {}
                weibo['id'] = item.get('id')
                weibo['正文'] = pq(item.get('text')).text()  # 借助pyquery去掉正文中的HTML
                weibo['点赞'] = item.get('attitudes_count')
                weibo['评论'] = item.get('comments_count')
                weibo['转发'] = item.get('reposts_count')
                yield weibo


def crapy(value):
    for page in range(1, max_page + 1):
        json = get_page(page,value)
        results = parse_page(*json)
        doc = open("output.txt", "a", encoding='utf8')
        for result in results:
            print(result, file=doc)
        doc.close()
    f = open("output.txt","r",encoding="utf-8")
    content = f.readlines()
    li = []

    for decontent in content:
        dic = {}
        print(decontent)
        dic.update(eval(decontent))
        f.close()
        f = open("output.txt","w")
        f.write("")
        f.close()
        li.append(dic)

    for i in li :
        print(i['正文'])
    return li