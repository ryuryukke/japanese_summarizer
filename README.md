# japanese_summarizer
This is a text summarizer for japanese.

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

## Reference
1. [text-summarizer](https://github.com/edubey/text-summarizer)                                                                                                      
2. [Understand Text Summarization and create your own summarizer in python](https://towardsdatascience.com/understand-text-summarization-and-create-your-own-summarizer-in-python-b26a9f09fc70)                                                                                                                                         
3. [MeCabを使ってみよう](https://qiita.com/yonedaco/items/27e1ad19132c9f1c9180)                                                                                      
4. [MeCabをpythonで使うまで](https://qiita.com/Sak1361/items/47e9ec464ccc770cd65c)                                                                                   
5. [日本語ストップワードの考察](https://mieruca-ai.com/ai/nlp-stopwords/)                                                                                            
6. [大自然言語時代のための、文章要約](https://qiita.com/icoxfog417/items/d06651db10e27220c819)
7. [日本経済新聞 ソフトバンク記事](https://www.nikkei.com/article/DGXMZO62742660Y0A810C2I00000/)
8. [日本経済新聞 トヨタ記事](https://www.nikkei.com/article/DGXMZO62743260Y0A810C2I00000/)
