from typing import Any, Iterable, Optional
import aiomysql

class Connection:
    """A thin wrapper around an aiomysql connection offering a nicer API (imo)."""

    __slots__ = (
        "_conn",
    )

    def __init__(self, conn: aiomysql.Connection) -> None:
        """Creates an instance of `Connection` from an aiomysql connection."""

        self._conn = conn
    
    async def execute(self, query: str, args: Iterable[Any] = ()) -> Optional[int]:
        """Executes `query` on a new cursor, returning lastrowid."""

        async with self._conn.cursor() as cur:
            await cur.execute(query, args)
            return cur.lastrowid
    
    async def fetchall(self, query: str, args: Iterable[Any] = ()) -> tuple[dict[str, Any]]:
        """Executes `query` on a new cursor, returning all results."""

        async with self._conn.cursor(aiomysql.DictCursor) as cur:
            await cur.execute(query, args)
            return await cur.fetchall()
    
    async def fetchone(self, query: str, args: Iterable[Any] = ()) -> Optional[dict[str, Any]]:
        """Executes `query` on a new cursor, returning the first result."""

        async with self._conn.cursor(aiomysql.DictCursor) as cur:
            await cur.execute(query, args)
            return await cur.fetchone()
    
    async def fetchcol(self, query: str, args: Iterable[Any] = ()) -> Optional[Any]:
        """Fetches the first column of the first result."""

        async with self._conn.cursor() as cur:
            await cur.execute(query, args)
            res = await cur.fetchone()
            
            return res[0] if res else None
