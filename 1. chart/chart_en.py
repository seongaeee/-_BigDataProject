import nltk
import requests
import konlpy
from bs4 import BeautifulSoup

if __name__ == "__main__":

    # 1. 사이트 가져오기기
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
    #req = requests.get('https://music.bugs.co.kr/genre/chart/kpop/ballad/total/day', headers=header)
    req = requests.get('https://music.bugs.co.kr/genre/chart/kpop/dance/total/day', headers=header)
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

    # print(lys[0])

    # -------------------------------------------------------------------------

    # 4. 가사 전처리
    #nltk.download('punkt')
    #nltk.download('averaged_perceptron_tagger')
    word = []
    word2 = []
    for l in lys:
        for w in nltk.tag.pos_tag(nltk.tokenize.word_tokenize(l)):
            if w[0].encode().isalpha():
                if w[1] in ['NN', 'NNS', 'NNP', 'NNPS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'JJ', 'JJR',
                               'JJS']:  # 명사, 동사, 형용사
                    word.append(w[0])
        word = list(set(word))
        word2.extend(word)
        word = []

    # 5. 메모장으로 옮기기

    file = open('dance_en.txt', 'w')
    for w in word2:
        data = w + " "
        file.write(data)
    file.close()