Tools 


Install



Imports.py : This module contains all the imports statement required to run the all the libraries used in 

webscraping.py and countryinfo.py : 
In this module,we scraped google news website related to covid and parsed them.We used Google News and newspaper libraries for parsing the article and being able to fetch data. Given the time period and query on which you want to search the news articles, we would get a list which will contain date, title, link,article. Given the scope of the project was restricted  to the African context,we proceeded with web scraping using various key words such African countries contained in countryinfo.py combined with terms such as covid or vaccinations.Furthermore, given limitations on the size of the dashboard, and relevancy of the data (more recent information preferred), we concentrated on results no older than 2 days from the current date.As result,we generated a dataframe containing the title,date of publication,text and keywords of each article.


preprocessing.py : 

Given that the results returned by google search are not always relevant to the query submit, an additional layer of data preprocessing was required. At this stage, for each article the keywords were identified. The keywords are most frequent words in text, or the entities recognized in text. Keywords were both used to eliminate articles that are not related to covid or articles that are out of African context. Keeping articles containing at least two keywords in the compiled list of words related to Covid.

Certain number of articles scrapped are approximately similar or complementing each other. To maintain coherence, at this stage the similarity score between one article to another was computed. We first transformed the articles text into word embedding or real-valued vectors using a sentence transformer. This results in vectors that are similar for words that appear in similar contexts, and thus have a similar meaning which enabled us to handle synonyms or words with similar meaning in the text and then we computed their similarity score using cosine similarity. The articles were clustered and combined according to their similarity score.


models.py : 

The combined articles went through a text preprocessing process such as  tokenization. The combined articles were divided into chunks of length that could be processed by the model and then they are summarized  using BART which uses a combination of concepts from BERT and GPT using Bidirectional and Auto-Regressive Transformers to train the model. Depending on the results, we improved the previous stages (web scraping, document filtering and similarity).


generate_summary.py : 

In this module,we combine all the above module to generate summary with respect to the url that was passed in. 



 
