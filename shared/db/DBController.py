import json
import aiosqlite

from entities.customer.model.customer import Customer
from shared.db.dbconfig import DB, C, T

class DBController:

    def __init__(self) -> None:
        self.database_path = DB.main

    async def create_tables(self) -> None:
        async with aiosqlite.connect(self.database_path) as connection:
            await connection.execute(f'''
                CREATE TABLE IF NOT EXISTS {T.customers} (
                    {C.login} TEXT, 
                    {C.password} TEXT,
                    {C.id} TEXT PRIMARY KEY
                )
            ''')
            await connection.execute(f'''
                  CREATE TABLE IF NOT EXISTS {T.admins} (
                      {C.id} TEXT PRIMARY KEY
                  )
           ''')
            await connection.execute(f'''
                 CREATE TABLE IF NOT EXISTS {T.history} (
                     {C.id} TEXT PRIMARY KEY,
                     {C.query_data} BLOB
                 )
             ''')
            await connection.commit()

    async def check_customer(self, login: str):
        async with aiosqlite.connect(self.database_path) as connection:
            cursor = await connection.execute(f'''
                   SELECT * from {T.customers} WHERE {C.login} == '{login}'
               ''')
            await connection.commit()
            row = await cursor.fetchone()

            if row:
                return Customer(*row)
            return None

    async def add_customer(self, customer: Customer):
        user_in_db = await self.check_customer(customer.login)
        if not user_in_db:
            async with aiosqlite.connect(self.database_path) as connection:
                await connection.execute(f'''
                     INSERT INTO {T.customers} 
                       ({C.login}, {C.password}, {C.id}) 
                       VALUES ('{customer.login}', '{customer.password}', '{customer.id}')
                ''')
                await connection.commit()
            return customer.id
        return False

    async def auth_customer(self, login: str, password: str):
        async with aiosqlite.connect(self.database_path) as connection:
            cursor = await connection.execute(f'''
                SELECT * from {T.customers} WHERE {C.login} == '{login}' AND {C.password} == '{password}'
            ''')
            row = await cursor.fetchone()
            await connection.commit()

            if row:
                return Customer(*row).id
            return None

db_controller = DBController()
