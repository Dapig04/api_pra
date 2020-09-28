import requests
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
import json


url = "https://openapi.naver.com/v1/search/news.json?query=smart"  # json 결과
your_id='kOqbDZNGInFEVynPzJDY'
your_secret='3EkQBXxBiH'
header = {"X-Naver-Client-Id":your_id,"X-Naver-Client-Secret": your_secret}

res=requests.get(url,headers=header)
res.status_code
rt_dict=json.loads(res.content) 
print(rt_dict.keys())
print(pd.DataFrame(rt_dict['items']))



# import os
# import sys
# import urllib.request
# client_id = your_id
# client_secret = your_secret
# encText = urllib.parse.quote("smart")
# url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
# # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
# request = urllib.request.Request(url)
# request.add_header("X-Naver-Client-Id",client_id)
# request.add_header("X-Naver-Client-Secret",client_secret)
# response = urllib.request.urlopen(request)
# rescode = response.getcode()
# if(rescode==200):
#     response_body = response.read()
#     print(response_body.decode('utf-8'))
# else:
#     print("Error Code:" + rescode)