import pickle
import os
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from google.auth.transport.requests import Request
from googleapiclient.errors import HttpError
from oauth2client.service_account import ServiceAccountCredentials
import datetime


def Create_Service(client_secret_file, api_name, api_version, *scopes):
    print(client_secret_file, api_name, api_version, scopes, sep='-')
    CLIENT_SECRET_FILE = client_secret_file
    API_SERVICE_NAME = api_name
    API_VERSION = api_version
    SCOPES = [scope for scope in scopes[0]]
    print(SCOPES)

    cred = None

    pickle_file = f'token_{API_SERVICE_NAME}_{API_VERSION}.pickle'
    # print(pickle_file)

    if os.path.exists(pickle_file):
        with open(pickle_file, 'rb') as token:
            cred = pickle.load(token)

    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            cred = flow.run_local_server(port=5001)

        with open(pickle_file, 'wb') as token:
            pickle.dump(cred, token)

    try:
        service = build(API_SERVICE_NAME, API_VERSION, credentials=cred)
        print(API_SERVICE_NAME, 'service created successfully')
        return service
    except Exception as e:
        print('Unable to connect.')
        print(e)
        return None

def convert_to_RFC_datetime(year=1900, month=1, day=1, hour=0, minute=0):
    dt = datetime.datetime(year, month, day, hour, minute, 0).isoformat() + 'Z'
    return dt

def getCarpetID(CLIENT_SECRET_FILE, SCOPES,folder_name):
    
    credentials = ServiceAccountCredentials.from_json_keyfile_name(CLIENT_SECRET_FILE, SCOPES)
    
    drive_service = build('drive', 'v3', credentials=credentials)
   
    try:
        response = drive_service.files().list(
            q="mimeType='application/vnd.google-apps.folder' and name='{}'".format(folder_name),
            fields="files(id)").execute()

        # Obtener el ID de la carpeta si existe
        if len(response['files']) > 0:
            folder_id = response['files'][0]['id']
            return (str(folder_id))
        else:
            return (None)
    except HttpError as e:
        return (None)