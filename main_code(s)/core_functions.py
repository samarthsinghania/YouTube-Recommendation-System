import numpy as np
import json as js
import random
from file_functions import Fily

class main_control:
    def __init__(self):
        self.vidid = None
        self.fily_obj = Fily()
        #To Do: Random video'er here(which puts random videos for first time)

    def cosine_similar_top_n(self, given_vector_id, quantity):
        '''This function takes in 2 Parameters:
        1. given_vector: the video id of the given vector
        2. quantiy (n): the top n  cosine similar's videoid(s)
        Returns the vid id of top n in list format'''

        
        with open("main_code(s)/json_files/vector.json", "r") as f: #vectorjso contains
            vidinfo = js.load(f)
            
        #its(vidinfo) in form: d ={'vidid': vector,..}
        
        given_vector = vidinfo[given_vector_id]

        cosine_list = []
        for vidid in vidinfo:
            if given_vector_id==vidid: #ignore if given is there
                pass
            else:
                vector = vidinfo[vidid]
                a_mag = np.linalg.norm(given_vector) #magnitudes 
                b_mag = np.linalg.norm(vector)

                dot = np.dot(given_vector,vector) #dot product
    
                cosine_similar = dot/(a_mag*b_mag) #costheta
                cosine_list.append((vidid, cosine_similar)) #appending to list
        #format: [(vidid, cosine_similar),...]

        #sorting on basis of 2nd element
        sorted_cosine_list = sorted(cosine_list,key=lambda x:x[1],reverse=True)

        topn=[]
        for i in range(0,quantity):
            topn.append(sorted_cosine_list[i][0])
        
        return topn

    def random_vid_id_sender(self, how_many):
        '''This Method returns random videos's id in a list format,
        1. how_many : ho  w many videos you want'''

        with open("main_code(s)/json_files/normal_data.json", 'r') as f:
            normal_dic = js.load(f)

        all_keys = list(normal_dic.keys()) #random throws TypeError in .keys() dtype('dict_keys' object)

        random_videos = []
        for i in range(how_many):
            random_videos.append(random.choice(all_keys))
        
        return random_videos

    def update_vid_recommender_with_latest_video(self, vid_id):
        '''This method takes latest video id(clicked by user)
        then finds cosine similar and updates the current video list in 

        1. vid_id : latest video clicked video id
        returns 1 for successfull execution, otherwise 0 '''
        try:
            top_9 = self.cosine_similar_top_n(vid_id,3)

            vids_streamlit = list()
            print(vids_streamlit)
            with open("main_code(s)/json_files/vid_detail_streamlit.json", 'r') as f:
                streamlit_json_dic = js.load(f) 
            

            #Updating the Cache:
            obj = Fily()
            obj.cache_updater([vid_id,top_9])

            #Updating for 1
            vids_streamlit = vids_streamlit + top_9[:5:2] #adds index 0,2,4 elements
            #Update 2
            
            lis_2 = streamlit_json_dic['cache'][1][1]
            vids_streamlit.append(lis_2[1])
            vids_streamlit.append(lis_2[3])

            #Update 3
            lis_3 = streamlit_json_dic['cache'][2][1]
            vids_streamlit.append(lis_3[5])

            #Update 4
            lis_4 = streamlit_json_dic['cache'][3][1]
            vids_streamlit.append(lis_4[6])

            #Update 5
            lis_5 = streamlit_json_dic['cache'][4][1]
            vids_streamlit.append(lis_5[7])

            #Update 6
            lis_6 = streamlit_json_dic['cache'][5][1]
            vids_streamlit.append(lis_6[8])
            
            #Update 7 (random 3 videos)
            lis_7 = self.random_vid_id_sender(3) #getting 3 random videos's id
            vids_streamlit = vids_streamlit + lis_7

            #Updating Vid_streamlit
            obj.vids_streamlit_updater(vids_streamlit)
        
        except Exception as e:
            return f"0 : Oh error, {e}"
        else:
            return 1
    
    def reset_homepage_to_random(self):
        '''This Method resets the video data in vid_Details_streamlit.json to random videos
        return 1 for success
        return 0 other wise + the error'''

        try:
            #gathering random video id
            random_vids = self.random_vid_id_sender(9)

            #iterate
            cache = []
            for vid in random_vids:
                similar = self.cosine_similar_top_n(vid,9)
                pair = [vid, similar] #to match catch for format in cache
                cache.append(pair)

            self.fily_obj.cache_updater(cache)
            self.fily_obj.vids_streamlit_updater(random_vids)
        
        except Exception as e:
            return f"0, Sorry error: {e}"
        else:
            return 1
    