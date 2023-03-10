from typing import Union
import fastapi
import requests
app = fastapi.FastAPI()

@app.get("/")
def read_root():
    url = 'https://api.chucknorris.io/jokes/random'
    return requests.get(url).json()['value']

@app.post("/")
def hello_post():
    return {'You':'posted!'}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


