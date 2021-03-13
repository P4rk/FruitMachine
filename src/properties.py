import os

TOKEN = os.environ.get('TOKEN')
SERVER_ID = os.environ.get('SERVER_ID', '')
SERVER_ID = int(SERVER_ID) if SERVER_ID else None
