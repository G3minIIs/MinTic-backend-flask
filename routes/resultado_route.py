from flask import jsonify,request, Blueprint
from controllers.resultado_controller import ResultadoController



#lo establecemos como app de blue print (coleccion de rutas)
resultado_Module = Blueprint('resultado',__name__)

#establecemos el controlador
controller = ResultadoController()

@resultado_Module.get('/') #aca tenemos el listar
def get_resultado():
    return jsonify(controller.get())

@resultado_Module.post('/mesa/<string:mesa_id>/candidato/<string:candidato_id>') #Crear
def createResultado(mesa_id,candidato_id):
    result = controller.create(request.get_json(), mesa_id,candidato_id)
    return jsonify(result), 201


@resultado_Module.get('/<string:id>') #listar por ID
def ver_resultado(id):
    return jsonify(controller.getById(id))


@resultado_Module.put('/<string:id>')#actualizar
def upd_resultado(id):
    controller.update(id, request.get_json())
    return jsonify({}), 204


@resultado_Module.delete('/<string:id>')#eliminar
def del_resultado(id):
    controller.delete(id)
    return jsonify({}), 204

                    # rutas de reportes
                    
@resultado_Module.get('/reportes/total') #listar todos resultados de los candidatos
def get_reporte_total():
    return jsonify(controller.get_total())

@resultado_Module.get('/reportes/total/mesa') #total de cada uno de los candidatos por mesa
def get_reporte_mesa():
    return jsonify(controller.get_total_mesa(request.args.to_dict()))

@resultado_Module.get('/reportes/total/candidato') #aca tenemos el total de votos por candidato
def get_reporte_votos_candidato():
    return jsonify(controller.get_total_candidato(request.args.to_dict()))


@resultado_Module.get('/reportes/total/mesa/candidato') #aca tenemos el total de votos de candidato en una mesa
def get_reporte_candidato_mesa():
    return jsonify(controller.get_total_mesa_candidato(request.args.to_dict()))
