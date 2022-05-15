# Word-Graph-based-Semantic-Query-Search


## Model Query Comparison  
All the below queries were run on the *20 newsgroups* dataset. 

|Query                     | Word Graph with Cosine Ranking               | BM25 Ranking                                 | Euclidean Ranking |
|------                    | -------------------------------              | -------------                                | ------------------|
|vote politics elections   |20news-bydate-train/talk.politics.misc/178406 | 20news-bydate-train/talk.politics.misc/178406  |20news-bydate-train/talk.politics.misc/178299 |
|                          |20news-bydate-train/talk.politics.guns/54690  | 20news-bydate-train/talk.politics.mideast/75929 | 20news-bydate-train/comp.windows.x/66922 |
|                          |20news-bydate-train/talk.politics.mideast/75929 | 20news-bydate-train/talk.politics.misc/177001 | 20news-bydate-train/sci.med/58809 |
|                          |20news-bydate-train/rec.motorcycles/104724    | 20news-bydate-train/rec.motorcycles/104367 | 20news-bydate-train/comp.os.ms-windows.misc/9763 |
|                          |20news-bydate-train/talk.politics.misc/177001 | 20news-bydate-train/talk.politics.guns/54690 | 20news-bydate-train/sci.space/61229 |
|                          |20news-bydate-train/rec.motorcycles/104367    | 20news-bydate-train/rec.motorcycles/104724 | 20news-bydate-train/talk.religion.misc/84071 |
|                          |20news-bydate-train/talk.politics.misc/177004 | 20news-bydate-train/talk.politics.guns/54314 | 20news-bydate-train/talk.politics.guns/54684 |
|                          |20news-bydate-train/talk.politics.mideast/76532 | 20news-bydate-train/talk.politics.guns/54187 | 20news-bydate-train/talk.politics.guns/53315 |
|                          |20news-bydate-train/talk.politics.misc/178505 | 20news-bydate-train/talk.politics.misc/176944 | 20news-bydate-train/talk.politics.misc/178405 |
|                          |20news-bydate-train/talk.politics.guns/54187  | 20news-bydate-train/talk.politics.guns/54684 | 20news-bydate-train/talk.politics.guns/53297 |
