from main import app
from typing import Optional


def messages_of_errors(message: str):
    return {'Error': message.title()}


@app.get("/search/{item_id}")
def read_root(item_id: str):
    from app.models import Scrapper

    search = item_id.replace(" ", "+")
    data = Scrapper.Scrapper(search)
    
    names_json = []
    c = 0
    if data.verify_connection() == 200:
        
        if data.parse_title() == []:
            return messages_of_errors("We don't found fics with this name :/")
        
        for i in data.parse_title():
            names_json.append(
                {
                    "author": data.parse_author()[c],
                    "title": i,
                    "thumb": data.parse_thumb()[c],
                    "status": data.parse_status()[c],
                }
            )
            c += 1

        return names_json
    else:
        return messages_of_errors(f"Status {data.verify_connection()}")

