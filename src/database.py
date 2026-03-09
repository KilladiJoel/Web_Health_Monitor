import aiosqlite
from datetime import datetime
class DatabaseManager:
    def __init__(self,db_name : str="sentinel.db"):
        self.db_name=db_name
    async def setup_db(self):
        async with aiosqlite.connect(self.db_name) as db:
            await db.execute("""CREATE TABLE IF NOT EXISTS RESULT(id INTEGER PRIMARY KEY AUTOINCREMENT,
                             url TEXT NOT NULL,
                             status TEXT NOT NULL,
                             http_code INTEGER,
                             timestamp TEXT NOT NULL)""")
            await db.commit()
    async def save_result(self,url : str,status : str,http_code : int,timestamp : str):
        async with aiosqlite.connect(self.db_name) as db:
            await db.execute("""INSERT INTO RESULT (url,status,http_code,timestamp) VALUES (?,?,?,?)""",
                             (url,status,http_code,timestamp))
            await db.commit()
    async def get_all_results(self):
        async with aiosqlite.connect(self.db) as db:
            async with db.execute("""SELECT * FROM RESULT ORDER BY id DESC""") as cursor:
                rows = await cursor.fetchall()
                return rows