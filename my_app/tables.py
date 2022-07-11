import sqlalchemy

from my_app.database import metadata


users_table = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("username", sqlalchemy.String(64), unique=True),
    sqlalchemy.Column("password", sqlalchemy.String()),
)
