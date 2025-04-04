import asyncio

from app.routes import app
from shared.db.DBController import db_controller

async def main() -> None:
    await db_controller.create_tables()
    app.run(debug=True)

if __name__ == '__main__':
    asyncio.run(main())
