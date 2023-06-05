# Importar módulo MongoClient de pymongo
from pymongo import MongoClient

# Crear conexión a la base de datos
client = MongoClient('mongodb://localhost:27017/')
db = client['musicprodata']
usuarios = db['usuarios']
productos = db['productos']




