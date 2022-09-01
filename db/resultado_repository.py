from models.resultado_model import ResultadoModel
from db.repository import Repository

class ResultadoRepository(Repository[ResultadoModel]):
    def __init__(self):
        super().__init__()