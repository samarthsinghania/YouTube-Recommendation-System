import numpy as np

class main_control:
    def __init__(self):
        self.vidid = None

    def cosine_similar(self, given_vector, main_vector):
        '''This function takes in 2 Parameters:
        1. given_vector: the video given vector
        2. main_vector: the total vector numpy array
        Returns the vid id of top n'''

        cosine_list = []

        for vector in main_vector:
            a_mag = np.linalg.norm(given_vector)
            b_mag = np.linalg.norm(vector)

            dot = np.dot(given_vector,vector)

            cosine_similar = dot/(a_mag*b_mag)
            cosine_list.append(cosine_similar)
        
        return np.array(cosine_list)
