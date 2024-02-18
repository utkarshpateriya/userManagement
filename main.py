from fastapi import FastAPI
from routers import itemsRoute

app = FastAPI()

app.include_router(itemsRoute.router)