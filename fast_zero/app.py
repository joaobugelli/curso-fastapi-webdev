from fastapi import FastAPI
from http import HTTPStatus
from fast_zero.schemas import Message

app = FastAPI()

var = None

@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'hello world'}
