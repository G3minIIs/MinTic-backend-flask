import json
from typing_extensions import Self
from urllib import request
from flask import jsonify, request, Blueprint
from controllers.candidato_controller import CandidatoController

candidato_Module = Blueprint('candidato', __name__) #lo establecemos como app de blue print (coleccion de rutas)
controller = CandidatoController() #establecemos el controlador

@candidato_Module.get('/') #aca tenemos metodo show all
def get_candidato():
    return jsonify(controller.get())

            #creamos el crud

@candidato_Module.post('/<string:partido_id>') #metodo crear
def create_candidato(partido_id):
    return jsonify(controller.create(request.get_json(), partido_id)), 201

@candidato_Module.get('/<string:id>') #metodo listar por ID
def ver_candidato(id):
    return jsonify(controller.getById(id))

@candidato_Module.put('/<string:id>') #metodo actualizar
def upd_candidato(id):
    controller.update(id, request.get_json())
    return jsonify({}), 204

@candidato_Module.delete('/<string:id>') #metodo eliminar
def del_candidato(id):
    controller.delete(id)
    return jsonify({}), 204