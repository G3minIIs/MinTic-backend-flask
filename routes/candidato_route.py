import json
from urllib import request
from flask import jsonify, request, Blueprint
from controllers.candidato_controller import CandidatoController

#lo establecemos como app de blue print (coleccion de rutas)
candidato_Module = Blueprint('candidato', __name__)
#establecemos el controlador
controller = CandidatoController()

@candidato_Module.get('/') #aca tenemos metodo show
def get_candidato():
    return jsonify(controller.get())

            #creamos el crud

@candidato_Module.post('/') # metodo crear "partido/<string:partido_id>
def create_candidato(): #partido_id
    result = controller.create(request.get_json())
    return jsonify(result), 201 #, partido_id


@candidato_Module.get('/<string:id>') #listar por ID
def ver_candidato(id):
    return jsonify(controller.getById(id))


@candidato_Module.put('/<string:id>')#actualizar
def upd_candidato(id):
    controller.update(id, request.get_json())
    return jsonify({}), 204


@candidato_Module.delete('/<string:id>')#eliminar
def del_candidato(id):
    controller.delete(id)
    return jsonify({}), 204