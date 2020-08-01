from bs4 import BeautifulSoup
import requests

class Scrapper():
    """
		Esta classe é apenas um teste, aplicar SOLID,
  		e pattenr factory, basicamente refatorar este codigo.
    """
    
    def __init__(self, search: str):
        #print(f"https://www.spiritfanfiction.com/busca?query={search}")
        self.request = requests.get(f"https://www.spiritfanfiction.com/busca?query={search}")
    
    
    def scrapping_base(self):
        title = [str]
        author = [str]
        thumb = [str]
        status = [str]
        data = [str]
                
        soup = BeautifulSoup(self.request.content, "html.parser")
        articles = soup.find_all('article', class_="clearfix espacamentoTop")
        
        for article in articles:
            a = article.find('a', class_="link")
            title.append(a.get_text())
            
            nick = article.find('a', class_="usuario usuarioPopupTrigger link")
            author.append(nick.get_text())
            
            tt = article.find('img', class_="img-rounded")
            thumb.append(tt.get('data-original'))
            
            span = article.find('span', class_="label label-fanfics")
            status.append(span.get_text())
        
        data = title, author, thumb, status
        
        return data
    

class Parser:
    
    def __init__(self, search: str):
        self.data = Scrapper(search)
    
    def parse_data(self):
        ds = self.data
        counter = 0
        retorno = [dict]
        
        for i in ds.scrapping_base()[0]:

            retorno.append({
                "title": i,
                "author": ds.scrapping_base()[1][counter],
                "thumb": ds.scrapping_base()[2][counter],
                "status": ds.scrapping_base()[3][counter]
            })
            
            counter += 1

        return retorno