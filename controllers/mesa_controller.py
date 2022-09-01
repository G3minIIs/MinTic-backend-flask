from models.mesa_model import MesaModel
from db.mesa_repository import MesaRepository

class MesaController():
    
    def __init__(self):
        self.repo = MesaRepository()  
    def get(self): # metodo get all para mostrar todo
        return self.repo.get_all() 
    def getById(self,id): #metodo para buscar una mesa por id
        return self.repo.get_by_id(id)  
    def create(self,data): #creamos Mesa xd
        mesa = MesaModel(data)
        return {
            "id":self.repo.save(mesa) #llamamos al repo en el metodo Save
        }
    def update(self, id,  data): #llamamos update y pasamos los valores
        mesa = MesaModel(data) 
        self.repo.update(id, mesa)
    def delete(self,id): #llamamos Delete y pasamos ID
        return self.repo.delete(id) 