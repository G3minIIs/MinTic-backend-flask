from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import dotenv_values
#importando los modulos de las rutas
from routes.mesa_route import mesa_Module
from routes.partido_route import partido_Module
from routes.candidato_route import candidato_Module
from routes.resultado_route import resultado_Module

config = dotenv_values('.env') #instanciamos las variables de entonro
app = Flask(__name__)
cors = CORS(app)

# registramos los Blue prints para las rutas
app.register_blueprint(mesa_Module, url_prefix="/mesa")
app.register_blueprint(partido_Module,url_prefix="/partido")
app.register_blueprint(candidato_Module, url_prefix="/candidato")
app.register_blueprint(resultado_Module, url_prefix="/resultado")

@app.route('/')
def hello_word():
    dictToReturn = {'message': 'what do you mean?'}
    return jsonify(dictToReturn)


if __name__ == '__main__':
    app.run(host='localhost', port=config["PORT"], debug=True)
