# coding=UTF-8
class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
        
    def add_url(self,url):
        if url is None:
            return
        else:
            self.new_urls.add(url)
        
    def add_urls(self,urls):
        if urls is None or len(urls)==0:
            return 
        else:
            for url in urls:
                self.add_url(url)
                     
    def has_url(self):
        return (len(self.new_urls)!=0)
         
    def next_url(self):
        url = self.new_urls.pop()
        self.old_urls.add(url)
        return url    
         
         
                        