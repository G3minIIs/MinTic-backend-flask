from db.resultados_repository import ResultadosRepository
from db.mesa_repository import MesaRepository
from db.candidato_repository import CandidatoRepository
from models.resultados_model import ResultadosModel
from models.mesa_model import MesaModel
from models.candidato_model import CandidatoModel

class ResultadosController():
  
  def _init_(self):
    self.repo = ResultadosRepository()
    self.repo_mesa = MesaRepository()
    self.repo_candidato = CandidatoRepository()
  
  def get(self):
      return self.repo.get_all()
  
  def get_by_id(self,id):
    return self.repo.get_by_id(id)
  
  def create(self, data, mesa_id, candidato_id):
    resultados = ResultadosModel(data)
    candidato = self.repo_candidato.get_by_id(candidato_id) 
    resultados.candidato = CandidatoModel(candidato)
    mesa = self.repo_mesas.get_by_id(mesa_id)
    resultados.mesa = MesaModel(mesa) 
    return self.repo.save(resultados)
  
  def update(self,id, data):
    resultados = ResultadosModel(data)
    self.repo.update(id, resultados)
  
  def delete(self,id):
    self.repo.delete(id)