from main import app
from typing import Optional

from app.models import Scrapper

def messages_of_errors(message: str):
    return {'Error': message.title()}


@app.get("/search/{item_id}")
def read_root(item_id: str):
    
    search = item_id.replace(" ", "+")
    data = Scrapper.Parser(search)
        
    if data.parse_data() == []:
        return messages_of_errors("We don't found fics with this name :/")
        
    return data.parse_data()

