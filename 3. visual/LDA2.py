import pyLDAvis.gensim
import gensim
from gensim import corpora
from imp import reload

# 단어와 빈도수 변수에 저장
tokenized_doc = []
check = []

a = 0
tokenized_doc.append([]) # tokenized_doc = [[]]
check.append([])
with open('data/ballad.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        line_array = line.strip().split("\t")
        tokenized_doc[a].append(line_array[0])
        check[a].append(int(line_array[1]))

a = 1
tokenized_doc.append([]) # tokenized_doc = [[],[]]
check.append([])
with open('data/dance.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        line_array = line.strip().split("\t")
        tokenized_doc[a].append(line_array[0])
        check[a].append(int(line_array[1]))

a = 2
tokenized_doc.append([]) # tokenized_doc = [[],[]]
check.append([])
with open('data/folk.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        line_array = line.strip().split("\t")
        tokenized_doc[a].append(line_array[0])
        check[a].append(int(line_array[1]))

a = 3
tokenized_doc.append([]) # tokenized_doc = [[],[]]
check.append([])
with open('data/ost.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        line_array = line.strip().split("\t")
        tokenized_doc[a].append(line_array[0])
        check[a].append(int(line_array[1]))

a = 4
tokenized_doc.append([]) # tokenized_doc = [[],[]]
check.append([])
with open('data/rnb.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        line_array = line.strip().split("\t")
        tokenized_doc[a].append(line_array[0])
        check[a].append(int(line_array[1]))

a = 5
tokenized_doc.append([]) # tokenized_doc = [[],[]]
check.append([])
with open('data/rnh.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        line_array = line.strip().split("\t")
        tokenized_doc[a].append(line_array[0])
        check[a].append(int(line_array[1]))

# ------------------------------------------------------------------

dictionary = corpora.Dictionary(tokenized_doc)
corpus = [dictionary.doc2bow(text) for text in tokenized_doc]

print(dictionary)
# ------------------------------------------------------------------
# LDA 인풋값 (word encoding, 빈도수) 만들기
output_list = []

for x in range(6):
    print("x", x)
    output_list.append([])
    for a in range(len(tokenized_doc[x])):
        for b in range(len(dictionary)):
            if tokenized_doc[x][a] == dictionary[b]:
                input_tuple = (b, check[x][a])
                output_list[x].append(input_tuple)
                break

# LDA 학습 및 시각화
NUM_TOPICS = 2 #20개의 토픽, k=20
ldamodel = gensim.models.ldamodel.LdaModel(output_list, num_topics=NUM_TOPICS, id2word=dictionary, passes=1)
topics = ldamodel.print_topics(num_words=5)
#for topic in topics:
#    print(topic)

vis = pyLDAvis.gensim.prepare(ldamodel, output_list, dictionary)
pyLDAvis.save_html(vis, 'chart_ly.html')


