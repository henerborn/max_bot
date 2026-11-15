import aiosqlite
from contextlib import asynccontextmanager


class DatabaseManager:
    def __init__(self, db_path: str):
        self.db_path = db_path

    async def init_db(self) -> None:
        async with aiosqlite.connect(self.db_path) as conn:
            await conn.execute("PRAGMA journal_mode=WAL;")
            version = await conn.execute("PRAGMA user_version;")
            row = await version.fetchone()
            current_version = row[0] if row else 0

            if current_version == 0:
                await conn.execute("""
                    CREATE TABLE IF NOT EXISTS links (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL UNIQUE,
                        url TEXT
                    );
                """)

                await conn.execute("PRAGMA user_version=1;")
                await conn.commit()

    @asynccontextmanager
    async def session(self):
        async with aiosqlite.connect(self.db_path) as conn:
            conn.row_factory = aiosqlite.Row
            async with conn.cursor() as cursor:
                try:
                    yield cursor
                    await conn.commit()
                except Exception as ex:
                    await conn.rollback()
                    raise ex

