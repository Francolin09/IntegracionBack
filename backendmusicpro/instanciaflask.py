from flask import Flask, jsonify, request
from conexionmongodb import usuarios,productos
from flask_cors import CORS
musicpro = Flask(__name__)
CORS(musicpro, resources={r"/*": {"origins": "*"}}, methods=["GET", "PUT", "POST"])
@musicpro.route('/')
def home():
    return 'Bienvenido a mi tienda!'

#<------------------------------------------------------INICIO SECTOR DE USUARIOS------------------------------------------------------------>
@musicpro.route('/usuarios', methods=['POST']) # esto es solo prueba
def agregar_usuario():
    usu= request.json
    usuarios.insert_one(usu)
    #return (f"se agrego el nuevo usuario con el nombre {usu['nombre_usuario']}")
    

@musicpro.route('/usuarios', methods=['GET'])
def get_usuarios():
    # Obtener todos los documentos de la colección "usuarios"
    resultado = []
    for usuario in usuarios.find():
        resultado.append({
            "rut": usuario["rut"],
            "nombre_usuario": usuario["nombre_usuario"],
            "correo_usuario": usuario["correo_usuario"],
            "password": usuario["password"]
        })
    # Retornar los resultados en formato JSON
    return jsonify(resultado)

@musicpro.route('/usuarios/<string:rut>', methods=['GET'])
def get_usuario(rut):

    # utilizando la instancia usuarios, se busca un usuario que tenga el rut consultado
    usuario = usuarios.find_one({'rut': rut})

    # utilizamos un if para ver si existe el usuario con el rut especificado
    if usuario:
        # Si el usuario existe, devolver su información en formato JSON
        return jsonify(f"se encontro al usuario. es {usuario['nombre_usuario']} con el correo {usuario['correo_usuario']}"), 200
    else:
        # Si el usuario no existe, devolver un mensaje de error en formato JSON
        return jsonify({'mensaje': 'Usuario no encontrado'}), 404

@musicpro.route('/usuarios/<string:rut>', methods=['PUT']) #revisar porqué no funciona con PUT
def editar_usuario(rut):
    usuario = usuarios.find_one({"rut": rut})
    if usuario:
        usuarios.update_one({"rut": rut}, {"$set": {"nombre_usuario": "editadoXD", "correo_usuario": "editadoXD", "password": "editadoXD"}})
        return "Usuario editado exitosamente"
    else:
        return "Usuario no encontrado"
    
@musicpro.route('/usuarios/<string:rut>', methods=['DELETE'])
def eliminar_usuario(rut):
    usuario = usuarios.find_one({"rut": rut})
    if usuario:
        usuarios.delete_one({"rut": rut})
        return "Usuario borrado exitosamente"
    else:
        return "No se encontró el usuario"
#<------------------------------------------------------FIN SECTOR DE USUARIOS------------------------------------------------------------>




#<------------------------------------------------------INICIO SECTOR DE PRODUCTOS------------------------------------------------------------>
@musicpro.route('/productos/nuevo/agregar', methods=['POST']) # esto es solo prueba
def agregar_producto():
    prod= request.json
    productos.insert_one(prod)
    return (f"se agrego el nuevo producto con el id {prod['id_producto']}")

@musicpro.route('/productos', methods=['GET'])
def get_productos():
    # Obtener todos los documentos de la colección "productos"
    resultado = []
    for producto in productos.find():
        resultado.append({
            "id_producto": producto["id_producto"],
            "categoria": producto["categoria"],
            "nombre": producto["nombre"],
            "precio": producto["precio"],
            "stock": producto["stock"],
            "img": producto["img"]
        })
    # Retornar los resultados en formato JSON
    return jsonify(resultado)

@musicpro.route('/productos/<int:id_producto>', methods=['GET'])
def get_producto(id_producto):

    # utilizando la instancia productos, se busca un usuario que tenga el rut consultado
    producto = productos.find_one({'id_producto': id_producto})

    # utilizamos un if para ver si existe el producto con el id especificado
    if producto:
        # Si el producto existe, devolver su información en formato JSON
        return jsonify(f"se encontro el producto. es {producto['nombre']} con precio de {producto['precio']}"), 200
    else:
        # Si el producto no existe, devolver un mensaje de error en formato JSON
        return jsonify({'mensaje': 'producto no encontrado'}), 404

@musicpro.route('/productos/editar/<int:id_producto>', methods=['PUT']) 
def editar_producto(id_producto):
    producto = productos.find_one({'id_producto': id_producto})
    if producto:
        productos.update_one({'id_producto': id_producto}, {"$set": {"categoria": "editado", "nombre": "editado", "precio":999, "stock":999,"categoria": "editado"}})
        return "Producto editado exitosamente"
    else:
        return "Producto no encontrado xd"


#<------------------------------------------------------FIN SECTOR DE PRODUCTOS------------------------------------------------------------>





#<------------------------------------------------------ INICIO ENTREGABLE INTEGRACIÓN------------------------------------------------------------>

@musicpro.route('/entregableprofe', methods=['GET'])
def retornar_profesor():
    return "mensaje correcto <3"

#<--------------------------------------------------------FIN ENTREGABLE INTEGRACIÓN-------------------------------------------------------------->





if __name__ == '__main__':
    musicpro.run(debug=True, host='0.0.0.0')

