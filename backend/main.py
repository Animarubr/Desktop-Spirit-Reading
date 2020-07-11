from fastapi import FastAPI

app = FastAPI()
"""
  Para rodar a aplicação é necessario usar o seguinte comando:
  > uvicorn main:app
  
  Para ativar o reload:
  > uvicorn main:app --reload

"""

from app.controllers import routes