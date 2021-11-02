from __future__ import print_function
import os
import shutil
import math
import subprocess
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2.credentials import Credentials
from io import BytesIO
import concurrent.futures

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive',
          'https://www.googleapis.com/auth/drive.file']


dir = "./"
creds = None
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

drive = build('drive', 'v3', credentials=creds)


def get_folder_videos(folder_id):
    files = drive.files().list(q="'{}' in parents and mimeType='video/mp4'".format(
        folder_id)).execute().get('files', [])
    return files


def download_video(file):
    req = drive.files().get_media(fileId=file.get("id"))
    print("Downloading " + file.get("name"))
    fh = BytesIO()
    downloader = MediaIoBaseDownload(fh, req)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print(f"Download {int(status.progress() * 100)}")
        with open(file.get('name'), 'wb') as video:
            video.write(fh.getbuffer())
    return file.get("name")


def split_video(dir_path, video):
    video_path = dir_path + "/" + video
    frame_per_second = math.ceil(1/60) # frames / seconds
    p = subprocess.Popen(["ffmpeg", "-i", video_path, "-r",
                          str(frame_per_second), dir_path + "/frame_%04d.png"])
    while p.poll() is None:
        print("spliting  lecture ", end="\r")
    else:
        convP = subprocess.Popen(
            ["convert", dir_path + "/*.png", video.split(".")[0] + ".pdf"])


def move_video(file):
    dir_name = file.split(".")[0]
    dir_path = dir + dir_name
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    if os.path.exists(dir_path):
        file_path = dir + file
        shutil.move(file_path, dir_path)
    split_video(dir_path, file)


def download_folder(folder_id, creds):
    files = get_folder_videos(folder_id)
    for file  in files:
        download_video(file)
        move_video(file.get("name"))



def main():
    folder_drive_id = str(input("Enter Drive Id: "))
    download_folder(folder_drive_id, creds)


if __name__ == '__main__':
    main()
