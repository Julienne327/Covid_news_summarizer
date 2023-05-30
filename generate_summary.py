# from transformers import BartTokenizer, BartForConditionalGeneration
# import torch
# from transformers import PegasusTokenizer, PegasusForConditionalGeneration

from preprocessing import*
from models import*
from webscraping import*
from countryinfo import* 
from imports import*

news_url = "https://news.google.com/news?q=Africa%20Covid&hl=en-US&sort=date&gl=Africa&num=10&ceid=US%3Aen&output=rss"
term = "vaccinations"
## combining results from both search terms 

def get_summary(news_url, term):
    news_df = generate_news_dataframe(news_url,term)
    selected_news = get_selected_news(news_df)
    article = get_article(selected_news)
    
    clustered_text, clustered_link = check_similarities(article, selected_news)

    print(clustered_link)
    
    # # my_links = [link.replace("\n", "") for link in link_list]

    # new_links = []
    
    # for links in clustered_link:
    #     inner_links = []
    #     for link in links:
    #         inner_links.append(link.replace("\n", ""))
    #     new_links.append(inner_links)
            
    # summaries = []
    # #Loop thru a list of text:links pairs
    # i = 0
    # for covid_data in clustered_text:
    #     summary = generate_summary(covid_data)
    #     summaries.append(summary)
    #     print("Summary: ", summary) 
    #     print("\nlink:"+str(i), new_links[i])

    #     i += 1
    #     # if i == 10:
    #     #     break
    return clustered_text
    # return summary, link_list

  
  