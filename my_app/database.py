import sqlalchemy
import databases

metadata = sqlalchemy.MetaData()

DATABASE_URL = "sqlite:///./sqlite.db"

my_database = databases.Database(DATABASE_URL)
