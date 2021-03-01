#coding:utf-8

import requests
from lxml import etree

ms_url = 'https://www.morningstar.cn/quickrank/default.aspx'

cookie = 'ASP.NET_SessionId=4ygb3055xlutew55qjppibfc; MSCC=99SJ6epEdjg=; Hm_lvt_eca85e284f8b74d1200a42c9faa85464=1614595517; user=username=253581590@qq.com&nickname=jaoyang&status=Free&password=sCJtwOOUGiS9yeC/VHCOfw==; authWeb=67CB818CB970265ED52E076C4DF11897030B428E05A808CC0C9D6964E1949E62D1E9E3E31DDAC70A0DA02E019410B1193D2B8FAE836B08E23C6AD99D1F047EAA85594A58745C65DE40C2DAB908953B28F871EAB3E9A47792D862703B09FBEEAC1E962512A5F9E3385216937A6175A41697190CBD; MS_LocalEmailAddr=253581590@qq.com=; Hm_lpvt_eca85e284f8b74d1200a42c9faa85464=1614608125'

headers = {'Cookie':cookie}

if __name__ == '__main__':
   html = requests.get(url=ms_url,headers=headers)
   html.encoding = html.apparent_encoding
   # 解析数据
   selector = etree.HTML(html.text)
   content = selector.xpath('//table/tr[@class="gridItem" or @class="gridAlternateItem"]')
   for tr in content:
      td = tr.findall('td')
      print(td[3].find('a').text)

