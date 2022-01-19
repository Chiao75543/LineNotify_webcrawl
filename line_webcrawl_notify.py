import requests
import random
import logging
import requests
from bs4 import BeautifulSoup

def web_crawl(weblink):
  headers = {
    	'user-agent': 'input your user angent'
      }
  res = requests.get(weblink, headers=headers)
  res.encoding = 'UTF-8'
  soup = BeautifulSoup(res.text, 'html.parser')
  return soup

soup_2 = web_crawl('https://www.cdc.gov.tw/Category/NewsPage/EmXemht4IT-IRAPrAnyG9A')
link = soup_2.find('td').find('a').get('href')
title = soup_2.find('td').find('a').get('title')
print('https://www.cdc.gov.tw'+link)
print(title)

# 設定Log的顯示格式
logging.basicConfig(level=logging.INFO,
	format='[%(asctime)s %(levelname)-8s] %(message)s',
	datefmt='%Y%m%d %H:%M:%S',
	)


# Line Notify api
def lineNotifyMessage(token, msg):
    headers = {
        'Authorization': 'Bearer ' + token, # Token
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    payload = {'message': msg}
    # Post to Line Notify
    r = requests.post(
        'https://notify-api.line.me/api/notify',
        headers=headers, 
        params=payload)
    return r.status_code


# 主程式開始
if __name__ == '__main__':

    # Line Notify 的 Token
    token = 'input your token'
    msg=''
    msg+='\n'+'【本日最新消息】'+'\n'+title
    msg+='\n'+'https://www.cdc.gov.tw'+link
    msg+='\n'+'【資料來源】'+'\n'+'https://www.cdc.gov.tw'
    msg+='\n'+'【直播頻道】'+'\n'+'https://www.youtube.com/channel/UCyh91eTE9jA3ykg8W3_v3DQ'

        # 確認訊息有內容
    if len(msg):
        logging.info('Sending Line Notify . . . ')
        status_code = lineNotifyMessage(token, msg)
        if status_code == 200:
            logging.info('Success.')
        else:
            logging.error('Response: {}'.format(status_code))
    else:
        logging.error('msg is empty.')
