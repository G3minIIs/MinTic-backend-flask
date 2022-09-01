from flask import jsonify, request, Blueprint
from controllers.mesa_controller import MesaController

mesa_Module = Blueprint('mesa',__name__) #lo establecemos como app de blue print (coleccion de rutas)

controller = MesaController() #establecemos el controlador

@mesa_Module.get('/') # para ver todas las mesas
def get_mesas():
    return jsonify(controller.get())

@mesa_Module.post('/') # metodo crear mesas
def createMesas():
    result = controller.create(request.get_json())
    return jsonify(result), 201

@mesa_Module.get('/<string:id>') # metodo listar por ID
def ver_mesa(id):
    return jsonify(controller.getById(id))

@mesa_Module.put('/<string:id>')# metodo actualizar
def upd_mesa(id):
    controller.update(id, request.get_json())
    return jsonify({}), 204

@mesa_Module.delete('/<string:id>')# metodo eliminar
def del_mesa(id):
    controller.delete(id)
    return jsonify({}), 204