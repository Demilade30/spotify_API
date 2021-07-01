import requests
from googleapiclient.discovery import build

uri = 


from pyyoutube import Api
api = Api(api_key="AIzaSyCdaSyclngkLTsXd8Xiix3KrnMExgP5EOI")

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.channels().list(
        part='status',
        forUsername=''
)

response = request.execute()
print(response)