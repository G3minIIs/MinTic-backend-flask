from db.resultado_repository import ResultadoRepository
from db.mesa_repository import MesaRepository
from db.candidato_repository import CandidatoRepository
from db.partido_repository import PartidoRepository

from models.partido_model import PartidoModel
from models.resultado_model import ResultadoModel
from models.mesa_model import MesaModel
from models.candidato_model import CandidatoModel


class ResultadoController():

    def __init__(self):
        self.repo = ResultadoRepository()
        self.repo_mesa = MesaRepository()
        self.repo_candidato = CandidatoRepository()
        self.repo_partido = PartidoRepository()
        
    def get(self):
        return self.repo.get_all()

    def getById(self, id):
        return self.repo.get_by_id(id)

    def create(self, data, mesa_id, candidato_id):
        resultado = ResultadoModel(data)  # creamos Resultado
        mesa = self.repo_mesa.get_by_id(mesa_id)
        resultado.mesa = MesaModel(mesa)

        candidato = self.repo_candidato.get_by_id(candidato_id)
        resultado.candidato = CandidatoModel(candidato)

        return {
            # llamamos al repo en el metodo Save
            "id": self.repo.save(resultado)
        }

    def update(self, id,  data):
        resultado = ResultadoModel(data)  # cremos Resultado
        # llamamos update y pasamos los valores
        self.repo.update(id, resultado)

    def delete(self, id):
        return self.repo.delete(id)  # llamamos Delete y pasamos ID

                 # consultas de resultados

    def get_total(self):
        return self.repo.total()

    def get_total_mesa(self, args):
        return self.repo.total_mesa(args['mesa_id'])

    def get_total_candidato(self, args):
        return self.repo.total_candidato(args['candidato_id'])

    def get_total_mesa_candidato(self, args):
        return self.repo.total_mesa_candidato(args['mesa_id'], args['candidato_id'])

'''
    # resultados de resultado_repository.py

def total(self): #obtener total de resultados
    pass

def total_mesa(self, mesa_id): #obtener total de resultados por mesa
    pass

def total_candidato(self, candidato_id):
    pass

def total_partido(self, partido_id):
    pass

def total_mesa_candidato(self, mesa_id, candidato_id):
    pass

def total_mesa_partido(self, mesa_id, partido_id):
    pass

'''