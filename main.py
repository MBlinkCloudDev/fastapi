from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
from typing import Optional
import json
import requests


app = FastAPI()


@app.get("/")
def read_root():
    url = 'https://api.chucknorris.io/jokes/random'
    return requests.get(url).json()['value']

class Person(BaseModel):
    id: Optional[int] = None
    name: str
    age: int
    gender: str

with open('people.json', 'r') as f:
    people = json.load(f)['people']

@app.get('/person/{p_id}')
def get_person(p_id: int):
    person = [p for p in people if p['id'] == p_id]
    return person[0] if len(person) > 0 else {}

@app.get('/search', status_code=200)
def search(
    age: Optional[int] = Query(None, title='Age', description='The age to search for'),
    name: Optional[str] = Query(None, title='Name', description='The name to search for')
    ):

    people1 = [p for p in people if p['age'] == age]

    if name is None:
        if age is None:
            return people
        else:
            return people1
    else:
        people2 = [p for p in people if name.lower() in p['name'].lower()]
        if age is None:
            return people2
        else:
            combined = [p for p in people1 if p in people2]
            return combined


@app.post('/addPerson', status_code=201)
def add_person(person: Person):
    p_id = max([p['id'] for p in people]) + 1
    new_person = {
        'id': p_id,
        'name': person.name,
        'age': person.age,
        'gender': person.gender
    }
    people.append(new_person)

    with open('people.json', 'w') as f:
        json.dump({'people': people}, f)
    return new_person

@app.put('/changePerson', status_code=204)
def change_person(person: Person):
    new_person = {
        'id': person.id,
        'name': person.name,
        'age': person.age,
        'gender': person.gender
    }

    person_list = [p for p in people if p['id'] == person.id]
    if len(person_list) > 0:
        people.remove(person_list[0])
        people.append(new_person)
        with open('people.json', 'w') as f:
            json.dump({'people': people}, f)
        return new_person
    else:
        return HTTPException(status_code=404, detail=f'Person with id {person.id} does not exist')

@app.delete('/deletePerson/{p_id}')
def delete_person(p_id: int):
    person = [p for p in people if p['id'] == p_id]
    if len(person) > 0:
        people.remove(person[0])
        with open('people.json', 'w') as f:
            json.dump({'people': people}, f)
    else:
        raise HTTPException(status_code=404, detail=f'There is no person with id {p_id}')

