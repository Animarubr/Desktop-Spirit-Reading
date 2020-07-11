from bs4 import BeautifulSoup
import requests

class Scrapper(object):
    """
		Esta classe é apenas um teste, aplicar SOLID,
  		e pattenr factory, basicamente refatorar este codigo.
    """
    
    def __init__(self, search: str):
        #print(f"https://www.spiritfanfiction.com/busca?query={search}")
        self.request = requests.get(f"https://www.spiritfanfiction.com/busca?query={search}")
    
    
    def verify_connection(self):
        return self.request.status_code
    
    
    def parse_title(self):
        title = []
        soup = BeautifulSoup(self.request.content, "html.parser")
        articles = soup.find_all('article', class_="clearfix espacamentoTop")
        
        for article in articles:
            a = article.find('a', class_="link")
            title.append(a.get_text())
        
        return title
    
    
    def parse_author(self):
        author = []
        soup = BeautifulSoup(self.request.content, "html.parser")
        articles = soup.find_all('article', class_="clearfix espacamentoTop")
        
        for article in articles:
            a = article.find('a', class_="usuario usuarioPopupTrigger link")
            author.append(a.get_text())
        
        return author
    
    
    def parse_thumb(self):
        thumb = []
        soup = BeautifulSoup(self.request.content, "html.parser")
        articles = soup.find_all('article', class_="clearfix espacamentoTop")
        
        for article in articles:
            a = article.find('img', class_="img-rounded")
            thumb.append(a.get('data-original'))
        
        return thumb
    
    
    def parse_status(self):
        status = []
        soup = BeautifulSoup(self.request.content, "html.parser")
        articles = soup.find_all('article', class_="clearfix espacamentoTop")
        
        for article in articles:
            a = article.find('span', class_="label label-fanfics")
            status.append(a.get_text())
        
        return status