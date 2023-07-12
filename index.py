# #coding: UTF-8

# # from traceback import print_tb
# import requests
# from bs4 import BeautifulSoup
# from datetime import datetime, timedelta

# # サイトのスクレイピングを実施
# url = "https://bangumi.org/talents/254278"
# word_response = requests.get(url)
# word_soup = BeautifulSoup(word_response.text, 'html.parser')

# def main():
#   #期間を取得
#   today = datetime.today()
#   seven_days_later = today + timedelta(days=7)
#   print('~'+ seven_days_later.strftime('%m月%d日')+'まで')

#   #テレビ番組の出演一覧を取得
#   TvContents = word_soup.find_all('div', class_='left_text_area')

#   i = 0
#   for TvContent in TvContents:
#       i=i+1
#       print('番組'+str(i))
#       print('番組タイトル：'+TvContent.find('p', class_='program_title').text)
#       print('放送時間：'+TvContent.find('p', class_='program_supplement').text.replace(" ", "").replace("\n", ""))


# if __name__ == "__main__":
#   main()
