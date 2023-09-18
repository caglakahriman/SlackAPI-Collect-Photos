from slack_bolt import App
import json
import requests
import urllib.request
import dotenv
import os
import shutil
from io import BytesIO

dotenv.load_dotenv()
app = App(token = os.environ["BOT_TOKEN"])

response = app.client.conversations_list()
channels = response["channels"]

for channel in channels:
    if (channel['name'] == 'channel_name1' or channel['name'] == 'channel_name2' or channel['name'] == 'channel_name3'):
        response = app.client.files_list(channel=channel["id"])
        files = response["files"]
        for file in files:
            url_private = file["url_private_download"]
            file_name = file["name"]
            if (file_name.endswith(".jpg") or file_name.endswith(".png") or file_name.endswith(".jpeg")):
                file_path = f"pictures/{file_name}"
                response = requests.get(url_private, stream=True)
                with open(file_path, 'wb') as out_file:
                    shutil.copyfileobj(BytesIO(response.content), out_file)