# coding=UTF-8
from test import url_manager, http_parse, http_download, http_writer 
class HttpMain(object):
    def __init__(self):
        self.urlmanager = url_manager.UrlManager()
        self.parse = http_parse.HttpParse()
        self.download = http_download.Download()
        self.writer = http_writer.HttpWriter()
    def main(self,root_url):
        count = 1
        urlmanager = self.urlmanager
        parse = self.parse
        down = self.download
        writer = self.writer
        
        self.urlmanager.add_url(root_url)
        
        while(self.urlmanager.has_url()):
            try:
                url = self.urlmanager.next_url()
                print('craw %d:%s'%(count,url))
                content = down.download(url)#下载url中的内容
                urls,data = parse.get_info(url,content) #解析当前的文本,得到相关的url
                urlmanager.add_urls(urls) #添加到url管理器中
                writer.writer_content(data)#写入writer中
                count = count+1 #如果失败，抓取失败的也会算入其中
            except:
                print ('error')
            if(count==10):#只抓取100条
                break
        writer.writer_htm()#将数据写入一个html中    
if __name__=='__main__':#如果不写这句话的话，import此模块同样会执行该函数，引入时__name__=模块名(http_main)，不引入时__name__=__main__
    print (__name__)
    main = HttpMain()
    main.main('http://baike.baidu.com/link?url=B4sod6A1rdbVwd660XmWeo6CbFnY-EvNKSfOEankVYCxsV1LSmgFw4rIrjzv6Q2WaF3gGFyzq_Lrc6KzKPycYq')     
        
        
        
        
        
        
        
        
        
