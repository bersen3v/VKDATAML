from flask import Flask, Response, request
from flask_cors import CORS, cross_origin
from entities.graph.methods.create_graph_async import create_graph_async
from entities.user.methods.get_friends_list import get_friends_list
from entities.user.methods.get_user_model_by_id import get_user_model_by_id

app = Flask(__name__)
CORS(app)

def long_running_function(id):
    user = get_user_model_by_id(id)
    friends = get_friends_list(user_id=user.id)
    for i in create_graph_async(object_id=user.id, users_list=friends):
        yield f'data: {i}\n\n'

# 303561841
@app.route('/stream')
def stream():
    id = request.args.get('id')
    return Response(long_running_function(id), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)