from Google.Google import Create_Service
from Google.ObtenerTokens import obtener_token

def crear_carpeta(nombre_pariente,nombre_carpeta):
    CLIENT_SECRET_FILE = "Google/client_secret.json"
    API_NAME = "drive"
    API_VERSION = "v3"
    SCOPES = ["https://www.googleapis.com/auth/drive"]

    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    tipo = ["application/vnd.google-apps.folder","application/vnd.google-apps.folder"]
    
    carpetas = [nombre_carpeta]

    if nombre_pariente:
        token_pariente,auxiliar = obtener_token(nombre_pariente,tipo)
        folder_id = token_pariente
        for carpeta in carpetas:
            file_metadata = {
                "name" : carpeta,
                "mimeType" : "application/vnd.google-apps.folder",
                "parents" : [folder_id]
            }
            service.files().create(body=file_metadata).execute() 
    else:
        for carpeta in carpetas:
            file_metadata = {
                "name" : carpeta,
                "mimeType" : "application/vnd.google-apps.folder"
            }
            service.files().create(body=file_metadata).execute()
    
    
    
    

    
        
    
        
        
        
        