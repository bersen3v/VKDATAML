import json
from flask import request, Response
from flask import Flask, Response, request
from flask_cors import CORS, cross_origin
from entities.customer.model.customer import Customer
from entities.graph.methods.create_graph_async import create_graph_async
from entities.user.methods.get_friends_list import get_friends_list
from entities.user.methods.get_user_model_by_id import get_user_model_by_id
from shared.db.DBController import db_controller

app = Flask(__name__)
CORS(app)

def long_running_function(id):
    user = get_user_model_by_id(id)
    friends = get_friends_list(user_id=user.id)
    for i in create_graph_async(object_id=user.id, users_list=friends):
        yield f'data: {i}\n\n'

# 303561841
@app.route('/graphstream')
def stream():
    id = request.args.get('id')
    return Response(long_running_function(id), mimetype='text/event-stream')

@app.route('/registration')
async def registration():
    login = request.args.get('login')
    password = request.args.get('password')
    new_customer = Customer(login,password)
    result = await db_controller.add_customer(new_customer)
    return Response(json.dumps({"result": str(result)}))

@app.route('/auth')
async def auth():
    login = request.args.get('login')
    password = request.args.get('password')
    result = await db_controller.auth_customer(login, password)
    return Response(json.dumps({"result": result}))