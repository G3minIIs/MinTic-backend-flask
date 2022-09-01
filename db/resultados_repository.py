from models.resultados_model import ResultadosModel
from db.repository import Repository

class ResultadosRepository(Repository[ResultadosModel]):
    def _init_(self):
        super()._init_()