# coding=UTF-8
from bs4 import BeautifulSoup
import re
import urllib
class HttpParse(object):
    def get_urls(self,page_url,soup):
        new_urls = set()
        links = soup.find_all('a',href=re.compile(r"/item/+"))
        for link in links:
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls

    def get_data(self,page_url,soup):
        data = {}
        data['url']=page_url
        title_node = soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find('h1')
        data['title'] = title_node.get_text()
        content_node = soup.find('div',class_="lemma-summary")
        data['detail'] = content_node.get_text()
        return data
        
    def get_info(self,page_url,content):
        if page_url is None or content is None:
            return 
        soup = BeautifulSoup(content,'html.parser',from_encoding='UTF-8')
        new_urls = self.get_urls(page_url, soup)
        new_data = self.get_data(page_url, soup)
        return new_urls,new_data
        