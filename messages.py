from typing import Annotated
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
messageinfo = ""


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_headers=["*"],
    allow_methods=["*"],
    allow_credentials=True
)
class Item(BaseModel):
    Title: str
    Message: str

@app.post("/send/")
async def send_message(item:Item):
    global messageinfo
    messageinfo += item.Message+" <br>"

@app.get("/fetch/")
async def download_file():
   return {"message": messageinfo}
