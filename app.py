from flask import Flask, request, render_template
from flask_cors import CORS
import pandas as pd


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)
users_data = []
#Lista de Usuários

#Página Inicial
@app.route("/")
def index():
    return 
#Rota que retorna Usuários
@app.route("/users")
def list_users():
    return users_data

@app.route("/users", methods=["POST"])
def create_users():
    input_json = request.json
    ids = len(users_data)

    if ids:
        new_id = len(users_data)+1
    else:
        new_id = 1

    users_data.append({
        "id": new_id,
        "nome": input_json["nome"],
        "email": input_json["email"],
        "senha": input_json["senha"],
        "tipo": input_json["tipo"],
        "materias": input_json["materias"]
    })
    return users_data

@app.route("/auth", methods=["POST"])
def login():
    #caso dê problema - request.form.get("campo")
    email_inserido = request.json["email"]
    senha_inserida = request.json["senha"]
    df = pd.DataFrame.from_records(users_data)
    consulta = df.loc[df['email'] == email_inserido]
    if consulta.empty == False:
        if consulta.iat[0, 3] == senha_inserida:
            return {"message": "Logado"}
        else:
            return {"message": "Senha Incorreta"}
    else:
       return {"message": "Usuario não existe"}

#Rota que adiciona Usuários

#Rota que Deleta Usuários
@app.route("/users/<int:users_id>", methods=["DELETE"])
def delete(users_id: int):
    user = users_data.get(users_id)

    if user:
        del users_data[users_id]
    
    return users_data

@app.route("/users/<int:users_id>", methods=["PUT"])
def updade(users_id:int):
    json = request.json
    name = json.get("name")

    if users_id in users_data:
        users_data[users_id]["name"] = name
    
    return users_data

@app.route("/duvida")
def duvidas():
  duvida = {
    "id_aluno": 0,
    "mensagem": 'meu pau na sua mão',
    "reposta": "",
    "materia": "mat"
  }
  return {"message": "em construção..."}
  
@app.route("/materias")
def list_materias():
  id = request.form.get('id')
  df = pd.DataFrame.from_records(users_data)
  consulta = df.loc[df['id'] == id]
  return consulta.iat[0, 5].to_json(orient='records')

@app.route("/teste")
def  agendar_teste():

  return {"message": "em construção..."}

@app.route("/reforco")
def  agendar_reforco():

  return {"message": "em construção..."}

app.run(host='0.0.0.0', port=5000) 