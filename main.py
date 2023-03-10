from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    #return {"Hello": "World"}
    url = 'https://api.chucknorris.io/jokes/random'
    return requests.get(url).json()['value']

@app.post("/")
def hello_post():
    return {'You':'posted!'}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
