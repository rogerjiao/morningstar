#coding:utf-8

import requests
from lxml import etree

ms_url = 'https://www.morningstar.cn/quickrank/default.aspx'

cookie = 'ASP.NET_SessionId=pwqmkv55x4qhvo554v0paa55; Hm_lvt_eca85e284f8b74d1200a42c9faa85464=1614322961,1614322975,1614575302,1614575445; MSCC=LdGyvUq4n54=; user=username=253581590@qq.com&nickname=jaoyang&status=Free&password=sCJtwOOUGiS9yeC/VHCOfw==; authWeb=D12C0F7E5C94C634EDD327F94F032B107E9E9FEE9BE167AFF85D9C988835C893674032B2F341A93410FABC5271AF4792EC2AA2F57FE63532885EA2D5B71E9676A4E842FF62932B29F4F1AD2F9E0E1D54E7D7DB3E4F3FFE8CDF313B1FDFC5F5F23D4C9809E8D642A012C5BA06711377CA513316BF; MS_LocalEmailAddr=253581590@qq.com=; Hm_lpvt_eca85e284f8b74d1200a42c9faa85464=1614578685'

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

