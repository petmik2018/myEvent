from fastapi import HTTPException

from my_app.database import my_database
from my_app import security, schemas, tables
from my_app.tables import users_table


async def read_users():
    query = users_table.select()
    return await my_database.fetch_all(query=query)



