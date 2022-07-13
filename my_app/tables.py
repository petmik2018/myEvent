import sqlalchemy

from my_app.database import metadata


users_table = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("user_email", sqlalchemy.String(64), unique=True),
    sqlalchemy.Column("hashed_password", sqlalchemy.String()),
    sqlalchemy.Column("is_superuser", sqlalchemy.Boolean)
)
