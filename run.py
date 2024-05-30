#Import
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config #importamos el archivo de configuración "config.py"

#Instancias
app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy (app)

#Rutas
@app.route('/')
def inicio():
    return ('Hola esta es la pagina de inicio')

#Run
if __name__ == '__main__':
    app.run(debug=True)