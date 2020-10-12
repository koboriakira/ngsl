import csv
from typing import Dict, List


def prepare():
    """
    dictionary.pyなどをつくるために作ったメソッド
    """
    dictionary: Dict[str, List[str]] = {}
    inverted_dictionary: Dict[str, str] = {}

    with open('ngsl_words.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            # 言葉の原形
            infinitiv = row[0]
            for word in row:
                if infinitiv not in dictionary:
                    dictionary[infinitiv] = []
                dictionary[infinitiv].append(word)
                inverted_dictionary[word] = infinitiv

    # print(dictionary)
    # print(inverted_dictionary)

    with open('ngsl_word_rank.csv') as f:
        reader = csv.reader(f)
        rank_dict: Dict[str, int] = {}
        for row in reader:
            intinitiv = row[0]
            rank = int(row[1])
            rank_dict[intinitiv] = rank

        # print(rank_dict)

    with open('supplemental.csv') as f:
        reader = csv.reader(f)
        supplemental = {}
        for row in reader:
            # 言葉の原形
            infinitiv = row[0]
            for word in row:
                if infinitiv not in supplemental:
                    supplemental[infinitiv] = []
                supplemental[infinitiv].append(word)

        print(supplemental)


prepare()
