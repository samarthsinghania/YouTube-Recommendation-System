import json as js 
import numpy as np
from YoutubeTags import videotags # for tag extraction
from googleapiclient.discovery import build #for youtube extraction

class Fily:
    def __init__(self):
        self.special = set(";@!$%#^&*(_-+={[|//,\\?.,<>~`:;']})") #edited to set here
        self.api_key = 'AIzaSyBKee1FNNg0jxGpCGqwywjJbLRrYGrsnIo'

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

        file_path = "NormalData.json"

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
    #word extractor
    def word_extractor(self, unbaked, baked=[]):
        '''(This is a Recursion Method, Thank God it was in my mind)
        This method takes 1 parameter -> array  (of all words)
        Then It returns a array with seperated new words'''

        #make new list, empty, keep adding in it easy,
        for word in unbaked:
            for char in word:
                if char in self.special: #if special character
                    # unbaked.append(word.split(char)) 
                    unbaked = unbaked + word.split(char) #add splitted word
                    unbaked.remove(word) #remove word from orignal copied list 
                    break
            else:
                unbaked.remove(word)
                baked.append(word)
        
        if unbaked ==[]:
            return baked
        else:
            return self.word_extractor(unbaked,baked)
        
    def tag_extractor(self,vidid):
        '''Takes video id, returns tags in a list'''
        link = f"https://www.youtube.com/watch?v={vidid}"

        tag = videotags(link).split(",")

        return [item.strip() for item in tag]
    
    def raw_data_gen(self, query,max,countrycode="IN"):
        '''This Function takes 3 Parameters: 
         1. query(like which topic)
         2. max (max videos you want in output)
         3. countrycode-> from which country video should be
         
         Return 1 for successful 
         Otherwise 0'''
        youtube = build("youtube", "v3", developerKey=self.api_key)

        request = youtube.search().list(
            q= query, #thing to search
            part="snippet",   
            type="video", #Type
            maxResults= max, #how many results
            regionCode= countrycode, #Country
            relevanceLanguage="en",
            videoEmbeddable="true", #Video Embeddable
        )
        response = request.execute()
        try: 
            with open('file.json','w') as f:
                js.dump(response,f)
        except Exception as e:
            return 0
        else:
            return 1
        
    def vector_creator(self, words, set_vectorformat):
        "This Function takes 2 parameters:"
        "1. words: All the words of given video in list format"
        "2. set_vectorformat: The All-words vector in set form"
        list_vectorformat = list(set_vectorformat)
        vector = np.zeros(len(list_vectorformat),dtype=np.int8)
        for word in words:
            if word in set_vectorformat: #if inside set,
                index = list_vectorformat.index(word)
                vector[index] = 1
            else:
                return "Error: word not found in set HOW"
            
        return vector.tolist() #return List form of that vector
    




            
        
        