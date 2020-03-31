import requests        #导入模块 实现发送数据到服务器

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    #字典类型的
words = {
        'i': 'peace',
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': '15835777995680',
        'sign': '0606526262b1f690c44854551c127515',
        'ts': '1583577799568',
        'bv': '0bbb180f75b7e2f83d7b245ab1b58103',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_CLICKBUTTION}'}

    #加请求头让服务器认识我们
headers = {
        'Accept': 'application / json, text / javascript, * / *; q = 0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie':'OUTFOX_SEARCH_USER_ID=-1730755425@113.73.33.72; OUTFOX_SEARCH_USER_ID_NCOO=138283091.9832873; _ntes_nnid=0eab6c259699556fbc7d53a0c103e5bf,1576483622569; JSESSIONID=aaarzkuqvJxNO6eMDH0cx; ___rl__test__cookies=1583577799567',
        'Host': 'fanyi.youdao.com',
        'Referer': 'http: // fanyi.youdao.com /',
        #这个信息是我们电脑的信息  浏览器信息 浏览器版本等
        'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    }

response = requests.post(url,data=words,headers = headers )
    #a = open(r'C:\Users\George~\Desktop\抓包\wenjian.txt', 'w')
    #a.write(result.text)
    #a.close()
#print(response)

#response.content.decode()    #默认utf-8
#response.content.decode('gbk')    #获取响应文本的格式
#response.text


print(response.content.decode())   #文本的结果
print(type(response.content.decode()))