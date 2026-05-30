import json as js 

class Fily:
    def __init__(self):
        pass

    def Raw_Data_To_Normal(self, raw_dict): 
        '''This function Takes in Raw_Response from YouTube and returns as in this format:
        {vidId: [thumbnail_path, title, description]}'''

        videos = raw_dict['items'] #this return list containing video as dict
        vid = {}
        for video in videos: #return each video dict
            vidID = video['id']['videoId'] #2dict
            title = video["snippet"]["title"]
            description = video["snippet"]["description"]
            thumbnail_path = video["snippet"]["thumbnails"]["high"]["url"]
            vid[vidID] = [thumbnail_path,title,description]
        return vid

