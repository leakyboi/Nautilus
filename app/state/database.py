from app.db.mysql import Connection
from .config import config
import aiomysql

sql_pool: aiomysql.Pool

async def create_mysql_pool() -> None:
    """Establishes a connection to the MySQL database, creating a connection pool."""

    global sql_pool
    
    sql_pool = await aiomysql.create_pool(
        pool_recycle= False,
        host= config.SQL_HOST,
        port= config.SQL_PORT,
        user= config.SQL_USER,
        db= config.SQL_DB,
        password= config.SQL_PASS,
    )
