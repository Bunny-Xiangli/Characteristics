import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# import ssl
#
# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     # Legacy Python that doesn't verify HTTPS certificates by default
#     pass
# else:
#     # Handle target environment that doesn't support HTTPS verification
#     ssl._create_default_https_context = _create_unverified_https_context

response = urllib.request.urlopen('https://calstore.internal.ericsson.com/elex?LI=EN/LZN7040249/0/2*&FB=0_0&FN=71_22102-AXB25019-V6Uen.*.html&HT=iss1583420186833&DT=Characteristics')
html = response.read()
# print (html) #显示结果为b开头的(bytes)，二进制形式的字符串，就是格式上不太好看
html_decode = html.decode('UTF-8')
print (html_decode)