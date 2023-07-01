from Google.Google import Create_Service
import os
import io
from googleapiclient.http import MediaIoBaseDownload
from Google.ObtenerTokens import obtener_token
from utils.gen_route import route

def descargar_archivo(nombres,tipos):
    CLIENT_SECRET_FILE = "Google/client_secret.json"
    API_NAME = "drive"
    API_VERSION = "v3"
    SCOPES = ["https://www.googleapis.com/auth/drive"]

    resultado = route("DSW-ProyectoCondosa-main","\\static\\img\\cache")
    
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    
    file_names = []
    file_ids = []
    
    for nombre in nombres:
        token_aux,nombre_aux = obtener_token(nombre,tipos)
        
        if token_aux and nombre_aux:
            file_ids.append(token_aux)
            file_names.append(nombre_aux)
    
    nombre_resultado = None

    for file_id, file_name in zip(file_ids, file_names):
        
        nombre_resultado = file_name
        
        request = service.files().get_media(fileId=file_id)
        
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fd = fh, request=request)
        done = False

        while not done:
            status, done = downloader.next_chunk()
            print("Download progress {0}".format(status.progress() * 100))

        fh.seek(0)

        with open(os.path.join(resultado, file_name), "wb") as f:
            f.write(fh.read())
            f.close()
        
    return nombre_resultado 
        
    