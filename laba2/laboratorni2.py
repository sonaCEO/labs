
from fastapi import FastAPI
import wikipedia
from pydantic import BaseModel

app = FastAPI()


class Out_Put(BaseModel):
    return_name: str


class Multi_Out_Put(BaseModel):
    return_multi_names: str


class Geo_Out_Put(BaseModel):
    geoplace: str


class Body_Request(BaseModel):
    key: str


@app.get('/{name}', response_model=Out_Put)
def wikipedia_names(name: str):
    return Out_Put(return_name=str(wikipedia.summary(name)))


@app.get('/multi/{name}', response_model=Multi_Out_Put)
def wikipedia_multi_names(name: str, names_numbers: int):
    result = ''
    for i in range(names_numbers):
        result += name + f' pages numbers #{i + 1} :' + str(wikipedia.search(name, results=2))
    return Multi_Out_Put(return_multi_names=result)


@app.post('/body/', response_model=Geo_Out_Put)
def get_wikipedia_by_body(request: Body_Request):
    page = wikipedia.page(request.key)
    return Geo_Out_Put(geoplace=page.summary)
