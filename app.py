import uuid
import os
import uvicorn
import logging
import json
from http import HTTPStatus
from functools import lru_cache
from fastapi import FastAPI, HTTPException, status, Request, Response


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0')