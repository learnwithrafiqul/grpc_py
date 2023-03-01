import grpc
import users_pb2
import users_pb2_grpc
from flask import Flask

app = Flask(__name__)
channel = grpc.insecure_channel('localhost:50051')
stub = users_pb2_grpc.UsersStub(channel)


@app.route('/')
def home():
    return "<h1>Hello World</h1>"


@app.route('/get-users')
def get_users():
    try:
        response = stub.GetUser(users_pb2.GetUsersRequest())
        return str(response)
    except Exception as e:
        return str(e)


@app.route('/create-user')
def create_user():
    try:
        user = users_pb2.User(
            id="2",
            name="Rafiqul Islam",
            email="test@example.com",
            password="password"
        )
        response = stub.CreateUser(users_pb2.CreateUserRequest(
            user=user
        ))
        return str(response)
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port="8081")
