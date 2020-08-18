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

## Detail
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
