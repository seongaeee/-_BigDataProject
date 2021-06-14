from wordcloud import WordCloud
import wordcloud
import matplotlib.pyplot as plt

# 단어와 빈도수 변수에 저장
tokenized_doc = []
check = []

with open('data/rnh.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        line_array = line.strip().split("\t")
        tokenized_doc.append(line_array[0])
        check.append(int(line_array[1]))

# 딕셔너리 만들기
frq = {}
for t in range(len(tokenized_doc)):
    frq[tokenized_doc[t]] = check[t]

print(frq)

# cloud 시각화
wordcloud = WordCloud(font_path="HMFMMUEX.TTC", width= 800, height=800)
keyword = wordcloud.generate_from_frequencies(frq)
array = wordcloud.to_array()

plt.figure(figsize=(30, 30))
plt.imshow(array, interpolation="bilinear")
plt.axis("off")
plt.show()
