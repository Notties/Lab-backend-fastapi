from typing import Union
from fastapi.middleware.cors import CORSMiddleware


from fastapi import FastAPI

app = FastAPI()

origins = [
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
     res = [{"Name": "Hi"}, {"Name": "Bro"}]
     return res
     
@app.get("/get_bmi/{height}-{weight}")
def read_root(height:float, weight:float):
     bmi = weight / (height/100)**2
     return bmi

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}