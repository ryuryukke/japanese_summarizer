import nltk
import MeCab
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx

def read_article(file_name):
    file = open(file_name, "r")
    filedata = file.readlines()
    article = filedata[0].split("。")
    sentences = [sentence for sentence in article if sentence != "\n"]
    return sentences

def sentence_similarity(sent1, sent2):
    wakati = MeCab.Tagger('-Owakati -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
    node1, node2 = wakati.parseToNode(sent1), wakati.parseToNode(sent2)
    sent1, sent2 = set(), set()
    
    # Exclude blanks and those with specific parts of speech(Adverbs, particles, conjunctions, auxiliary verbs)
    while node1:
        word = node1.surface
        hinshi = node1.feature.split(",")[0]
        if word == " " or hinshi in ["副詞", "助詞", "接続詞", "助動詞"]:
            node1 = node1.next
            continue
        sent1.add(word)
        node1 = node1.next
    
    while node2:
        word = node2.surface
        hinshi = node2.feature.split(",")[0]
        if word == " " or hinshi in ["副詞", "助詞", "接続詞", "助動詞"]:
            node2 = node2.next
            continue
        sent2.add(word)
        node2 = node2.next

    # Bag of words
    all_words = list(sent1 | sent2)
    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)
    
    for word in sent1:
        vector1[all_words.index(word)] += 1
    for word in sent2:
        vector2[all_words.index(word)] += 1

    # cosine similarity equals 1 - cosine distance
    return 1 - cosine_distance(vector1, vector2)


def build_similarity_matrix(sentences):
    # similarity matrix shows cosine similarity between sentences
    num = len(sentences)
    similarity_matrix = np.zeros((num, num))
    for idx1 in range(num):
        for idx2 in range(num):
            if idx1 == idx2:
                continue
            similarity_matrix[idx1][idx2] = sentence_similarity(sentences[idx1], sentences[idx2])
    return similarity_matrix

def generate_summary(file_name, top_n = 3):
    summarize_text = []
    # Step 1 - Read text and split it
    sentences =  read_article(file_name)

    # Step 2 - Generate Similary Martix across sentences
    sentence_similarity_martix = build_similarity_matrix(sentences)

    # Step 3 - Rank sentences in similarity martix
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_martix)
    scores = nx.pagerank(sentence_similarity_graph)
    
    # Step 4 - Sort the rank and pick top sentences
    ranked_sentence = sorted([(scores[i], s) for i, s in enumerate(sentences)], reverse=True)

    print("top_n important sentences:")
    for i in range(top_n):
        print(f"score:{ranked_sentence[i][0]}, sentence:{ranked_sentence[i][1]}")
        summarize_text.append("".join(ranked_sentence[i][1]))

    # Step 5 - Output a summary
    print("Summary: \n", "。".join(summarize_text)+"。")

# make a summary
generate_summary("toyota.txt", 10)

