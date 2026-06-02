from googleapiclient.discovery import build
import json

api_key = 'AIzaSyBKee1FNNg0jxGpCGqwywjJbLRrYGrsnIo'

youtube = build("youtube", "v3", developerKey=api_key)


request = youtube.search().list(
        q="A Day In The Life of A Software Engineer In Mumbai | Blockchain Developer | SB Jain College Nagpur", #thing to search
        part="snippet",   
        type="video", #video ho
        maxResults=5
    )
response = request.execute()

# print(response)

with open('file.json','w') as f:
    json.dump(response,f)



