# japanese_summarizer
This is a text summarizer for japanese.　pls feel free to download it and try!

## Two Approaches for summarization
### 1. Extractive

This approach is to create a summary by extracting sentences from a text which are relatively important.

pros: A summary can be grammatically natural in most of the cases, because we can make the summary choosing some sentences from the text.

cons: We can't paraphrase because we can't use any words which are not in the text.

### 2. Abstractive

This approach is to take the meaning of the text and paraphrase the text shortly using words which are not in the text.

pros: A summary can be more rich than extractive type's one because we can use words which are not in the text.

cons: It is difficult to make a summary which is grammatically natural.

## Details
I extended [text-summarizer](https://github.com/edubey/text-summarizer) to apply to japanese as well.

Similar to the system, I used [TextRank algorithm](https://web.eecs.umich.edu/~mihalcea/papers/mihalcea.emnlp04.pdf) to rank the semantically important sentences and choose the top_n of them to be a summary.

I introduced a graph which had nodes as sentences and edges as cosine similarity between sentences.

In this algorithm, the sentences that have greater cosine similarity with more sentences can be seen as important.

I didn't specify stopwords explicitly, but I excluded the ones whose parts of speech were adverbs, particles, conjunctions and auxiliary verbs in the morphological analysis of the sentence.

This is because I assumed these parts of speech had relatively less information than ones like nouns, verbs, adjectives, etc. 

TextRank algorithm is based on [PageRank algorithm](http://ilpubs.stanford.edu:8090/422/1/1999-66.pdf).

## PageRank algorithm
PageRank algorithm is an algorithm used by Google Search to rank web pages in their search engine results.

The basic idea behind PageRank algorithm is that pages that are linked to are good pages, and links from even more linked pages (i.e., popular pages) are valued highly.

## Result
・input sentences

ソフトバンクが6月末時点で、米アマゾン株約10億ドルを保有していたことがわかった。保有資産の現金化で得た資金を上場株で運用していることを明らかにしており、他にも米マイクロソフトや米テスラなどの株式も保有していた。米規制当局に提出した文書によると、6月末時点でIT企業を中心に26の米上場株を保有。傘下の英半導体設計アームの売却・再編に向けた交渉を進めているとみられる米半導体エヌビディアの株式も約1億8000万ドル保有していた。ソフトバンクは4.5兆円の保有資産の現金化を進めている。自社株買いや負債削減に充てる方針だが、資金が一時的に積み上がっている。11日の決算発表時に孫正義会長兼社長は、資金の一部を4～6月に30銘柄の上場株で試験的に運用したことを明らかにしていた。4～6月ではソフトバンク本体で1兆円超を投資し、一部を売却して約650億円の売却益を計上した。投資先を多様化するため、ソフトバンクが67%、孫氏が33%を出資して投資運用会社を立ち上げることも決めている。

・summary

 自社株買いや負債削減に充てる方針だが、資金が一時的に積み上がっている。米規制当局に提出した文書によると、6月末時点でIT企業を中心に26の米上場株を保有。傘下の英半導体設計アームの売却・再編に向けた交渉を進めているとみられる米半導体エヌビディアの株式も約1億8000万ドル保有していた。4～6月ではソフトバンク本体で1兆円超を投資し、一部を売却して約650億円の売却益を計上した。投資先を多様化するため、ソフトバンクが67%、孫氏が33%を出資して投資運用会社を立ち上げることも決めている。
 
## Installation of Libraries
```
pip install nltk
pip install numpy
pip install networkx
```
Mecab is a morphological analyzer for Japanese texts.
### How to install MeCab
```
$ brew install mecab
$ brew install mecab-ipadic

# Add an additional dictionary
$ cd ~/Downloads
$ git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
$ cd mecab-ipadic-neologd
$ ./bin/install-mecab-ipadic-neologd -h
```

## Reference
1. [text-summarizer](https://github.com/edubey/text-summarizer)                                                                                                      
2. [Understand Text Summarization and create your own summarizer in python](https://towardsdatascience.com/understand-text-summarization-and-create-your-own-summarizer-in-python-b26a9f09fc70)                                                                                                                                         
3. [MeCabを使ってみよう](https://qiita.com/yonedaco/items/27e1ad19132c9f1c9180)                                                                                      
4. [MeCabをpythonで使うまで](https://qiita.com/Sak1361/items/47e9ec464ccc770cd65c)                                                                                   
5. [日本語ストップワードの考察](https://mieruca-ai.com/ai/nlp-stopwords/)                                                                                            
6. [大自然言語時代のための、文章要約](https://qiita.com/icoxfog417/items/d06651db10e27220c819)
7. [日本経済新聞 ソフトバンク記事](https://www.nikkei.com/article/DGXMZO62742660Y0A810C2I00000/)
8. [日本経済新聞 トヨタ記事](https://www.nikkei.com/article/DGXMZO62743260Y0A810C2I00000/)
9. [MeCabダウンロード](https://techacademy.jp/magazine/24037)

# Blogs
I wrote some detail about this implementation in [my blog](https://spond.hatenablog.com/entry/2020/08/20/135437).
My blog is only in Japanese, sorry.
