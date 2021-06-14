import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager, rc


def showGraph(wordInfo):
    font_location = "HMFMMUEX.TTC"
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    matplotlib.rc('font', family=font_name)

    plt.xlabel('주요 단어')
    plt.ylabel('빈도수')
    plt.grid(True)

    Sorted_Dict_Values = sorted(wordInfo.values(), reverse=True)
    Sorted_Dict_Keys = sorted(wordInfo, key=wordInfo.get, reverse=True)


    # 30 이하 값 딕셔너리 삭제
    for x in range(len(Sorted_Dict_Values)):
        if Sorted_Dict_Values[x] < 30:
            save_x = x
            break
    del Sorted_Dict_Values[save_x:len(Sorted_Dict_Values)]
    del Sorted_Dict_Keys[save_x:len(Sorted_Dict_Keys)]

    # 그래프 만들기
    plt.bar(range(len(Sorted_Dict_Values)), Sorted_Dict_Values, align='center')
    plt.xticks(range(len(Sorted_Dict_Keys)), list(Sorted_Dict_Keys), rotation='70')

    plt.show()


def main():
    tokenized_doc = []
    check = []

    # 데이터 가져오기
    with open('data/dance.txt', 'r', encoding='UTF-8') as f:
        for line in f:
            line_array = line.strip().split("\t")
            tokenized_doc.append(line_array[0])
            check.append(int(line_array[1]))

    # input 데이터 만들기
    word = {}
    for t in range(len(tokenized_doc)):
        word[tokenized_doc[t]] = check[t]

    # print(word)
    showGraph(word)


if __name__ == "__main__":
    main()
