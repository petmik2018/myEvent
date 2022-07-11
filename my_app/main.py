import sqlalchemy
from fastapi import FastAPI


from my_app.database import DATABASE_URL, my_database
from my_app.routers import users
from my_app.routers import auth
from my_app.tables import metadata


engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

metadata.create_all(engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)


@app.on_event("startup")
async def startup():
    await my_database.connect()


@app.on_event("shutdown")
async def shutdown():
    await my_database.disconnect()

