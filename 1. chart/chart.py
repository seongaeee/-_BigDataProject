import requests
import konlpy
from bs4 import BeautifulSoup
#from konlpy.tag import Okt
from konlpy.tag import Kkma

if __name__ == "__main__":

    # 1. 사이트 가져오기기
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
    #req = requests.get('https://music.bugs.co.kr/genre/chart/kpop/ballad/total/day', headers=header)
    req = requests.get('https://music.bugs.co.kr/genre/chart/kpop/rns/total/day', headers=header)
    html = req.text
    parse = BeautifulSoup(html, 'html.parser')

    # 2. 차트 순위 100개 페이지 가져오기
    sites = parse.find_all("a", {"class": "trackInfo"})

    site = []

    for t in sites:
        site.append(t["href"])

    # print(site)

    # 3. 가사 가져오기
    lys = []
    for s in site:
        # 3-1. 해당 페이지 가져오기
        header1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
        req1 = requests.get(s, headers=header)
        html1 = req1.text
        parse1 = BeautifulSoup(html1, 'html.parser')

        # 3-2. 해당 가사 가져오기
        ly = parse1.find("div", {"class": "lyricsContainer"})
        if ly.find('xmp'):
            lys.append(ly.find('xmp').text)

    # -------------------------------------------------------------------------

    # 4. 가사 전처리
    word = []
    kkma = Kkma()

    for l in lys:
        for w in kkma.nouns(l):
            word.append(w)

    print(word)

    # ------------------------------------------------------------------------

    # 5. 메모장으로 옮기기

    file = open('rnb.txt', 'w')
    for w in word:
        data = w + " "
        file.write(data)
    file.close()


    # 5. mysql 옮기기
    #conn = pymysql.connect(host='localhost', user='root', password='2791', db='chart', charset='utf8')
    #cursor = conn.cursor()
    #sql = "INSERT INTO chart_ly2 (id, word) VALUES (%s, %s)"

    #num = 1
    #for w in word:
    #    cursor.execute(sql, (num, w))
    #    num = num + 1

    #conn.commit()
    #conn.close()

