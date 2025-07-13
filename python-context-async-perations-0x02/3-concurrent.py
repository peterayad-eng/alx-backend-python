import asyncio
import aiosqlite

async def async_fetch_users(db_name):
    async with aiosqlite.connect(db_name) as db:
        async with db.execute("SELECT * FROM users") as cursor:
            users = await cursor.fetchall()
            print("All users:")
            for user in users:
                print(user)
            return users

async def async_fetch_older_users(db_name):
    async with aiosqlite.connect(db_name) as db:
        async with db.execute("SELECT * FROM users WHERE age > 40") as cursor:
            older_users = await cursor.fetchall()
            print("Users older than 40:")
            for user in older_users:
                print(user)
            return older_users

async def fetch_concurrently():
    await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )

db_name = "users.db"

all_users, older_users = asyncio.run(fetch_concurrently(db_name))

