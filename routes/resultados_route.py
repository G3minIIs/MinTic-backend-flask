from flask import jsonify,request, Blueprint
from controllers.resultados_controller import ResultadosController
from routes.mesa_route import mesa_Module

resultados_module = Blueprint('resultados', __name__)
controller = ResultadosController()

@resultados_module.get('/')
#@logger
def get_resultados(): 
    return jsonify(controller.get())

@resultados_module.get('/<string:id>')
def showresultados(id): 
    return jsonify(controller.get_by_id(id))

@resultados_module.post('/mesa/<string:mesa_id>/candidato/<string:candidato_id>')
#@logger
def create_resultados(mesa_id, candidato_id):
  return jsonify(controller.create(request.get_json(), mesa_id, candidato_id)), 201
  
@resultados_module.put('/<string:id>')
def update_user(id):
  controller.update(id, request.get_json())
  return jsonify({}), 204
  
@resultados_module.delete('/<string:id>')
def delete_resultados(id):
  controller.delete(id)
  return jsonify({}), 204