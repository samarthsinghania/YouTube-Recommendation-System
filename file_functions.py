import json as js 

class Fily:
    def __init__(self):
        pass

    def Raw_Data_To_Normal(self, raw_dict): 
        '''This method Takes in Raw_Response from YouTube and returns as in this format:
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

    def data_appender(self, new_data):
        '''This method takes 1 parameters: 
        1. new_data -> in dict form(Which basically is what to be appended)'''

        file_path = "NormalDadta.json"

        try:
            with open(file_path,"r") as f:
                data  = js.load(f)
            with open(file_path, "w") as f:
                data.update(new_data)
                js.dump(data, f)
        
        #Just some Exception Handling
        except js.decoder.JSONDecodeError as e: #if error return 0
            return "FileEmpty: The NormalData File is empty my guy"
        except FileNotFoundError as e:
            return "No file exists with this name"
        except Exception as e:
            return "General: Error came oh no!"
        else: #no error return 1
            return 1

        