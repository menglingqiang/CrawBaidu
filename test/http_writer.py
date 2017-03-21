# coding=UTF-8
from idlelib.iomenu import encoding
class HttpWriter(object):
    def __init__(self):
        self.datas = []
        
    def writer_content(self,content):
        if content is None:
            return
        self.datas.append(content)
    def writer_htm(self):
        fout = open('out.html','w',encoding='UTF-8')
        fout.write("<html>") 
        fout.write('<head><meta charset="utf-8"></head>') 
        fout.write("<body>") 
        fout.write("<table>")
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>"% data['url'])
            fout.write("<td>%s</td>"% data['title'])
            fout.write("<td>%s</td>"% data['detail'])
            fout.write("</tr>")
        fout.write("<table>") 
        fout.write("</body>")  
        fout.write("</html>")  