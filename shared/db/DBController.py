import json
import aiosqlite
import pickle


from entities.customer.model.customer import Customer
from shared.db.dbconfig import DB, C, T

class DBController:

    def __init__(self) -> None:
        self.database_path = DB.main

    async def create_tables(self) -> None:
        async with aiosqlite.connect(self.database_path) as connection:
            await connection.execute(f'''
                CREATE TABLE IF NOT EXISTS {T.customers} (
                    {C.photo} TEXT,
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
                     {C.trace} TEXT PRIMARY KEY,
                     {C.id} TEXT,
                     {C.vk_username} TEXT,
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

    async def add_graph_to_history(self, trace, customer_id: str, vk_username, graph):
        data = pickle.dumps(graph)

        async with aiosqlite.connect(self.database_path) as connection:
            await connection.execute(f'''
                REPLACE INTO history 
                ({C.trace}, {C.id}, {C.vk_username}, {C.query_data}) 
                VALUES (?, ?, ?, ?)
            ''', (str(trace), customer_id, vk_username, data))
            await connection.commit()
        return True

    async def get_graph_history(self, customer_id: str):
        async with aiosqlite.connect(self.database_path) as connection:
            cursor = await connection.execute(f'''
                   SELECT * from {T.history} WHERE {C.id} == '{customer_id}'
                       ''')
            row = await cursor.fetchall()
            await connection.commit()
            if row:
                res = []
                for t in row:
                    res.append(pickle.loads(t[3]))
                return res
            return None


    async def add_customer(self, customer: Customer):
        user_in_db = await self.check_customer(customer.login)
        if not user_in_db:
            async with aiosqlite.connect(self.database_path) as connection:
                await connection.execute(f'''
                     INSERT INTO {T.customers} 
                       ({C.photo}, {C.login}, {C.password}, {C.id}) 
                       VALUES (?,?,?,?)
                ''', (customer.photo, customer.login, customer.password, str(customer.id)))
                await connection.commit()
            return str(customer.id)
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

    async def get_customers(self):
        async with aiosqlite.connect(self.database_path) as connection:
            cursor = await connection.execute(f'''
                   SELECT * from {T.customers}
               ''')
            row = await cursor.fetchall()
            await connection.commit()

            customers_list = []
            for customer in row:
                customer_data = {
                    "photo": str(customer[0]),
                    "login": str(customer[1]),
                    "password": str(customer[2]),
                    "id": str(customer[3])
                }
                customers_list.append(customer_data)

            if customers_list:
                return customers_list

        return None


db_controller = DBController()
