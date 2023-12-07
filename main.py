from fastapi import FastAPI
from routers import bragdocs

app = FastAPI()

app.include_router(bragdocs.router)
