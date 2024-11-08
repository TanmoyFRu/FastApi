from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {'data':{
        "name":"Tanmoy Debnath"
    }}

@app.get('/about')
def about():
    return {'data':{
        "version":"v1.0.0",
        "author":"Tanmoy Debnath",
        "description":"This is a simple API developed using FastAPI framework."
    }}