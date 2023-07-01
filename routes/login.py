from flask import Blueprint, render_template as rt, request, url_for, redirect
from routes.contratos import borrar_cache

bp = Blueprint('index', __name__) #al llamar el blue print en base sería (NomreBP.FuncionAsociadaARuta)

@bp.route('/', methods=['GET', 'POST'])
def index(): #esta función debe coincidir con el url_for del html (base)
    borrar_cache(["Vacio.png"])
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        data_prueba = {
            "antonyctmre@gmail.com":{
                "password": "qwerty",
                "nombre": "Antony",
                "apellido": "Vargas",
                "cargo": "Contratista",
                "tipo": "personal",
                "id": "3"
            },
            "arnold8900@gmail.com":{
                "password": "qwerty",
                "nombre": "Arnold",
                "apellido": "Camacho",
                "cargo": "Admin",
                "tipo": "personal",
                "id": "1"
            },
            "luis@gmail.com":{
                "password": "qwerty",
                "nombre": "Luis",
                "apellido": "Jimenez",
                "cargo": "Pdte Junta Propietarios",
                "tipo": "solicitante",
                "id": "5"
            }
        }
        
        if email in data_prueba.keys():
            # Los datos coinciden, realizar acciones adicionales
            d_password = data_prueba.get(email).get("password")
            if password==d_password:
                print("Exito")
                id = data_prueba.get(email).get("id")
                tipo = data_prueba.get(email).get("tipo")
                print(url_for('principal.principal' ,tipo = tipo ,id = id))
                
                return redirect(url_for('principal.principal',tipo = tipo  , id = id))
            else:
                print("Fallo")
        else:
            # Los datos no coinciden, mostrar mensaje de error
            print("Fallo")
    return rt("index.html") #El rendertemplate siempre buscará el archivo en templates