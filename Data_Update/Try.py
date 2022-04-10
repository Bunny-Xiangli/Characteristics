# -*- coding: utf-8 -*-

import lxml
# import beautifulsoup4 不能这样写，因为BeautifulSoup被打包进了bs4
from bs4 import BeautifulSoup
import lxml
import html5lib
import urllib3


url = 'view-source:https://calstore.internal.ericsson.com/elex?id=78103&SR=DOCTITLE&ORPA=chara&fn=71_22102-AXB25019-V6Uen.DM.html#dzj1583419969522'

request = urllib3.Request(url)

response = urllib3.urlopen(request,timeout=20)

content = response.read()

soup = BeautifulSoup(content,'html.parser')

tag = soup.title


# if 'id="iss1583420186833__table_ydf_r1c_j4b" class="table"' is in

    #Get title: