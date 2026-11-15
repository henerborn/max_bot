import sqlite3
import logging
from database.manager import DatabaseManager

logger = logging.getLogger(__name__)

class LinksRepository:
    def __init__(self, db_manager: DatabaseManager):
        self._db = db_manager

    async def new_url(self, title: str, url: str):
        try:
            async with self._db.session() as cursor:
                await cursor.execute(
                    "INSERT INTO links (title, url) VALUES (?, ?)",
                    (title, url)
                )
                return True
        except sqlite3.IntegrityError as ex:
            logger.info(f"A record with title '{title}' is already exists")
            await self.update_url(title, url)

    async def update_title(self, old_title: str, new_title: str) -> str | None:
        async with self._db.session() as cursor:
            await cursor.execute(
                "UPDATE links SET title = ? WHERE title = ?",
                (new_title, old_title)
            )
            await cursor.execute("SELECT title FROM links WHERE title = ?", (new_title, ))
            row = await cursor.fetchone()
        logger.info(f"Title '{old_title}' succefully changed on '{new_title}'")
        return row["title"] if row else None

        
    async def update_url(self, title: str, url: str) -> str:
        async with self._db.session() as cursor:
            await cursor.execute(
                "UPDATE links SET url = ? WHERE title = ?",
                (url, title)
            )
            await cursor.execute("SELECT url FROM links WHERE title = ?", (title, ))
            row = await cursor.fetchone()
        logger.info(f"'{title}' - {url}")
        return row["url"] if row else None


    async def get_url(self, title: str) -> str | None:
        async with self._db.session() as cursor:
            await cursor.execute("SELECT url FROM links WHERE title = ?", (title,))
            row = await cursor.fetchone()
        return row["url"] if row else None


    async def delete_url(self, title: str):
        async with self._db.session() as cursor:
            await cursor.execute("DELETE FROM links WHERE title = ?", (title,))


