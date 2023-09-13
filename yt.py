import google.auth
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
import os
import pickle

API_KEY = 'AIzaSyC-hInglYjbjMjkpUMfzFw9FxKgc4jLyJ8'
import os
import pickle
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Set API key


# Set up OAuth 2.0 credentials
creds = None
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'client_secret.json',
            scopes=['https://www.googleapis.com/auth/youtube.upload'],
            redirect_uri='http%3A%2F%2Flocalhost%3A8000'
        )
        creds = flow.run_local_server(port=0)
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

# Set up API client
youtube = build('youtube', 'v3', developerKey=API_KEY, credentials=creds)

# Set up video upload request
request_body = {
    'snippet': {
        'title': 'Video title',
        'description': 'Video description',
        'tags': ['tag1', 'tag2']
    },
    'status': {
        'privacyStatus': 'private'
    }
}

# Set up video file upload
from googleapiclient.http import MediaFileUpload
media_file = MediaFileUpload('D:\Sarab youtube\\automated videos\\automated videos\image_7.png_edited.mp4')

# Execute the upload request
try:
    response = youtube.videos().insert(
        part='snippet,status',
        body=request_body,
        media_body=media_file
    ).execute()
    print(response)
except HttpError as error:
    print(f'An error occurred: {error}')
