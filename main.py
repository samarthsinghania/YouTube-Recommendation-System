import numpy as np
import json as js

class main_control:
    def __init__(self):
        self.vidid = None
        #To Do: Random video'er here(which puts random videos for first time)

    def cosine_similar_top_n(self, given_vector_id, quantity):
        '''This function takes in 2 Parameters:
        1. given_vector: the video id of the given vector
        2. quantiy (n): the top n  cosine similar's videoid(s)
        Returns the vid id of top n in list format'''

        
        with open("vector.json", "r") as f:
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
