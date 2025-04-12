import asyncio

from app.routes import app
from entities.graph.methods.create_graph_async import create_graph_async
from entities.user.methods.get_friends_list import get_friends_list
from entities.user.methods.get_user_model_by_id import get_user_model_by_id
from shared.db.DBController import db_controller


async def main() -> None:
    await db_controller.create_tables()
    app.run(debug=True)


if __name__ == '__main__':
    asyncio.run(main())
