from fastapi import FastAPI
from routers import itemsRoute, usersRoute

app = FastAPI()

app.include_router(itemsRoute.router)
app.include_router(usersRoute.router)