from http import HTTPStatus
from app import app, mongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request


@app.route("/") #mapear o recurso
def contexto_app():
    #retoro uma string que quero apresentar na tela
    # codigo http - 200 - ok
    return "Bem vindo ao CRUD de pessoa ", HTTPStatus.OK

@app.route('/pessoa', methods=['POST'])
def salvar_pessoa():
	_json = request.json
	_nome = _json['nome']
	_idade = _json['idade']
	_endereco = _json['endereco']
	_email = _json['email']
	_telefone = _json['telefone']
	_cpf = _json["cpf"]
	# valida valores recebidos
	if _nome and _email and _idade and _endereco and _telefone and _cpf and request.method == 'POST':

		id = mongo.db.pessoa.insert({'nome': _nome, 'idade': _idade, 'endereco': _endereco, 'email': _email, 'telefone': _telefone, 'cpf': _cpf})
		resp = jsonify('Usuário cadastrado com successo!')
		resp.status_code = 200
		return resp
	else:
		return not_found()


@app.route("/pessoas", methods=['GET'])
def listar_pessoas():
	pessoas = mongo.db.pessoa.find()
	resp = dumps(pessoas)
	return resp


@app.route("/pessoa/<id>", methods=['GET']) #get sempre listagem
def listar_by_id(id):
	pessoa = mongo.db.pessoa.find_one({'_id': ObjectId(id)})
	resp = dumps(pessoa)
	return resp


@app.route('/update', methods=['PUT'])
def update_pessoa():
	_json = request.json
	_id = _json['_id']
	_nome = _json['nome']
	_idade = _json['idade']
	_endereco = _json['endereco']
	_email = _json['email']
	_telefone = _json['telefone']
	_cpf = _json['cpf']
	# valida valores recebido
	if _nome and _email and _idade and _endereco and _telefone and _cpf and _id and request.method == 'PUT':

		mongo.db.pessoa.update_one({'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, {'$set': {'nome': _nome, 'idade': _idade, 'endereco': _endereco, 'email': _email, 'telefone': _telefone, 'cpf': _cpf}})
		resp = jsonify('Pessoa atualizada com successo!')
		resp.status_code = 200
		return resp
	else:
		return not_found()


@app.route('/delete/<id>', methods=['DELETE'])
def delete_pessoa(id):
	mongo.db.pessoa.delete_one({'_id': ObjectId(id)})
	resp = jsonify('Usuário deletado com successo!')
	resp.status_code = 200
	return resp

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

if __name__ == "__main__":
    app.run()
