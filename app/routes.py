import json
from flask import Flask, Response, request, url_for, send_file
from flask_cors import CORS, cross_origin
from entities.customer.model.customer import Customer
from entities.graph.methods.create_graph_async import create_graph_async
from entities.user.methods.get_friends_list import get_friends_list
from entities.user.methods.get_user_model_by_id import get_user_model_by_id
from shared.db.DBController import db_controller


app = Flask(__name__)
CORS(app)

def long_running_function(id, customer_id):
    user = get_user_model_by_id(id)
    friends = get_friends_list(user_id=user.id)
    for i in create_graph_async(customer_id=customer_id, object_id=user.id, users_list=friends):
        yield f'data: {i}\n\n'

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Methods'] = '*'
    return response

# 303561841
@app.route('/graphstream')
async def stream():
    id = request.args.get('id')
    customer_id = request.args.get('customer_id')
    return Response(long_running_function(id, customer_id), mimetype='text/event-stream')

@app.route('/registration')
async def registration():
    login = request.args.get('login')
    password = request.args.get('password')
    new_customer = Customer(None, login,password)
    result = await db_controller.add_customer(new_customer)
    return Response(json.dumps({"result": str(result)}))

@app.route('/auth')
async def auth():
    login = request.args.get('login')
    password = request.args.get('password')
    result = await db_controller.auth_customer(login, password)
    return Response(json.dumps({"result": result}))

@app.route('/history')
async def history():
    customer_id = request.args.get('customer_id')
    result = await db_controller.get_graph_history(customer_id)
    return Response(json.dumps({"result": result}))


@app.route('/addcustomer', methods=['POST'])
async def addcustomer():
    login = request.form.get('login')
    password = request.form.get('password')
    path = '/get_photo?uri=static/photos/default.png'

    if 'photo' in request.files:
        photo = request.files['photo']
        photo.save('../static/photos/' + photo.filename)
        path = '/get_photo?uri=static/photos/' + photo.filename


    new_customer = Customer(path, login, password)
    result = await db_controller.add_customer(new_customer)

    return Response(json.dumps({"result": result}))


@app.route('/getcustomers')
async def get_customers():
    result = await db_controller.get_customers()
    return Response(json.dumps({"result": result}))

@app.route('/get_photo_uri')
def get_photo_uri():
    photo_path = request.args.get('photo_path')

    if photo_path:
        photo_uri = url_for('static', filename='photos/' + photo_path, _external=True)
        return Response(json.dumps({'photo_uri': photo_uri}))

@app.route('/get_photo')
def get_photo():
    photo_uri = request.args.get('uri')
    return send_file('../' + photo_uri, mimetype='image/jpeg')

