# Semantic Query Search Using Query Augmentation in Word Graphs


## Model Query Comparison  
All the below queries were run on the *20 newsgroups* dataset. 

| Query                   	| Word Graph with Cosine Ranking                  	| BM25 Ranking                                    	| Euclidean Ranking                                	|
|-------------------------	|-------------------------------------------------	|-------------------------------------------------	|--------------------------------------------------	|
| vote politics elections 	| 20news-bydate-train/talk.politics.misc/178406   	| 20news-bydate-train/talk.politics.misc/178406   	| 20news-bydate-train/talk.politics.misc/178299    	|
|                         	| 20news-bydate-train/talk.politics.guns/54690    	| 20news-bydate-train/talk.politics.mideast/75929 	| 20news-bydate-train/comp.windows.x/66922         	|
|                         	| 20news-bydate-train/talk.politics.mideast/75929 	| 20news-bydate-train/talk.politics.misc/177001   	| 20news-bydate-train/sci.med/58809                	|
|                         	| 20news-bydate-train/rec.motorcycles/104724      	| 20news-bydate-train/rec.motorcycles/104367      	| 20news-bydate-train/comp.os.ms-windows.misc/9763 	|
|                         	| 20news-bydate-train/talk.politics.misc/177001   	| 20news-bydate-train/talk.politics.guns/54690    	| 20news-bydate-train/sci.space/61229              	|
|                         	| 20news-bydate-train/rec.motorcycles/104367      	| 20news-bydate-train/rec.motorcycles/104724      	| 20news-bydate-train/talk.religion.misc/84071     	|
|                         	| 20news-bydate-train/talk.politics.misc/177004   	| 20news-bydate-train/talk.politics.guns/54314    	| 20news-bydate-train/talk.politics.guns/54684     	|
|                         	| 20news-bydate-train/talk.politics.mideast/76532 	| 20news-bydate-train/talk.politics.guns/54187    	| 20news-bydate-train/talk.politics.guns/53315     	|
|                         	| 20news-bydate-train/talk.politics.misc/178505   	| 20news-bydate-train/talk.politics.misc/176944   	| 20news-bydate-train/talk.politics.misc/178405    	|
|                         	| 20news-bydate-train/talk.politics.guns/54187    	| 20news-bydate-train/talk.politics.guns/54684    	| 20news-bydate-train/talk.politics.guns/53297     	|

Time taken to fetch results: 12.5340821743 seconds

![Word Graph for Politics based query](https://github.com/aneeshbose/Word-Graph-based-Semantic-Query-Search/blob/main/imgs/subgraph_politics.png?raw=true)


| Query                            	| Word Graph with Cosine Ranking      	| BM25 Ranking                        	| Euclidean Ranking                               	|
|----------------------------------	|-------------------------------------	|-------------------------------------	|-------------------------------------------------	|
| planet satellite astronaut orbit 	| 20news-bydate-train/sci.space/59870 	| 20news-bydate-train/sci.space/59874 	| 20news-bydate-train/comp.windows.x/67064        	|
|                                  	| 20news-bydate-train/sci.space/59909 	| 20news-bydate-train/sci.space/59905 	| 20news-bydate-train/misc.forsale/76515          	|
|                                  	| 20news-bydate-train/sci.space/59905 	| 20news-bydate-train/sci.space/59871 	| 20news-bydate-train/sci.med/59204               	|
|                                  	| 20news-bydate-train/sci.space/59874 	| 20news-bydate-train/sci.space/60103 	| 20news-bydate-train/rec.motorcycles/104726      	|
|                                  	| 20news-bydate-train/sci.space/59913 	| 20news-bydate-train/sci.space/59870 	| 20news-bydate-train/rec.motorcycles/104705      	|
|                                  	| 20news-bydate-train/sci.space/60103 	| 20news-bydate-train/sci.space/59909 	| 20news-bydate-train/sci.med/58841               	|
|                                  	| 20news-bydate-train/sci.space/60932 	| 20news-bydate-train/sci.space/59873 	| 20news-bydate-train/comp.windows.x/66966        	|
|                                  	| 20news-bydate-train/sci.space/59871 	| 20news-bydate-train/sci.space/61207 	| 20news-bydate-train/comp.windows.x/67200        	|
|                                  	| 20news-bydate-train/sci.space/59904 	| 20news-bydate-train/sci.space/59850 	| 20news-bydate-train/comp.sys.mac.hardware/50455 	|
|                                  	| 20news-bydate-train/sci.space/60187 	| 20news-bydate-train/sci.space/61155 	| 20news-bydate-train/sci.space/59870             	|

Time taken to fetch results: 23.7800240517 seconds

![Word Graph for Space based query](https://github.com/aneeshbose/Word-Graph-based-Semantic-Query-Search/blob/main/imgs/subgraph_sci_space.png?raw=true)

| Query                       	| Word Graph with Cosine Ranking             	| BM25 Ranking                               	| Euclidean Ranking                               	|
|-----------------------------	|--------------------------------------------	|--------------------------------------------	|-------------------------------------------------	|
| wheel shaft motorcycle gear 	| 20news-bydate-train/rec.motorcycles/104290 	| 20news-bydate-train/rec.autos/102764       	| 20news-bydate-train/rec.motorcycles/104582      	|
|                             	| 20news-bydate-train/rec.motorcycles/104726 	| 20news-bydate-train/rec.motorcycles/104637 	| 20news-bydate-train/rec.motorcycles/104548      	|
|                             	| 20news-bydate-train/rec.motorcycles/104639 	| 20news-bydate-train/comp.windows.x/66871   	| 20news-bydate-train/rec.motorcycles/104625      	|
|                             	| 20news-bydate-train/rec.motorcycles/104536 	| 20news-bydate-train/rec.motorcycles/104569 	| 20news-bydate-train/rec.motorcycles/104947      	|
|                             	| 20news-bydate-train/rec.motorcycles/104387 	| 20news-bydate-train/rec.autos/102770       	| 20news-bydate-train/rec.autos/102770            	|
|                             	| 20news-bydate-train/rec.motorcycles/104814 	| 20news-bydate-train/rec.motorcycles/104497 	| 20news-bydate-train/misc.forsale/76187          	|
|                             	| 20news-bydate-train/misc.forsale/76187     	| 20news-bydate-train/rec.motorcycles/104841 	| 20news-bydate-train/rec.autos/102764            	|
|                             	| 20news-bydate-train/rec.motorcycles/104569 	| 20news-bydate-train/rec.motorcycles/104451 	| 20news-bydate-train/talk.politics.mideast/76103 	|
|                             	| 20news-bydate-train/rec.motorcycles/104841 	| 20news-bydate-train/misc.forsale/76187     	| 20news-bydate-train/talk.politics.misc/176936   	|
|                             	| 20news-bydate-train/rec.motorcycles/104497 	| 20news-bydate-train/rec.motorcycles/104814 	| 20news-bydate-train/talk.politics.mideast/76067 	|

Time taken to fetch results: 13.1146659851 seconds

![Word Graph for Sports based query](https://github.com/aneeshbose/Word-Graph-based-Semantic-Query-Search/blob/main/imgs/subgraph_rec_motorcycle.png?raw=true)
