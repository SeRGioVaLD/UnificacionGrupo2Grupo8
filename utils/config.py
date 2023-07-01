from dotenv import load_dotenv
import os

def getURI():
    #CARGA LAS VARIABLES DE ENTORNO DEL .env
    load_dotenv()

    #SE ALMACENAN EN VARIABLES
    user = os.environ["USER"]
    password = os.environ["PASSWORD"]
    host = os.environ["HOST"]
    database = os.environ["DATABASE"]
    server = os.environ["SERVER"]

    #SE GENERA EL URI PARA ENTRAR AL PROYECTO
    DATABASE_CONNECTION_URI = f'{server}://{user}:{password}@{host}/{database}'
    return DATABASE_CONNECTION_URI

class Config:
    SECRET_KEY = 'my-secret-key'
    DEBUG = True
    # Configuramos la base de datos que vamos a utilizar para nuestra aplicación
    SQLALCHEMY_DATABASE_URI = getURI()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Configuramos el tiempo máximo de caché a 0 para evitar problemas de actualización
    SEND_FILE_MAX_AGE_DEFAULT = 0