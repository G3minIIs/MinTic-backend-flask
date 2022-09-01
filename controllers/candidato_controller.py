from db.candidato_repository import CandidatoRepository
from models.candidato_model import CandidatoModel
from db.partido_repository import PartidoRepository
from models.partido_model import PartidoModel
from routes.partido_route import partido_Module
from controllers.partido_controller import PartidoController

class CandidatoController():
    
    def __init__(self):
        self.repo = CandidatoRepository()
        self.repo_partido = PartidoRepository()
        
    def get(self): 
            return self.repo.get_all()
    def getById(self,id): #metodo para ver un candidato mediante el id
        return self.repo.get_by_id(id) 
    def create(self,data): # creamos el candidato , partido_id
        candidato = CandidatoModel(data) #creamos candidato
        '''partido = self.repo_partido.get_by_id(partido_id) #partido_id
        candidato.partido = PartidoModel(partido)'''
        return {
            "id":self.repo.save(candidato) #llamamos al repo en el metodo Save
        }
    def update(self, id,  data): #llamamos update y pasamos los valores
        candidato = CandidatoModel(data) 
        self.repo.update(id, candidato) 
    def delete(self,id): #llamamos Delete y pasamos ID
        return self.repo.delete(id) 