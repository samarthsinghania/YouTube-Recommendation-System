import json as js 
import numpy as np
from YoutubeTags import videotags # for tag extraction
from googleapiclient.discovery import build #for youtube extraction

class Fily:
    def __init__(self):
        self.special =  '''"&*(_#-+={$^@[|//,\\?.,<>~`:;']})"''' #edited to set here
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

    def dictionary_data_appender(self, new_data, file_path):
        '''This method takes 1 parameters: 
        1. new_data -> in dict form(Which basically is what to be appended)
        2. file_path -> the files' path
        This functions appends something to a dictionary in a folder ok,'''
        
        # file_path = "NormalData.json"

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
    def word_extractor(self, given_words, lower=False):
        '''(This is a Recursion Method)
        This method takes 1 parameter -> array  (of all words)
        Special lower Parameter: True means convert to lower, else false
        Then It returns a array with seperated new words'''

        #Plan Use Translate table and str.translate() method for this

        translate_table =  str.maketrans({i:" " for i in self.special})
        
        output_words = []
        try: 
            for word in given_words:
                if lower ==True:
                    word = word.lower()
                new_word_list  = (word.translate(translate_table)).split()
                output_words = output_words + new_word_list
        except Exception as e:
            return f"Oh no error..{e}"
        else:
            return output_words

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
            videoDuration= 'medium' #Remove Shorts (Keep video Between 4-20 minutes)
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
        '''This Function takes 2 parameters:
        1. words: All the words of given video in list format
        2. set_vectorformat: The All-words vector in set form
        And returns the vector in list form'''
        list_vectorformat = list(set_vectorformat)
        vector = np.zeros(len(list_vectorformat),dtype=np.int8)
        for word in words:
            if word in set_vectorformat: #if inside set,
                index = list_vectorformat.index(word)
                vector[index] = 1
            else:
                return "Error: word not found in set HOW"
            
        return vector.tolist() #return List form of that vector
    
    
    def vids_streamlit_updater(self, vid_list):
        '''This Method takes the updated vid_list and updates it in file vid_detail_streamlit.json's
        vid_streamlit key.
        Reuturn 1 for Successfull Execution Otherwise 0'''

        try:
            with open("vid_detail_streamlit.json", 'r') as f:
                loaded_streamlit_dic = js.load(f)
            loaded_streamlit_dic["vids_streamlit"] = vid_list
            with open("vid_detail_streamlit.json", 'w') as f:
                js.dump(loaded_streamlit_dic,f)
        except Exception as e:
            return f"0 Error came oh no..{e}"
        else:
            return 1
        
    def cache_updater(self, vid_id):
        '''This functoin takes in latest video  id to be updated in key "cache" of
        vid_detail_streamlit.json and updates it'''
        try:
            with open("vid_detail_streamlit.json", 'r') as f:
                loaded_streamlit_dic = js.load(f)
            
        except Exception as e:
            return f"0 Error came oh no..{e}"
        else:
            try:
                temporary = loaded_streamlit_dic['cache'] #returns List in cache
                temporary.insert(0,vid_id)                  #add vid id at index 0
                temporary.pop()                             #remove very last index item

                loaded_streamlit_dic['cache'] = temporary
                with open("vid_detail_streamlit.json", 'w') as f:
                    js.dump(loaded_streamlit_dic,f)
            except Exception as e2:
                return f"Error oh no..{e2}"
            else:
                return 1
            
        
        