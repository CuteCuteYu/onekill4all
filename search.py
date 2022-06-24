import requests
from bs4 import BeautifulSoup


def search(key):
	#-------------------- 1.获取页面信息 -----------------------
	headers = {
		"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.9999.0 Safari/537.36",
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
		"Accept-Encoding": "gzip, deflate",
		"Accept-Language": "en,es;q=0.9,ja;q=0.8,zh;q=0.7,zh-CN;q=0.6",
	}
	# 咱们在这里直接给定义一个关键词
	baiduweb = requests.get("https://www.baidu.com/s?wd=" + key + "&pn=10",headers = headers)
	baiduweb_text = baiduweb.text

	#-------------------- 2.清洗页面信息 -----------------------
	import json
	# 使用BS4模块
	baidu_soup = BeautifulSoup(baiduweb_text,"html.parser")


	cache_title_list = []
	for cache_title in baidu_soup.find_all(attrs = {"class" : "c-tools tools_47szj"}):
		dt = cache_title["data-tools"]
		dt = dt.replace("'",'"')
		dt = json.loads(dt)

		title = dt.get("title")
		cache_title_list.append(title)
	return cache_title_list


