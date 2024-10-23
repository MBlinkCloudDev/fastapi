import requests

url = "http://127.0.0.1:8000/"


# get standard response without using parameters
response = requests.get(url=url)


print(response.status_code)
print(response.json(), type(response.json()))

# get person by ID
r2 = requests.get(url+"person/1")#, params={key: value}, args)
print(r2.json())


# get entire entries
r3 = requests.get(url+"search")#, params={key: value}, args)
print(r3.json())


# get entries based on age and name
r4 = requests.get(url+"search", params={"age": 25, "name": "Mike"})#, args)
print(r4.json())

#-------------------------------------------------------------------------------

myobj = {
    "id": 8,
    "name": "str",
    "age": 200,
    "gender": "str2"
}

# post new entry to the "database"-JSON
r5 = requests.post(url+"addPerson", json=myobj)
print(r5.json())


# update entry based on ID
r6 = requests.put(url+"changePerson", json=myobj)
print(r6.text)
#print(r6.json())



# delete entry based on ID
p_id=16
r7 = requests.delete(url+f"deletePerson/{p_id}", json=myobj)
print(r7.json())
