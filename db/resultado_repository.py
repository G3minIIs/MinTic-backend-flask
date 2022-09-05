from array import array
from unittest import result
from models.resultado_model import ResultadoModel
from db.repository import Repository
from bson import ObjectId

class ResultadoRepository(Repository[ResultadoModel]):
    def __init__(self):
        super().__init__()
        
    def total(self): #obtener total de resultados
        data = self.get_all()
        result = {"results": {}}
        for register in data:
            if register["candidato"]["nombre"] + " " + register["candidato"]["apellido"] not in result["results"]:
                result["results"].update({register["candidato"]["nombre"] + " " + register["candidato"]["apellido"]:1})
            else:
                result["results"][register["candidato"]["nombre"] + " " + register["candidato"]["apellido"]] +=  1
        return result
    
    def total_mesa(self, mesa_id): #obtener total de resultados por mesa
        filter = {"mesa.$id": ObjectId(mesa_id)}
        data = self.query(filter)
        result = {}
        for register in data:
            if "mesa" not in result:
                result["mesa"] = register["mesa"] ["numero_mesa"]
                result["_id"] = register["mesa"] ["_id"]
                result["results"] = {}      
            if register["candidato"]["nombre"] + " " + register["candidato"]["apellido"] not in result["results"]:
                result["results"].update({register["candidato"]["nombre"] + " " + register["candidato"]["apellido"]:1})
            else:
                result["results"][register["candidato"]["nombre"] + " " + register["candidato"]["apellido"]] +=  1
        return result

    def total_candidato(self, candidato_id): # obtener el total de resultados por candidato
        filter = {"candidato.$id": ObjectId(candidato_id)}
        data = self.query(filter)
        result = {}
        for register in data:      
            if register["candidato"]["nombre"] + " " + register["candidato"]["apellido"] not in result:
                result.update({register["candidato"]["nombre"] + " " + register["candidato"]["apellido"]:1})
            else:
                result[register["candidato"]["nombre"] + " " + register["candidato"]["apellido"]] +=  1
        return result

    def total_mesa_candidato(self, mesa_id, candidato_id): # total de votos de candidato por mesa
        filter = {"$and": [
            {"mesa.$id": ObjectId(mesa_id)},
            {"candidato.$id": ObjectId(candidato_id)}]} 
        data = self.query(filter)
        result = {}
        for register in data:
            if "mesa" not in result:
                result["mesa"] = register["mesa"] ["numero_mesa"]
                result["_id"] = register["mesa"] ["_id"]
                result["results"] = {}      
            if register["candidato"]["nombre"] + " " + register["candidato"]["apellido"] not in result["results"]:
                result["results"].update({register["candidato"]["nombre"] + " " + register["candidato"]["apellido"]:1})
            else:
                result["results"][register["candidato"]["nombre"] + " " + register["candidato"]["apellido"]] +=  1
        return result