from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)
users_data = {
 
}
#Lista de Usuários
def response_users():
    return {"users":list(users_data.values())}
#Página Inicial
@app.route("/")
def index():
    return "hello World!"
#Rota que retorna Usuários
@app.route("/users")
def list_users():
    return response_users()
#Rota que adiciona Usuários
@app.route("/users", methods=["POST"])
def create_users():
    json = request.json

    ids = list(users_data.keys())

    if ids:
        new_id = ids[-1] +1
    else:
        new_id = 1

    users_data[new_id] = {
        "id": new_id,
        "User":json["User"]
        #"name": json["name"],
        #"email":json["email"],
        #"senha":json["senha"],
        #"auth" : json["auth"],
        #"userType": json["userType"],
        #"materias": json["materias"]
    }
    return response_users()
#Rota que Deleta Usuários
@app.route("/users/<int:users_id>", methods=["DELETE"])
def delete(users_id: int):
    user = users_data.get(users_id)

    if user:
        del users_data[users_id]
    
    return response_users()

@app.route("/users/<int:users_id>", methods=["PUT"])
def updade(users_id:int):
    json = request.json
    name = json.get("name")

    if users_id in users_data:
        users_data[users_id]["name"] = name
    
    return response_users()