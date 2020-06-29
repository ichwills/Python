def get():
    import random
    from urllib import request
    import re
    from bs4 import BeautifulSoup
    num = random.randint(14, 240)
    html = str('http://www.gaoxiaogif.cn/gif-'+str(num)+'.html')
    data = request.Request(html)
    data.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0')
    data = request.urlopen(data)
    print('Status:', data.status, data.reason)
    html = (data.read().decode('utf-8'))
    html = BeautifulSoup(html,'lxml')
    html = html.prettify()
    data = (re.findall('[a-zA-z]+://[^\s]*', html))
    data = (data[2])
    print(data)
    data = str(data)
    data = data[0:-3]
    print(data)
    data = request.Request(data)
    data.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0')
    data = request.urlopen(data)
    print('Status:', data.status, data.reason)
    gif = data.read()
    with open("gif.gif","wb")as f:
        f.write(gif)

