from linebot import LineBotApi, LineBotSdkDeprecatedIn30
from linebot.models import TextSendMessage
import requests
from bs4 import BeautifulSoup
from datetime import timedelta, datetime
import warnings
import locale
from dotenv import load_dotenv
import os

load_dotenv()
CHANNEL_ACCESS_TOKEN = os.environ['CHANNEL_ACCESS_TOKEN']

# サイトのスクレイピングを実施
url = "https://bangumi.org/talents/254278"
word_response = requests.get(url)
word_soup = BeautifulSoup(word_response.text, 'html.parser')

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')

def main():

    #期間を取得
    today = datetime.today()
    seven_days_later = today + timedelta(days=7)
    name = "髙橋海人"
    #テレビ番組の出演一覧を取得
    TvContents = word_soup.find_all('div', class_='left_text_area')

    i = 0
    txt = [name+'出演番組']
    # txt.append('~'+ seven_days_later.strftime('%m月%d日')+'まで')
    txt.append('~'+ seven_days_later.strftime('%m-%d')+'まで')


    for TvContent in TvContents:
        i=i+1
        dateTime = TvContent.find('p', class_='program_supplement').text.replace(" ", "").replace("\n", "")
        title = TvContent.find('p', class_='program_title').text

        if('番組タイトル：'+ title in txt):
            continue
        txt.append('\n番組'+str(i))
        txt.append('放送時間：'+ dateTime)
        txt.append('番組タイトル：'+ title)

    message = '\n'.join(txt)
    # print(txt)
    messages = TextSendMessage(message)
    line_bot_api.broadcast(messages=messages)

if __name__ == "__main__":
    main()
