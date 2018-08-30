#coding: utf8
# author: Xinyi Wu (xinyi.wu5@pactera.com)
import gensim.summarization
import logging

logger = logging.getLogger("NewsScraper.NLP")

def newsTitleFilter(title):
  return True

def newsSummaryFilter(summary):
  return True

class Processor:
  def __init__(self, news):
    self.listNews = news

  def summarize(self):
    for news in self.listNews:
      try:
        news['summaryGensim'] = gensim.summarization.summarize(news['article'],
                                                               word_count=100)
      except:
        logger.exception("Error in summarizing " + news['title'])
        news['summaryGensim'] = None

  @property
  def newsList(self):
    return self.listNews

if __name__ == '__main__':
    print(newsSummaryFilter('This is a fake news.'))
    print(newsTitleFilter('Today is a good day.'))