import urllib.request

url = 'http://www.whatismyip.com.tw' #输入网址，可以看到自己电脑访问的IP是多少

proxy_support = urllib.request.ProxyHandler({'http':'118.114.250.104:8888'})
opener=urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

print(html)