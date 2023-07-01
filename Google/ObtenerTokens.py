from Google.Google import Create_Service

def obtener_token(nombre,tipo):
    CLIENT_SECRET_FILE = "Google/client_secret.json"
    API_NAME = "drive"
    API_VERSION = "v3"
    SCOPES = ["https://www.googleapis.com/auth/drive"]

    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    
    response  = service.files().list().execute()
    files = response.get('files')
    
    for file in files:
        if  file.get('name') == nombre and (file.get('mimeType') == tipo[0] or file.get('mimeType') == tipo[1]):
            token = str(file.get('id'))
            name = str(file.get('name'))
            break
        else:
            token = None
            name = None

    if token and name:
        return token,name
    else: 
        return None,None